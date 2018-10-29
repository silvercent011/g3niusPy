#Sidney Alex
'''
Genius (Lite) Tkinter Main Interface - GTMI
'''
#Funções
from func.login import *
from func.log import *
#Janelas
from menus.inicio_level3 import *
from menus.inicio_level4 import *
from menus.inicio_level6 import *
from menus.cadastra_usuario import *
#TkInter
from tkinter import *
from tkinter import font
from tkinter import ttk
#Sistema Operacional
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
    				login.delete(0,END)
    				senha.delete(0,END)
    				usuario = logins[loginEntrada][3]
    				nivel = logins[loginEntrada][4]
    				if (int(logins[loginEntrada][4]) == 1):
    					pass
    				elif (int(logins[loginEntrada][4]) == 2):
    					pass
    				elif (int(logins[loginEntrada][4]) == 3):
    					colocaLog(loginEntrada,usuario,nivel,'LOGIN NO SISTEMA')
    					menuLevel3(loginEntrada,usuario,nivel)
    				elif (int(logins[loginEntrada][4]) == 4):
    					colocaLog(loginEntrada,usuario,nivel,'LOGIN NO SISTEMA')
    					menuLevel4(loginEntrada,usuario,nivel)
    				elif (int(logins[loginEntrada][4]) == 5):
    					pass
    				elif (int(logins[loginEntrada][4]) == 6):
    					colocaLog(loginEntrada,usuario,nivel,'LOGIN NO SISTEMA')
    					menuLevel6(loginEntrada,usuario,nivel)
    				elif (int(logins[loginEntrada][4]) == 7):
    					pass
    				elif (int(logins[loginEntrada][4]) == 8):
    					pass
    				elif (int(logins[loginEntrada][4]) == 9):
    					pass
    				elif (int(logins[loginEntrada][4]) == 10):
    					pass
    			else:
    				print('Senha incorreta :(')
    	else:
    		print('Usuário não encontado :(')
    else:
    	print('O campo de login só aceita números :(')

def btPrimAcesso():
	cadastraUsuarios(codigos,logins)

def btEsqueceu():
	messagebox.showinfo('Ops!','Função não implementada!')

def btSairInicio():
	exit()
#Inicio do programa
logins = {}
codigos = {}
log = {}
carregaLogin(logins)
carregaCodigos(codigos)
carregaLog(log)
print(log)
janela = Tk()
loginForms = Frame(janela)
loginForms.pack(side=RIGHT,fill=Y)
ladoInfo = Frame(janela)
ladoInfo.pack(side=LEFT,fill=X)

#Lado Info
welcome = ttk.Label(ladoInfo, text='Bem-Vindo ao Genius Lite')
welcome.pack()

#Lado Login
labelLogin = ttk.Label(loginForms, text='Login:')
labelSenha = ttk.Label(loginForms, text='Senha:')
login =      ttk.Entry(loginForms)
senha =      ttk.Entry(loginForms, show='*')
entrar =     ttk.Button(loginForms, width=30, text='Entrar',command=btEntrar)
primAcesso = ttk.Button(loginForms, width=30, text='Primeiro Acesso?',command=btPrimAcesso)
esqSenha =   ttk.Button(loginForms, width=30, text='Esqueceu sua senha?',command=btEsqueceu)
sair =   ttk.Button(loginForms, width=30, text='Sair',command=btSairInicio)

#loginForms['background'] = 'red'
ladoInfo['bg'] = 'green'
janela['bg'] = '#112233'


labelLogin.pack()
login.pack(fill=X)
labelSenha.pack()
senha.pack(fill=X)
entrar.pack()
primAcesso.pack()
esqSenha.pack()
sair.pack()

janela.geometry('850x400')
janela.title('Genius')

janela.mainloop()
