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

def pesquisaAluno(login,nivel,usuario,dictAlunos,janelaPai,janelaFechar, funcaoFechar):
    janelaFechar.destroy()
    dictAlunos.clear()

    carregaAlunosArquivo(arqAlunos,dictAlunos)

    r = ttk.Style()
    r.configure('branco.TLabel',bcakground='white')

    s = ttk.Style()
    s.configure('branco.TFrame',background='white')

    version = 'Genius (LITE) - 7.0.1'
    altura       = 5
    largura      = 20
    largura2     = 110
    largura3	 = 17
    espacamento1 = 50
    espacamento2 = 20

    frameGeral = ttk.Frame(janelaPai,width=largura2)
    frameGeral.grid(row=0,column=0,sticky=W+E)
    frameGeral['style'] = 'branco.TFrame'
    frameGeral['padding'] = (espacamento1,espacamento2)

    #Fontes e estilos
    fonteTo5 = font.Font(family='Segoe Ui', size=18, weight='bold')
    fonteTopo2 = font.Font(family='Segoe Ui', size=14, weight='normal')
    fonteTopo3 = font.Font(family='Segoe Ui', size=12, weight='normal')
    fonteTopo4 = font.Font(family='Segoe Ui', size=24, weight='bold')
    fonteTopo5 = font.Font(family='Segoe Ui', size=35, weight='bold')
    fonteTopo6 = font.Font(family='Segoe Ui', size=14, weight='bold')
    
    #Box Alunos
    labelBox = ttk.Labelframe(frameGeral,text='ALUNOS ENCONTRADOS NO BANCO DE DADOS',width=largura2)
    labelBox.grid(row=1,column=0,sticky=W+E)
    
    global boxAlunos
    boxAlunos = Listbox(labelBox,width=largura2)
    boxScroll = Scrollbar(labelBox,orient=VERTICAL,command=boxAlunos.yview)
    boxAlunos.configure(yscrollcommand=boxScroll.set)
    boxAlunos.grid(row=1,column=0,sticky=W+E)
    boxScroll.grid(row=1,column=0,sticky=E+S+N)
    carregaAlunosBox(boxAlunos,dictAlunos)

    boxAlunos.bind('<<ListboxSelect>>',carregaParaEdicao)

    #Suporte1
    suporte1 = ttk.Label(frameGeral,text='')
    suporte1.grid(row=2,column=0,sticky=W+E)

    #Frame para botões de filtro
    filtros = ttk.Frame(frameGeral)
    filtros.grid(row=3,column=0,sticky=W+E)

    btAlfab = ttk.Button(filtros,text='Filtrar por Nome')
    btAlfab.grid(row=0,column=0)

    btTurma = ttk.Button(filtros,text='Filtrar por Turma')
    btTurma.grid(row=0,column=1)

    #Suporte2
    suporte2 = ttk.Label(frameGeral,text='')
    suporte2.grid(row=4,column=0,sticky=W+E)

    #Label para edição de campos
    editLabel = ttk.Labelframe(frameGeral,text='MODIFICAR INFORMAÇÕES',width=largura2)
    editLabel.grid(row=6,column=0,sticky=W)

    #Frame contendo os campos para edição
    frameEdit = ttk.Frame(editLabel)
    frameEdit.grid(row=0,column=0,columnspan=9,sticky=W+E)

    #Nome
    nome = ttk.Label(frameEdit,text='NOME',font=fonteTopo3)
    nome.grid(row=0,column=0,sticky=W)

    global inNome
    inNome = ttk.Entry(frameEdit, font=fonteTopo2)
    inNome.grid(row=1,column=0,columnspan=15,sticky=W+E)
    
    #Código
    codigo = ttk.Label(frameEdit,text='CÓDIGO',font=fonteTopo3)
    codigo.grid(row=2,column=0,sticky=W)

    global inCodigo
    inCodigo = ttk.Entry(frameEdit, font=fonteTopo2)
    inCodigo.grid(row=3,column=0,sticky=W+E)

    #Turno
    turno = ttk.Label(frameEdit,text='TURNO',font=fonteTopo3)
    turno.grid(row=2,column=5,sticky=W)

    global inTurno
    inTurno = ttk.Combobox(frameEdit, font=fonteTopo2)
    #Implementar a leitura desses valores em arquivos
    inTurno['values'] = ('Selecionar','Manhã','Tarde','Noite','Integral', 'Semi-integral')
    inTurno.current(0)
    inTurno.grid(row=3,column=5,sticky=W+E)

    #Turma
    turma = ttk.Label(frameEdit,text='TURMA',font=fonteTopo3)
    turma.grid(row=2,column=10,sticky=W)

    global inTurma
    inTurma = ttk.Combobox(frameEdit, font=fonteTopo2)
    #Implementar a leitura desses valores em arquivos
    inTurma['values'] = ('Selecionar','1°Ano','2°Ano','3°Ano','4°Ano', '5°Ano')
    inTurma.current(0)
    inTurma.grid(row=3,column=10,sticky=W+E)

    #Ano
    ano = ttk.Label(frameEdit,text='ANO',font=fonteTopo3)
    ano.grid(row=6,column=0,sticky=W)

    global inAno
    inAno = ttk.Spinbox(frameEdit, font=fonteTopo2)
    inAno.grid(row=7,column=0,sticky=W+E)
    '''
    #Status A/N
    status = ttk.Label(frameEdit,text='STATUS',font=fonteTopo3)
    status.grid(row=8,column=0,sticky=W)

    global inStatus
    inStatus = ttk.Combobox(frameEdit, font=fonteTopo2)
    inStatus.grid(row=9,column=0,sticky=W+E)
    '''
    #Suporte3
    suporte3 = ttk.Label(frameGeral,text='')
    suporte3.grid(row=7,column=0,sticky=W+E)

    #Frame para agrupar os botões 
    botoes = ttk.Frame(frameGeral)
    botoes.grid(row=8,column=0,sticky=W+S+N+E)

    btImprimir = ttk.Button(botoes,text='Imprimir')
    btImprimir.grid(row=0,column=0)
    
    btSalvar = ttk.Button(botoes,text='Salvar',command=partial(ponte,inCodigo,inNome,inTurma,inTurno,inAno,login,dictAlunos,1))
    btSalvar.grid(row=0,column=1)

    btExcluir = ttk.Button(botoes,text='Excluir',command=partial(ponte,inCodigo,inNome,inTurma,inTurno,inAno,login,dictAlunos,2))
    btExcluir.grid(row=0,column=2)

    btVoltar = ttk.Button(botoes,text='Voltar',command=partial(funcaoFechar,login,usuario,nivel,dictAlunos,janelaPai,frameGeral))
    btVoltar.grid(row=0,column=3)

    #Suporte4
    suporte4 = ttk.Label(frameGeral,text='')
    suporte4.grid(row=9,column=0,sticky=W+E)
    
