#Funcional
from functools import partial
#TkInter
from tkinter import ttk
from tkinter import *
#Funções
from func.login import *
from func.log import *
#Sistema Operacional
import sys
import platform
import getpass

def btSair(loginEntrada,usuario,nivel):
	
    colocaLog(loginEntrada,usuario,nivel,'SAIU DO SISTEMA')
    exit()


def menuLevel3(login,usuario,level):
    '''
    Menu para usuários nível 6
    '''
    info = 'Usuário nível ' + str(level)
    level3 = Tk()
    #Cadastrar Alunos
    cadastra_aluno = ttk.Button(level3,width=20,text='Cadastrar Alunos')
    cadastra_aluno.grid(row=4,column=1)
    #Pesquisar Alunos
    pesquisa_aluno = ttk.Button(level3,width=20,text='Pesquisar Alunos')
    pesquisa_aluno.grid(row=5,column=1)
    #Lançar Notas 
    lancar_notas = ttk.Button(level3,width=20,text='Lançar Notas')
    lancar_notas.grid(row=6,column=1)
    #Material Impresso
    material_impresso = ttk.Button(level3,width=20,text='Material Impresso')
    material_impresso.grid(row=7,column=1)
    #Log de Informações
    exibir_log = ttk.Button(level3,width=20,text='Log de Informações')
    exibir_log.state(['disabled']) 
    exibir_log.grid(row=8,column=1)
    #Sair
    sair = ttk.Button(level3,width=20,text='Sair',command=partial(btSair,login,usuario,level))
    sair.grid(row=9,column=1)

    labelUser = Label (level3, text=usuario)
    labelUser.grid    (row=0, column=0)
    labelLevel = Label(level3, text=info)
    labelLevel.grid   (row=1,column=0)


    level3.geometry('400x400')
    level3.mainloop()