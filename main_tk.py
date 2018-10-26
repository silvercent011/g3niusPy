from tkinter import ttk
from func.login import *
from tkinter import *
#import tkinter as tk
import sys
import platform
import getpass

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
					
    				menuLevel6(logins[loginEntrada][3],logins[loginEntrada][4])
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

def menuLevel6(usuario,level):
	info = 'Usuário nível ' + str(level)
	level6 = Tk()
	labelUser = Label(level6, text=usuario)
	labelUser.grid(row=0, column=0)
	labelLevel = Label(level6, text=info)
	labelLevel.grid(row=1,column=0)
	level6.geometry('400x400')
	level6.mainloop()

#Inicio do programa
logins = {}
codigos = {}
carregaLogin(logins)
carregaCodigos(codigos)

janela = Tk()
loginForms = Frame(janela, width=300)

labelLogin = ttk.Label(loginForms, text='Login:')
labelSenha = Label(loginForms, text='Senha:')
login =      Entry(loginForms)
senha =      Entry(loginForms, show='*')
entrar =     Button(loginForms, width=20, text='Entrar',command=btEntrar )
primAcesso = Button(loginForms, width=20, text='Primeiro Acesso?',command=btPrimAcesso )

loginForms['bg'] = 'blue'

loginForms.pack(side=RIGHT)

labelLogin.grid(row=0 , column=10)
login.grid     (row=1 , column=10, columnspan=2)
labelSenha.grid(row=2 , column=10)
senha.grid     (row=3 , column=10, columnspan=2)
entrar.grid    (row=4 , column=10)
primAcesso.grid(row=5 , column=10)

janela.geometry('850x400')
janela.title('Genius')

janela.mainloop()
