from tkinter import ttk
from func.login import *
from tkinter import *
import sys
import platform
import getpass

def menuLevel6(usuario,level):
    '''
    Menu para usuários nível 6
    '''
    info = 'Usuário nível ' + str(level)
    level6 = Tk()

    cadastra_aluno = ttk.Button(level6,width=20,text='Cadastrar Alunos')
    cadastra_aluno.grid(row=4,column=1)
    gerar_codigo = ttk.Button(level6,width=20,text='Gerar Cógidos')
    gerar_codigo.grid(row=5,column=1)
    exibir_usuarios = ttk.Button(level6,width=20,text='Gerenciar Usuários')
    exibir_usuarios.grid(row=6,column=1)
    exibir_log = ttk.Button(level6,width=20,text='Log de Informações')
    exibir_log.grid(row=7,column=1)
    sair = ttk.Button(level6,width=20,text='Sair')
    sair.grid(row=8,column=1)

    labelUser = Label (level6, text=usuario)
    labelUser.grid    (row=0, column=0)
    labelLevel = Label(level6, text=info)
    labelLevel.grid   (row=1,column=0)


    level6.geometry('400x400')
    level6.mainloop()