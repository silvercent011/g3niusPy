#Sidney Alex
'''
Genius (Lite) Tkinter Main Interface - GTMI
'''
#Funções
from func.login import *
from func.log import *
from functools import partial
#Janelas
from menus.inicio_level6 import *
from menus.cadastra_usuario import *
#TkInter
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
#Sistema Operacional
import sys
import platform
import getpass

def btEntrar():
	
    if (login.get() == '' or senha.get() == ''):
    	messagebox.showerror('Ops!','Alguns campos de login estão vazios')
    elif (len(login.get()) < 11):
    	messagebox.showerror('Ops!', 'Seu CPF está completo?')
    elif (len(login.get()) > 11):
        messagebox.showerror('Ops!', 'Seu CPF tem mais de 11 números! Ele é exclusivo bença?')
    elif(login.get().isnumeric()):
    	loginEntrada = login.get()
    	senhaEntrada = senha.get()
    	if (loginEntrada in logins):
    			if (senhaEntrada == logins[loginEntrada][1]):
    				login.delete(0,END)
    				senha.delete(0,END)
    				usuario = logins[loginEntrada][3]
    				nivel = logins[loginEntrada][4]
    				colocaLog(loginEntrada,usuario,nivel,'LOGIN NO SISTEMA')
    				frameGeral.destroy()
    				menuLevel(loginEntrada,usuario,nivel,alunos,janela)
    			else:
    				messagebox.showerror('Ops!','A senha está incorreta')
    	else:
    		messagebox.showerror('Ops!','Usuário não encontrado em nossa base de dados')
    else:
    	messagebox.showerror('Ops!','O campo de login só aceita números :(')

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
alunos = {}
carregaLogin(logins)
carregaCodigos(codigos)
carregaLog(log)

'''
Menu inicial da aplicação
'''

version = 'Genius (LITE) - 7.0.1'
altura      = 10
largura     = 20
largura2     = 62
espacamento1 = 50
espacamento2 = 20


janela = Tk()
janela.resizable(FALSE,FALSE)
frameGeral = ttk.Frame(janela)
frameGeral.grid(row=0, column=0)
#Fontes e estilos
fonteTo5 = font.Font(family='Segoe Ui', size=18, weight='bold')
fonteTopo2 = font.Font(family='Segoe Ui', size=14, weight='normal')
fonteTopo3 = font.Font(family='Segoe Ui', size=12, weight='normal')
fonteTopo4 = font.Font(family='Segoe Ui', size=24, weight='bold')

s = ttk.Style()
s.configure('branco.TFrame',background='white')

r = ttk.Style()
r.configure('branco.TLabel',background='white')

loginForms = ttk.Frame(frameGeral)
loginForms.pack(side=RIGHT,fill=Y)
loginForms['style'] = 'branco.TFrame'
ladoInfo = ttk.Frame(frameGeral)
ladoInfo.pack(side=LEFT)
ladoInfo['style'] = 'branco.TFrame'


#Lado Info
welcome = ttk.Label(ladoInfo,width=largura,text='THINKED FOR ALL,\nBUILT FOR YOU!',font=fonteTopo4)
welcome.grid(row=0,column=0,sticky=N,columnspan=6,rowspan=7)
welcome['style'] = 'branco.TLabel'


#Lado Login
#LabelLogin
labelLogin = ttk.Label(loginForms, text='Login(CPF):',font=fonteTopo3)
labelLogin.grid(row=6,column=10,sticky=W)
labelLogin['style'] = 'branco.TLabel'
#CampoLogin
login = ttk.Entry(loginForms)
login.grid(row=7,column=10,sticky=E,columnspan=2)
#LabelSenha
labelSenha = ttk.Label(loginForms, text='Senha:',font=fonteTopo3)
labelSenha.grid(row=8,column=10,sticky=W)
labelSenha['style'] = 'branco.TLabel'
#CampoSenha
senha = ttk.Entry(loginForms, show='*')
senha.grid(row=9,column=10,sticky=E,columnspan=2)
#BtEntrar
entrar = ttk.Button(loginForms, width=largura, text='Entrar',command=btEntrar)
entrar.grid(row=10,column=10,sticky=W,ipady=altura)
#BtPrimeiroAcesso
primAcesso = ttk.Button(loginForms, width=largura, text='Primeiro Acesso?',command=btPrimAcesso)
primAcesso.grid(row=10,column=11,sticky=W,ipady=altura)
#BtEsqueceuASenha
esqSenha =   ttk.Button(loginForms, width=largura, text='Esqueceu sua senha?',command=btEsqueceu)
esqSenha.grid(row=11,column=10,sticky=W,ipady=altura)
#BtSair
sair =   ttk.Button(loginForms, width=largura, text='Sair',command=btSairInicio)
sair.grid(row=11,column=11,sticky=W,ipady=altura)

#ÁREA DE TESTES
level3 = ttk.Button(loginForms, width=largura, text='Level3', command=partial(menuLevel,'000000000000','TESTE',3,alunos,janela))
level3.grid(row=14,column=10,sticky=W)

level4 = ttk.Button(loginForms, width=largura, text='Level4', command=partial(menuLevel,'000000000000','TESTE',4,alunos,janela))
level4.grid(row=15,column=10,sticky=W)

level6 = ttk.Button(loginForms, width=largura, text='Level6', command=partial(menuLevel,'000000000000','TESTE',6,alunos,janela))
level6.grid(row=16,column=10,sticky=W)




janela['bg'] = 'white'
#janela.geometry('850x400')
janela.title('Genius')

janela.mainloop()
