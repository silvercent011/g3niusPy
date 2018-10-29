#Funcional
from functools import partial
#Funções
from func.login import *
from func.log import *
#TkInter
from tkinter import ttk
from tkinter import font
from tkinter import *
#Sistema
import sys
import platform
import getpass

def btSair(loginEntrada,usuario,nivel):
	
    colocaLog(loginEntrada,usuario,nivel,'SAIU DO SISTEMA')
    exit()

def menuLevel6(login,usuario,level):
    '''
    Menu para usuários nível 6
    '''
    info        = 'Usuário nível ' + str(level)
    altura      = ''
    largura     = 30
    largura2     = 62
    espacamento1 = 50
    espacamento2 = 20
    #Frame
    janela = Tk()
    janela.title('Genius - Acesso Nível ' + str(level))
    janela.resizable(FALSE,FALSE)
    level6 = ttk.Frame(janela)
    level6.grid(row=0,column=0)
    level6['padding'] = (espacamento1,espacamento2)
    #Informações Usuário e logo
    fonteTopo = font.Font(family='Segoe Ui', size=18, weight='bold')
    fonteTopo2 = font.Font(family='Segoe Ui', size=14, weight='normal')
    imagemLogo = PhotoImage(file='./icons/logoSmall2.png')
    logo = Label(level6,text='GENIUS',image=imagemLogo)
    logo.grid(row=0, column=0,columnspan=2,rowspan=2,sticky=W)

    labelUser = Label (level6, text=usuario, font=fonteTopo)
    labelUser.grid    (row=0, column=3,sticky=E)
    labelLevel = Label(level6, text=info, font=fonteTopo2)
    labelLevel.grid   (row=1,column=3,sticky=E)
    #Cadastrar Alunos
    imagemCadastro = PhotoImage(file='./icons/account80.png')
    cadastra_aluno = ttk.Button(level6,width=largura,compound=TOP,text='Cadastrar Alunos',image=imagemCadastro)
    cadastra_aluno.grid(row=4,column=0)
    #Pesquisar Alunos
    imagemPesquisa = PhotoImage(file='./icons/search80.png')
    pesquisa_aluno = ttk.Button(level6,width=largura,compound=TOP,text='Pesquisar Alunos',image=imagemPesquisa)
    pesquisa_aluno.grid(row=4,column=1)
    #Material Impresso
    imagemImpresso = PhotoImage(file='./icons/exam80.png')
    material_impresso = ttk.Button(level6,width=largura,compound=TOP,text='Material Impresso',image=imagemImpresso)
    material_impresso.grid(row=4,column=2)
    #Gerar Códigos
    imagemCodigos = PhotoImage(file='./icons/newDocument80.png')
    gerar_codigo = ttk.Button(level6,width=largura,compound=TOP,text='Gerar Cógidos',image=imagemCodigos)
    gerar_codigo.grid(row=4,column=3)
    #Gerenciar usuários
    imagemUsuarios = PhotoImage(file='./icons/gruposDeUsuários80.png')
    exibir_usuarios = ttk.Button(level6,width=largura,compound=TOP,text='Gerenciar Usuários',image=imagemUsuarios)
    exibir_usuarios.grid(row=5,column=0)
    #Log de Informações
    imagemLog = PhotoImage(file='./icons/overview80.png')
    exibir_log = ttk.Button(level6,width=largura,compound=TOP,text='Log de Informações',image=imagemLog)
    exibir_log.state(['disabled']) 
    exibir_log.grid(row=5,column=1)
    #Sair
    imagemSair= PhotoImage(file='./icons/cancel80.png')
    sair = ttk.Button(level6,width=largura2,compound=TOP,text='Sair',image=imagemSair,command=partial(btSair,login,usuario,level))
    sair.grid(row=5,column=2,columnspan=2)

    #level6.geometry('400x400')
    janela.geometry('870x400')
    janela.mainloop()

#menuLevel6(000000000000,'TESTE',0)