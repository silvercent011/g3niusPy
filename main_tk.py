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
from tkinter import font, ttk, messagebox
from PIL import ImageTk, Image
#Sistema Operacional
import sys
import platform
import getpass

def btEntrar():
	
    if (login.get() == '' or senha.get() == ''):
    	messagebox.showerror('Ops!','Alguns campos de login estão vazios')
    elif(login.get().isnumeric()):
    	if (len(login.get()) < 11):
    		messagebox.showerror('Ops!', 'Seu CPF está completo?')
    	elif (len(login.get()) > 11):
        	messagebox.showerror('Ops!', 'Seu CPF tem mais de 11 números! Ele é exclusivo bença?')
    	else:
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
def botoesDeTeste(loginEntrada,usuario,nivel,alunos,janela):
		frameGeral.destroy()
		menuLevel(loginEntrada,usuario,nivel,alunos,janela)

'''
Menu inicial da aplicação
'''
logins = {}
codigos = {}
log = {}
alunos = {}
carregaLogin(logins)
carregaCodigos(codigos)
carregaLog(log)

version = 'Genius (LITE) - 7.0.1'
altura       = 10
largura      = 20
largura2     = 62
largura3	 = 17
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
fonteTopo5 = font.Font(family='Segoe Ui', size=35, weight='bold')
fonteTopo6 = font.Font(family='Segoe Ui', size=14, weight='bold')

s = ttk.Style()
s.configure('branco.TFrame',background='white')

r = ttk.Style()
r.configure('branco.TLabel',background='white')

frameGeral['style'] = 'branco.TFrame'

loginForms = ttk.Frame(frameGeral)
loginForms.grid(row=0,column=2)
loginForms['style'] = 'branco.TFrame'
loginForms['padding'] = (espacamento1,espacamento2)
separador = ttk.Separator(frameGeral, orient=VERTICAL)
separador.grid(row=0,column=1,sticky=N+S)
ladoInfo = ttk.Frame(frameGeral)
ladoInfo.grid(row=0,column=0,sticky=N)
ladoInfo['style'] = 'branco.TFrame'
ladoInfo['padding'] = (espacamento1,espacamento2)


#Lado Info
welcome = ttk.Label(ladoInfo,width=largura3,text='THINKED FOR ALL,\nBUILT \nFOR YOU!',font=fonteTopo5)
welcome.grid(row=0,column=0)
welcome['style'] = 'branco.TLabel'

suporte1 = ttk.Label(ladoInfo,text='')
suporte1.grid(row=7,column=0)
suporte1['style'] = 'branco.TLabel'

suporte2 = ttk.Label(ladoInfo,text='')
suporte2.grid(row=8,column=0)
suporte2['style'] = 'branco.TLabel'

suporte3 = ttk.Label(ladoInfo,text='')
suporte3.grid(row=9,column=0)
suporte3['style'] = 'branco.TLabel'

imagemLogo = ImageTk.PhotoImage(Image.open('./icons/logoSmall2.png'))
logo = ttk.Label(ladoInfo,text='Genius',image=imagemLogo)
logo.image = imagemLogo
logo.grid(row=10,column=0,sticky=S+W)
logo['style'] = 'branco.TLabel'

versao = ttk.Label(ladoInfo,text = version, font=fonteTopo3)
versao['style'] = 'branco.TLabel'
versao.grid(row=10,column=5,sticky=E)


#Lado Login
#LabelLogin
labelLogin = ttk.Label(loginForms, text='LOGIN(CPF):',font=fonteTopo2)
labelLogin.grid(row=6,column=10,sticky=W)
labelLogin['style'] = 'branco.TLabel'
#CampoLogin
login = ttk.Entry(loginForms,font=fonteTopo2)
login.grid(row=7,column=10,sticky=W+E,columnspan=2,pady=10)
#LabelSenha
labelSenha = ttk.Label(loginForms, text='SENHA:',font=fonteTopo2)
labelSenha.grid(row=8,column=10,sticky=W)
labelSenha['style'] = 'branco.TLabel'
#CampoSenha
senha = ttk.Entry(loginForms, show='*',font=fonteTopo2)
senha.grid(row=9,column=10,sticky=W+E,columnspan=2,pady=10)

#BtEntrar
imagemEntrar = ImageTk.PhotoImage(Image.open('./icons/30/Approval30px.png'))
entrar = ttk.Button(loginForms,width=largura, text='Entrar',command=btEntrar,compound=TOP, image=imagemEntrar)
entrar.image = imagemEntrar
entrar.grid(row=10,column=10,sticky=W+E,ipady=altura)
#BtPrimeiroAcesso
imagemPrimAcesso = ImageTk.PhotoImage(Image.open('./icons/30/Registration30px.png'))
primAcesso = ttk.Button(loginForms, width=largura,text='Primeiro Acesso?',command=btPrimAcesso,compound=TOP, image = imagemPrimAcesso)
primAcesso.image = imagemPrimAcesso
primAcesso.grid(row=10,column=11,sticky=W+E,ipady=altura)
#BtEsqueceuASenha
imagemEsqSenha = ImageTk.PhotoImage(Image.open('./icons/30/ForgotPassword30px.png'))
esqSenha =   ttk.Button(loginForms,width=largura, text='Esqueceu sua senha?',command=btEsqueceu,compound=TOP,image=imagemEsqSenha)
esqSenha.image = imagemEsqSenha
esqSenha.grid(row=11,column=10,sticky=W+E,ipady=altura)
#BtSair
imagemSair = ImageTk.PhotoImage(Image.open('./icons/30/Cancel30px.png'))
sair = ttk.Button(loginForms,width=largura,text='Sair',command=btSairInicio,compound=TOP,image=imagemSair)
sair.image = imagemSair
sair.grid(row=11,column=11,sticky=W+E,ipady=altura)


#ÁREA DE TESTES
level3 = ttk.Button(loginForms, width=largura, text='Level3', command=partial(botoesDeTeste,'000000000000','TESTE',3,alunos,janela))
level3.grid(row=14,column=10,sticky=W)

level4 = ttk.Button(loginForms, width=largura, text='Level4', command=partial(botoesDeTeste,'000000000000','TESTE',4,alunos,janela))
level4.grid(row=15,column=10,sticky=W)

level6 = ttk.Button(loginForms, width=largura, text='Level6', command=partial(botoesDeTeste,'000000000000','TESTE',6,alunos,janela))
level6.grid(row=16,column=10,sticky=W)



janela.configure(background='white')
janela.title('Genius')

janela.mainloop()
