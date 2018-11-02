#TkInter
from tkinter import ttk
from func.login import *
from func.log import *
from func.gerenciaAluno import *
from tkinter import *
from tkinter import messagebox
#Funcional
from functools import partial
#Sistema
import sys
import platform
import getpass
from datetime import *

arqAlunos = './data/database.genius'

def cadastraAluno(login,nivel,usuario,dictAlunos):
    '''
    Menu para cadastro de alunos
    '''
    carregaAlunosArquivo(arqAlunos,dictAlunos)

    s = ttk.Style()
    s.configure('branco.TFrame',background='white')
    espacamento1 = 50
    espacamento2 = 20

    janela = Toplevel()
    janela.resizable(FALSE,FALSE)
    frameGeral = ttk.Frame(janela)
    frameGeral.grid(row=0, column=0)
    frameGeral['style'] = 'branco.TFrame'
    frameGeral['padding'] = (espacamento1,espacamento2)

    label1 = ttk.Label(frameGeral, text='Nome completo:')
    label1.grid(row=0,column=4)
    nomeCompleto = ttk.Entry(frameGeral)
    nomeCompleto.grid(row=0,column=5)

    label2 = ttk.Label(frameGeral, text='Turma:')
    label2.grid(row=2,column=4)
    turma = ttk.Combobox(frameGeral)
    turma.grid(row=2,column=5)

    label3 = ttk.Label(frameGeral, text='Turno:')
    label3.grid(row=4,column=4)
    turno = ttk.Combobox(frameGeral)
    turno.grid(row=4, column=5)

    label4 = ttk.Label(frameGeral, text='Ano:')
    label4.grid(row=6,column=4)
    ano = ttk.Entry(frameGeral)
    ano.grid(row=6, column=5)



    enviar = ttk.Button(frameGeral, width=30, text='Cadastrar',command=partial(ponte,nomeCompleto,usuario,login,nivel,turma,turno,ano,dictAlunos))
    enviar.grid(row=13,column=9)

    #frameGeral.geometry('850x400')
    frameGeral.mainloop()
    janela.title('Cadastrar usuários')

def ponte(nomeAluno,nome,cpf,nivel,turma,turno,ano,dictAlunos):
    nomeAluno2 = nomeAluno.get()
    nomeAluno2 = nomeAluno2.upper()
    nomeAluno.delete(0,END)
    
    turma2 = turma.get()
    turma2 = turma2.upper()
    
    turno2 = turno.get()
    turno2 = turno2.upper()
    
    ano2 = ano.get()
    ano2 = ano2.upper()

    nome2 = nome
    cpf2 = cpf

    codigoAluno1 = datetime.now()
    codigoAluno2 = str(codigoAluno1.strftime('%d%m%y%H%M%S'))

    nivel2 = nivel

    cadastro(nomeAluno2,nome2,cpf2,codigoAluno2,nivel2,turma2,turno2,ano2,dictAlunos)


def cadastro(nomeAluno,nome,cpf,codigoAluno,nivel,turma,turno,ano,dictAlunos):

    cadastrarAlunosArquivo(nomeAluno,str(codigoAluno),turma,turno,ano,cpf,dictAlunos)
    acao = 'CADASTROU ALUNO (' + str(codigoAluno) + ')'
    colocaLog(cpf,nome,nivel,acao)

