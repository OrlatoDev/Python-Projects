from tkinter import *
import requests

window = Tk()

window['bg'] = "#E9E6DF"
window.title("Valores Moedas")
window.geometry("350x350")
window.resizable(False, False)

title = Label(window, text="Cotação de Moedas", font="Ubuntu 25", bg="#E9E6DF")
title.pack()

options = [

"USD (Dólar)",
"EUR (Euro)",
"GBP (Libra)",
"ARS (Peso)",
"JPY (Iene Japonês)",
"CHF (Franco Suiço)",
"CNY (Yuan Chinês)",
"BTC (Bitcoin)"

]

clicked = StringVar()
clicked.set(options[0])

coin = OptionMenu(window, clicked, *options)
coin["bg"] = "#E9E6DF"
coin["relief"] = "groove"
coin["width"] = 18
coin["justify"] = LEFT
coin["font"] = "Ubuntu 12"
coin.pack(side=TOP, pady=10)

def btn_Clicked():
    textbox.delete(1.0, END)
    opraw = clicked.get()
    op = opraw[0:3]
    url = "https://economia.awesomeapi.com.br/all/"+str(op)+"-BRL"
    request = requests.get(url)
    datajson = request.json()
    filter1 = datajson[op]
    value = filter1['bid']
    textbox.insert(END, "R$"+str(round(float(value), 2)))

button1 = Button(window, bg="#E9E6DF", relief="groove", width=21, font="Ubuntu 12", text="Verificar", command=btn_Clicked)
button1.pack(side=TOP)

textbox = Text(window, bg="#E9E6DF", relief="groove", width=21, font="Ubuntu 12")
textbox.pack(side=TOP, pady=10)

window.mainloop()
