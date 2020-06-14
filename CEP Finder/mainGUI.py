import requests
from tkinter import *
from time import sleep

window = Tk()

window.title("Consulta Endereço")
window['bg'] = "black"
window.geometry("425x300+300+100")
window.resizable(False, False)

result = Label(window, text="", bg="black", fg="white", justify=LEFT)
result.place(x=175, y=145)

def limpar():
    result['text'] = ""
    entrycep.delete(0, 'end')

def btn_Clicked():
    cep = entrycep.get()

    if len(cep) != 8 or not cep.isdigit():
        entrycep.delete(0, 'end')
        result['text'] = "CEP Inválido!"

    else:
        request = requests.get('https://viacep.com.br/ws/'+str(cep)+'/json/')
        datajson = request.json()

        if "erro" in datajson:
            entrycep.delete(0, 'end')
            result['text'] = "CEP "+str(cep)+" não encontrado!"

        else:
            localidade = datajson['localidade']
            bairro = datajson['bairro']
            rua = datajson['logradouro']
            estado = datajson['uf']

            if datajson['complemento'] == "":
                complemento = "Nenhum"
                pass
            else:
                complemento = datajson['complemento']

            result['text'] = "Cep: "+str(cep)+"\nCidade: "+str(localidade)+"\nBairro: "+str(bairro)+"\nRua: "+str(rua)+"\nEstado: "+str(estado)+"\nComplemento: "+str(complemento)
    entrycep.delete(0, 'end')

            
            

title = Label(window, text="Consulta Endereço", font="TimesNewRoman 15", bg="black", fg="red", pady=30)
title.pack(side=TOP)

cepstr = Label(window, text="Insira um CEP:", font="TimesNewRoman 10", bg="black", fg="white", padx=85)
cepstr.pack(side=TOP, ipady=5, anchor=W)

entrycep = Entry(window, width=35, bg="gray12", fg="white", font="TimesNewRoman 10")
entrycep.pack(side=TOP)

texto="Pesquisar"

button = Button(window, text=texto, bg="gray12", fg="white", font="TimesNewRoman 10", width=len(texto), command=btn_Clicked)
button.place(x=88, y=150)

limpar = Button(window, text="Limpar", bg="gray12", fg="white", font="TimesNewRoman 10", width=len(texto), command=limpar)
limpar.place(x=88, y=187)

window.mainloop()
