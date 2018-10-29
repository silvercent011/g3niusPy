#Funcional
from functools import partial
from func.login import *
from func.log import *
from tkinter import ttk
from tkinter import *
import sys
import platform
import getpass

def btSair(loginEntrada,usuario,nivel):
	
    colocaLog(loginEntrada,usuario,nivel,'SAIU DO SISTEMA')
    exit()

def menuLevel4(login,usuario,level):
    '''
    Menu para usuários nível 6
    '''
    info = 'Usuário nível ' + str(level)
    level4 = Tk()
    #Cadastrar Alunos
    cadastra_aluno = ttk.Button(level4,width=20,text='Cadastrar Alunos')
    cadastra_aluno.grid(row=4,column=1)
    #Pesquisar Alunos
    pesquisa_aluno = ttk.Button(level4,width=20,text='Pesquisar Alunos')
    pesquisa_aluno.grid(row=5,column=1)
    #Gerenciar horários
    gerenciar_horarios = ttk.Button(level4,width=20,text='Gerenciar Horários')
    gerenciar_horarios.grid(row=6,column=1)
    #Material Impresso
    material_impresso = ttk.Button(level4,width=20,text='Material Impresso')
    material_impresso.grid(row=7,column=1)
    #Log de Informações
    exibir_log = ttk.Button(level4,width=20,text='Log de Informações')
    exibir_log.state(['disabled']) 
    exibir_log.grid(row=8,column=1)
    #Sair
    sair = ttk.Button(level4,width=20,text='Sair', command=partial(btSair,login,usuario,level))
    sair.grid(row=9,column=1)

    labelUser = Label (level4, text=usuario)
    labelUser.grid    (row=0, column=0)
    labelLevel = Label(level4, text=info)
    labelLevel.grid   (row=1,column=0)


    level4.geometry('400x400')
    level4.mainloop()