from tkinter import *
import os
import platform
import sys
from login import *
'''
Genius(Lite) Login Main Ui 1.0 - GLMU
'''
#Criação da janela principal
janela = Tk()
janela.title('Genius')
janela['bg'] = '#212121'
#LARGURA X ALTURA + ESQUERDA + TOPO  
janela.geometry('850x500')
#----------------------------------------------------
#Botões
login = Button(janela, width=40, text='Login',command=testeBotao)
login.place(x=400, y=100)
lb = Label(janela, text='Clica no botão bença')
lb.place(x=400,y=160)


#Exibição da janela principal.
janela.mainloop()
#----------------------------------------------------