#TkInter
from tkinter import ttk, messagebox, font
from func.login import *
from func.log import *
from func.gerenciaAluno import *
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
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

    r = ttk.Style()
    r.configure('branco.TLabel',bcakground='white')

    s = ttk.Style()
    s.configure('branco.TFrame',background='white')

    version = 'Genius (LITE) - 7.0.1'
    altura       = 10
    largura      = 20
    largura2     = 62
    largura3	 = 17
    espacamento1 = 50
    espacamento2 = 20

    frameGeral = ttk.Frame(janelaPai)
    frameGeral.grid(row=0, column=0)
    frameGeral['style'] = 'branco.TFrame'
    frameGeral['padding'] = (espacamento1,espacamento2)

    #Fontes e estilos
    fonteTo5 = font.Font(family='Segoe Ui', size=18, weight='bold')
    fonteTopo2 = font.Font(family='Segoe Ui', size=14, weight='normal')
    fonteTopo3 = font.Font(family='Segoe Ui', size=12, weight='normal')
    fonteTopo4 = font.Font(family='Segoe Ui', size=24, weight='bold')
    fonteTopo5 = font.Font(family='Segoe Ui', size=35, weight='bold')
    fonteTopo6 = font.Font(family='Segoe Ui', size=14, weight='bold')

    label1 = ttk.Label(frameGeral, text='NOME COMPLETO:',font=fonteTopo2)
    label1.grid(row=0,column=4,sticky=W)
    nomeCompleto = ttk.Entry(frameGeral,font=fonteTopo3)
    nomeCompleto.grid(row=1,column=4,columnspan=15,sticky=W+E)

    label2 = ttk.Label(frameGeral, text='TURMA:',font=fonteTopo2)
    label2.grid(row=2,column=4,sticky=W)
    turma = StringVar()
    selecTurma = ttk.Combobox(frameGeral,textvariable=turma,font=fonteTopo3)
    #Implementar a leitura desses valores em arquivos
    selecTurma['values'] = ('Selecionar','1°Ano','2°Ano','3°Ano','4°Ano', '5°Ano')
    selecTurma.current(0)
    selecTurma.grid(row=3,column=4,sticky=W+E)

    suporte1 = ttk.Label(frameGeral,text='')
    suporte1.grid(row=3,column=5)

    label3 = ttk.Label(frameGeral, text='TURNO:',font=fonteTopo2)
    label3.grid(row=2,column=6,sticky=W)
    turno = StringVar()
    selecTurno = ttk.Combobox(frameGeral, textvariable=turno,font=fonteTopo3)
    #Implementar a leitura desses valores em arquivos
    selecTurno['values'] = ('Selecionar','Manhã','Tarde','Noite','Integral', 'Semi-integral')
    selecTurno.current(0)
    selecTurno.grid(row=3, column=6,sticky=W+E)

    suporte2 = ttk.Label(frameGeral,text='')
    suporte2.grid(row=3,column=7)

    label4 = ttk.Label(frameGeral, text='ANO:',font=fonteTopo2)
    label4.grid(row=2,column=8,sticky=W)
    ano = ttk.Spinbox(frameGeral,font=fonteTopo3,from_=1950,to=2200)
    ano.grid(row=3, column=8,sticky=W+E)

    suporte3 = ttk.Label(frameGeral,text='',font=fonteTopo3)
    suporte3.grid(row=4,column=4,columnspan=15,sticky=W+E)

    suporte4 = ttk.Label(frameGeral,text='')
    suporte4.grid(row=5,column=4)



    imagemEnviar = ImageTk.PhotoImage(Image.open('./icons/30/Approval30px.png'))
    enviar = ttk.Button(frameGeral, width=30, text='Cadastrar',compound=TOP,image=imagemEnviar,command=partial(ponte,nomeCompleto,usuario,login,nivel,selecTurma,selecTurno,ano,dictAlunos,suporte3))
    enviar.image = imagemEnviar
    enviar.grid(row=7,column=4,columnspan=4,sticky=W+E)

    imagemVoltar = ImageTk.PhotoImage(Image.open('./icons/30/Cancel30px.png'))
    voltar = ttk.Button(frameGeral,width=30,text='Voltar',compound=TOP,image=imagemVoltar,command=partial(funcaoFechar,login,usuario,nivel,dictAlunos,janelaPai,frameGeral))
    voltar.image = imagemVoltar
    voltar.grid(row=7, column=8,columnspan=4,sticky=W+E)

    label1['style']   = 'branco.TLabel'
    label2['style']   = 'branco.TLabel'
    label3['style']   = 'branco.TLabel'
    label4['style']   = 'branco.TLabel'
    suporte1['style'] = 'branco.TLabel'
    suporte2['style'] = 'branco.TLabel'
    suporte3['style'] = 'branco.TLabel'
    suporte4['style'] = 'branco.TLabel'

    janelaPai.title('Cadastrar Alunos')

def ponte(nomeAluno,nome,cpf,nivel,turma,turno,ano,dictAlunos,status):
    nomeAluno2 = nomeAluno.get()
    nomeAluno2 = nomeAluno2.upper()
    
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

    if nomeAluno2 == '':
        messagebox.showerror('Ops!','O nome do aluno não foi informado!')
    elif turma2 == '' or turma2 == 'SELECIONAR': 
        messagebox.showerror('Ops!','A turma não foi selecionada.')
    elif turno2 == '' or turno2 == 'SELECIONAR':
        messagebox.showerror('Ops!','O turno não foi selecionado.')
    elif ano2 == '':
        messagebox.showerror('Ops!','O ano não foi informado.')
    else:
        achou = False
        for x in dictAlunos:
            value = dictAlunos[x][1]
            value2 = dictAlunos[x][2]
            if nomeAluno2 == value and turma2 == value2:
                achou = True
                
        if achou == True:
            if messagebox.askyesno('Ops!', 'O nome informado já existe nessa turma, deseja cadastrar mesmo assim?'):
                cadastro(nomeAluno2,nome2,cpf2,codigoAluno2,nivel2,turma2,turno2,ano2,dictAlunos,status)
        else:
            nomeAluno.delete(0,END)
            cadastro(nomeAluno2,nome2,cpf2,codigoAluno2,nivel2,turma2,turno2,ano2,dictAlunos,status)

def cadastro(nomeAluno,nome,cpf,codigoAluno,nivel,turma,turno,ano,dictAlunos,status): 
    cadastrarAlunosArquivo(nomeAluno,str(codigoAluno),turma,turno,ano,cpf,dictAlunos)
    acao = 'CADASTROU ALUNO (' + str(codigoAluno) + ')'
    status['text'] = nomeAluno + '\n CADASTRADO COM SUCESSO. COD:' + str(codigoAluno)
    colocaLog(cpf,nome,nivel,acao)