def carregaParaEdicao(evt):
    '''
    Carrega valores selecionados no listbox para a função colocaFrame
    '''
    limpa()
    wid = evt.widget
    valor1 = wid.get(wid.curselection()[0])
    valor2 = valor1.split(' - ')

    alunos = {}
    carregaAlunosArquivo(arqAlunos,alunos)
    codAluno = valor2[0]
    infoCompleta = alunos[codAluno]

    colocaFrame(infoCompleta)

def colocaFrame(info):
    '''
    Coloca as informações recebidas no frame para modificação
    '''
    inCodigo.delete(0,'end')
    inCodigo.insert(0,info[0])
    inCodigo.configure(state='readonly')

    inNome.delete(0,'end')
    inNome.insert(0,info[1])

    inTurma.delete(0,'end')
    inTurma.insert(0,info[2])

    inTurno.delete(0,'end')
    inTurno.insert(0,info[3])

    inAno.delete(0,'end')
    inAno.insert(0,info[4])

    #inStatus.delete(0,'end')
    #inStatus.insert(0,info[6])
def limpa():
    inCodigo.configure(state=NORMAL)
    inCodigo.delete(0,'end')

    inNome.delete(0,'end')

    inTurma.delete(0,'end')

    inTurno.delete(0,'end')

    inAno.delete(0,'end')

    #inStatus.delete(0,'end')
    #inStatus.insert(0,info[6])

def ponte(inCodigo,inNome,inTurma,inTurno,inAno,cpf,dictAlunos,opcao):

    codigo = inCodigo.get()
    codigo = codigo.upper()

    nome = inNome.get()
    nome = nome.upper()

    turma = inTurma.get()
    turma = turma.upper()

    turno = inTurno.get()
    turno = turno.upper()

    ano = inAno.get()
    ano = ano.upper()

    if opcao == 1:
        salvarModificacoesAlunos(codigo,nome,turma,turno,ano,cpf,dictAlunos)
    elif opcao == 2:
        excluirAluno(codigo,nome,turma,turno,ano,cpf,dictAlunos)
        limpa()
    boxAlunos.delete(0,END)
    carregaAlunosBox(boxAlunos,dictAlunos)
