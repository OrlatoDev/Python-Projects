import os
from time import sleep
from tkinter import *
from tkinter import messagebox

window = Tk()

window['bg'] = "black"
window.resizable(False, False)
window.geometry("600x350+150+100")
window.title("CESAR Encoding")
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#FUNCTIONS
def encoding():
    error = False
    word = entry1.get()
    #TRANSFORMA A PALAVRA EM UMA LISTA
    wordlisted = list(word)

    #CRIA A VARIAVEL CHAR QUE FUNCIONA COMO UM CONTADOR REFERENCIAL PARA O CARACTERE DA PALAVRA
    char=0
    #CRIA A LISTA POS PARA GUARDAR OS VALORES DA POSICAO DA LETRA DA PALAVRA NO ALFABETO
    pos=[]
    #LACO FOR QUE REPETE O NUMERO DE VEZES DO LENGTH DA LISTA DA PALAVRA
    for encrypt in range(len(wordlisted)):
        #AQUI COMECA E ENCRIPTOGRAFIA, A LISTA VAI SENDO PREENCHIDA COM OS NUMEROS QUE SE REFEREM AO INDEX
        #DA LETRA NO ALFABETO E ADICIONA MAIS 3 POSICOES AO INDEX (IDEIA DA CRIPTOGRAFIA DE CESAR)
        try:
            #VERIFICA SE TEM ESPACO OU AS LEtRAS X, Y E Z
            if wordlisted[char] == " ":
                pos.append(" ")
            elif wordlisted[char] == "x":
                pos.append(0)
            elif wordlisted[char] == "y":
                pos.append(1)
            elif wordlisted[char] == "z":
                pos.append(2)
            else:
                pos.append(alfabeto.index(wordlisted[char])+3)
        except:
            #SE DE RUIM É PQ TEM ACENTO OU CEDILHA OU SLA
            messagebox.showerror("Erro", "Não use caracteres especiais, números ou acentos!")
            error = True
            break
        #ADICIONA 1 A VARIAVEL CONTADORA PARA INDICAR Que FOI "LIDO" MAIS UM CARACTERE
        char+=1
    #LISTA COM A PALAVRA ENCRIPTOGRAFADA
    wordencryptografedlist = []
    #CONTADOR
    i = 0
    #LACO FOR Q REPETE O NUMERO DE VEZES CORRESPONDENTES AO NUMERO DE CARACTERES
    for substitution in range(len(pos)):
        #SUBSTITUI O NUMERO DA POSICAO PELA LETRA CORRESPONDENTE E VERIFICA SE TEM ESPACO
        if pos[i] == " ":
            wordencryptografedlist.append(" ")
        else:
            wordencryptografedlist.append(alfabeto[pos[i]])
        #ADICIONA 1 AO CONTADOR
        i += 1
    #CRIA UMA VAIRAVEL NA QUAL TEM A LISTA "TRANSFORMADA" EM STRING
    wordencryptografed = "".join(wordencryptografedlist)
    #SE TIVER ERRO N PRINTA A PALAVRA ATE ONDE ELE CONSEGUIU FAZER
    if error == True:
        pass
    else:
        result['state'] = NORMAL
        result.delete(1.0, END)
        result.insert(END, wordencryptografed)
        result['state'] = DISABLED

#WIDGETS
title = Label(window, text="Cryptografador CESAR", font="Helvetica 20", bg="black", fg="white")
title.pack(side=TOP, pady=20)

str1 = Label(window, text="Escreva algo (evite caracteres especiais, acentos e números):", font="Helvetica 12", bg="black", fg="white")
str1.pack(side=TOP)

entry1 = Entry(window, bg="gray10", fg="white", font="Helvetica 12", width=700, relief=FLAT)
entry1.pack(side=TOP, pady=20, padx=20)

btn1 = Button(window, text="Encriptografar", bg="gray10", fg="white", font="Helvetica 12", width=30, relief=FLAT, command=encoding)
btn1.pack()

result = Text(window, bg="gray10", fg="white", font="Helvetica 12", relief=FLAT, width=700, state=DISABLED)
result.pack(side=TOP, pady=20, padx=20)

window.mainloop()