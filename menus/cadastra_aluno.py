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

def cadastraAluno(login,nivel,usuario,dictAlunos,janelaPai,janelaFechar, funcaoFechar):
    '''
    Menu para cadastro de alunos
    '''
    janelaFechar.destroy()
    carregaAlunosArquivo(arqAlunos,dictAlunos)

    s = ttk.Style()
    s.configure('branco.TFrame',background='white')
    espacamento1 = 50
    espacamento2 = 20

    frameGeral = ttk.Frame(janelaPai)
    frameGeral.grid(row=0, column=0)
    frameGeral['style'] = 'branco.TFrame'
    frameGeral['padding'] = (espacamento1,espacamento2)

    label1 = ttk.Label(frameGeral, text='Nome completo:')
    label1.grid(row=0,column=4)
    nomeCompleto = ttk.Entry(frameGeral)
    nomeCompleto.grid(row=0,column=5)

    label2 = ttk.Label(frameGeral, text='Turma:')
    label2.grid(row=2,column=4)
    turma = StringVar()
    selecTurma = ttk.Combobox(frameGeral,textvariable=turma)
    #Implementar a leitura desses valores em arquivos
    selecTurma['values'] = ('1°Ano','2°Ano','3°Ano','4°Ano', '5°Ano')
    selecTurma.grid(row=2,column=5)

    label3 = ttk.Label(frameGeral, text='Turno:')
    label3.grid(row=4,column=4)
    turno = StringVar()
    selecTurno = ttk.Combobox(frameGeral, textvariable=turno)
    #Implementar a leitura desses valores em arquivos
    selecTurno['values'] = ('Manhã','Tarde','Noite','Integral', 'Semi-integral')
    selecTurno.grid(row=4, column=5)

    label4 = ttk.Label(frameGeral, text='Ano:')
    label4.grid(row=6,column=4)
    ano = ttk.Entry(frameGeral)
    ano.grid(row=6, column=5)

    enviar = ttk.Button(frameGeral, width=30, text='Cadastrar',command=partial(ponte,nomeCompleto,usuario,login,nivel,selecTurma,selecTurno,ano,dictAlunos))
    enviar.grid(row=13,column=4)

    voltar = ttk.Button(frameGeral,width=30,text='Voltar',command=partial(funcaoFechar,login,usuario,nivel,dictAlunos,janelaPai,frameGeral))
    voltar.grid(row=13, column=5)
    #frameGeral.geometry('850x400')
    janelaPai.title('Cadastrar Alunos')

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
    codigoAluno2 = str(codigoAluno1.strftime('%y%m%d%H%M%S'))
    nivel2 = nivel

    achou = False
    for x in dictAlunos:
        value = dictAlunos[x][1]
        value2 = dictAlunos[x][2]
        if nomeAluno2 == value and turma2 == value2:
            achou = True
            
    if achou == True:
        if messagebox.askyesno('Ops!', 'O nome informado já existe nessa turma, deseja cadastrar mesmo assim?'):
            cadastro(nomeAluno2,nome2,cpf2,codigoAluno2,nivel2,turma2,turno2,ano2,dictAlunos)
    else:
        cadastro(nomeAluno2,nome2,cpf2,codigoAluno2,nivel2,turma2,turno2,ano2,dictAlunos)


def cadastro(nomeAluno,nome,cpf,codigoAluno,nivel,turma,turno,ano,dictAlunos):

    cadastrarAlunosArquivo(nomeAluno,str(codigoAluno),turma,turno,ano,cpf,dictAlunos)
    acao = 'CADASTROU ALUNO (' + str(codigoAluno) + ')'
    colocaLog(cpf,nome,nivel,acao)

#dictAlunos = {}
#cadastraAluno('00000000000',6,'TESTE',dictAlunos)