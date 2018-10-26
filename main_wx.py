from func.login import *
from tkinter import *
import os
import platform
import wx
'''
def btEntrar():
	
    if (login.get() == '' or senha.get() == ''):
    	print('Campos vazios')
    elif(login.get().isnumeric()):
    	loginEntrada = login.get()
    	senhaEntrada = senha.get()
    	if (loginEntrada in logins):
    			if (senhaEntrada == logins[loginEntrada][1]):
    				print('Logado como',logins[loginEntrada][3])
    				print('Usuario Nivel',logins[loginEntrada][4])
    			else:
    				print('Senha incorreta :(')
    	else:
    		print('Usuário não encontado :(')
    else:
    	print('O campo de login só aceita números :(')

def btPrimAcesso():
    primeiroAcesso = Tk()
    primeiroAcesso.geometry('300x300')
    primeiroAcesso.mainloop()
'''
#Inicio do programa

#Criação de variáveis e carregamento de codigos
logins = {}
codigos = {}
carregaLogin(logins)
carregaCodigos(codigos)

#Janela e widgets
app = wx.App()
janela = wx.Frame(None,-1,'Genius', style = wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.CLOSE_BOX|wx.CAPTION,size=(850,460))

bt_entrar = wx.Button(app,label = 'Entrar')


#Posicionamento e exibição
janela.Centre()
janela.Show()
app.MainLoop()