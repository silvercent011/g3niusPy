#TkInter
from tkinter import ttk
from func.login import *
from tkinter import *
from tkinter import messagebox
#Funcional
from functools import partial
#Sistema
import sys
import platform
import getpass
def cadastraAluno(chaves,usuarios):
    '''
    Menu para cadastro de alunos
    '''
    frameGeral = Tk()

    label1 = ttk.Label(frameGeral, text='Nome completo:')
    label1.grid(row=0,column=0)
    nomeCompleto = ttk.Entry(frameGeral)
    nomeCompleto.grid(row=0,column=1)

    label2 = ttk.Label(frameGeral, text='Turma:')
    label2.grid(row=2,column=0)
    turma = ttk.Combobox(frameGeral)
    turma.grid(row=2,column=1)

    label3 = ttk.Label(frameGeral, text='Turno:')
    label3.grid(row=4,column=0)
    turno = ttk.Combobox(frameGeral)
    turno.grid(row=4, column=1)

    label4 = ttk.Label(frameGeral, text='Ano:')
    label4.grid(row=6,column=0)
    ano = ttk.Entry(frameGeral)
    ano.grid(row=6, column=1)


    enviar = ttk.Button(frameGeral, width=30, text='Cadastrar')
    enviar.grid(row=13,column=0)

    #frameGeral.geometry('850x400')
    frameGeral.title('Cadastrar usuários')
    frameGeral.mainloop()

def ponte(nomeCompleto,cpf,senha,senhaC,codigo,chaves,usuarios):
    pass

def cadastro(nome,cpf,senha,senhaC,codigo,chaves,usuarios):
    pass