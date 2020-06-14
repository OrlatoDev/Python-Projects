#api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}
key = "f3175f3bed5f403e2d51e326eec0895b"
from time import sleep
from tkinter import *

import requests

window = Tk()
window.geometry("600x500+200+150")
window["bg"] = "blue"
window.title("Weather")

def pesquisa():
    cidade = city.get()

    url = "https://api.openweathermap.org/data/2.5/weather?q="+str(cidade)+"&appid="+str(key)+"&lang=pt_br"
    request = requests.get(url)
    data = request.json()

    try:
        main = data["main"]
    except:
        infos['text'] = "Cidade "+str(cidade)+" não encontrada!"
    else:
        climalista = data["weather"]
        climajson = climalista[0]
        descricao = climajson['description']
        tempk = main["temp"]
        umidaderaw = main["humidity"]
        sensacaok = main['feels_like']

        tempcelsius = round((tempk - 273.15), 2)
        sensacaocelsius = round((sensacaok - 273.15), 2)
        umidade = str(umidaderaw)+"%"

        city.delete(0, 'end')

        infos['text'] = "Cidade: "+str(cidade.capitalize())+"\nTemperatura: "+str(tempcelsius)+"°C\n"+"Sensação Térmica: "+str(sensacaocelsius)+"°C\n"+"Umidade: "+str(umidade)+"\nDescrição: "+str(descricao.capitalize())

title = Label(window, text="Tempo Rápido", bg="blue", fg="white", padx=30, font="Antipasto 40")
title.pack(side=TOP)

strinfo = Label(window, text="Digite uma cidade: ", bg="blue", fg="white", padx=30, font="Antipasto 15")
strinfo.pack(side=TOP, anchor=W)

city = Entry(window, bg="white", fg="black", font="Antipasto 15", width=1000)
city.pack(side=TOP, padx=30)

buttonpesquisa = Button(window, bg="blue", fg="white", font="Antipasto 15", text="Pesquisar", width=30, command=pesquisa)
buttonpesquisa.pack(side=TOP, pady=10)

infos = Label(window, bg="blue", fg="white", font="Antipasto 15", justify=LEFT, text="", padx=30)
infos.pack(side=TOP, anchor=W, pady=5) 

window.mainloop()
