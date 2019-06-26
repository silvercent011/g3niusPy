from tkinter import ttk, messagebox, font
from func.login import *
from func.log import *
from func.gerenciaAluno import *
from func.gerenciaUser import *
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
arqUsers = './data/users.genius'

def pesquisaAluno(login,nivel,usuario,dictAlunos,janelaPai,janelaFechar, funcaoFechar,codigoJanela):
    janelaFechar.destroy()
    dictAlunos.clear()

    global dictUsers
    dictUsers = {}

    global infoUser
    infoUser = [login,nivel,usuario]

    carregaAlunosArquivo(arqAlunos,dictAlunos)
    carregaUsersArquivo(arqUsers,dictUsers)

    r = ttk.Style()
    r.configure('branco.TLabel',bcakground='white')

    s = ttk.Style()
    s.configure('branco.TFrame',background='white')

    t = ttk.Style()
    t.configure('branco.TLabelframe',font=('Segoe UI',12,'normal'),background='white',foreground='white')

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
    if codigoJanela == 1:
        texto = 'ALUNOS ENCONTRADOS NO BANCO DE DADOS'
    elif codigoJanela == 2:
        texto = 'USUÁRIOS ENCONTRADOS NO BANCO DE DADOS'
        
    labelBox = ttk.Labelframe(frameGeral,text=texto,width=largura2)
    labelBox['style'] = 'branco.TLabelframe'
    labelBox.grid(row=1,column=0,sticky=W+E)
    
    global boxAlunos
    boxAlunos = Listbox(labelBox,width=largura2)
    boxScroll = Scrollbar(labelBox,orient=VERTICAL,command=boxAlunos.yview)
    boxAlunos.configure(yscrollcommand=boxScroll.set)
    boxAlunos.grid(row=1,column=0,sticky=W+E)
    boxScroll.grid(row=1,column=0,sticky=E+S+N)
    if codigoJanela == 1:
        carregaAlunosBox(boxAlunos,dictAlunos)
        funcaoSuporte = carregaParaEdicao
    elif codigoJanela == 2:
        carregaUsersBox(boxAlunos,dictUsers)
        funcaoSuporte = carregaParaEdicao2
    
    boxAlunos.bind('<<ListboxSelect>>',funcaoSuporte)

    

    #Suporte1
    suporte1 = ttk.Label(frameGeral,text='')
    suporte1.grid(row=2,column=0,sticky=W+E)
    suporte1['style'] = 'branco.TLabel'

    if codigoJanela == 1:
        #Frame para botões de filtro
        filtros = ttk.Frame(frameGeral)
        filtros.grid(row=3,column=0,sticky=W+E)
        filtros['style'] = 'branco.TFrame'

        imageAlfab = ImageTk.PhotoImage(Image.open('./icons/30/AlphabeticalSorting30px.png'))
        btAlfab = ttk.Button(filtros,text='Filtrar por ordem alfabética',compound=TOP,image=imageAlfab,command=partial(organizaAlunosNome,boxAlunos,dictAlunos))
        btAlfab.grid(row=0,column=0,ipady=altura)
        btAlfab.image = imageAlfab

        imageTurma = ImageTk.PhotoImage(Image.open('./icons/30/Numeric30px.png'))
        btTurma = ttk.Button(filtros,text='Filtrar por Turma',compound=TOP,image=imageTurma,command=partial(organizaAlunosTurma,boxAlunos,dictAlunos))
        btTurma.grid(row=0,column=1,ipady=altura)
        btTurma.image = imageTurma

        imageChave = ImageTk.PhotoImage(Image.open('./icons/30/Access30px.png'))
        btChave = ttk.Button(filtros,text='Filtrar por chave',compound=TOP,image=imageChave,command=partial(organizaAlunosChave,boxAlunos,dictAlunos))
        btChave.grid(row=0,column=2,ipady=altura)
        btChave.image = imageChave
        
        imageAno = ImageTk.PhotoImage(Image.open('./icons/30/Calendar30px.png'))
        btFAno = ttk.Button(filtros,text='Filtrar por ano',compound=TOP,image=imageAno,command=partial(organizaAlunosAno,boxAlunos,dictAlunos))
        btFAno.grid(row=0,column=3,ipady=altura)
        btFAno.image = imageAno
        
        global campoBusca
        campoBusca = ttk.Entry(filtros,font=fonteTopo2)
        campoBusca.grid(row=0,column=4,columnspan=2,sticky=W+E)

        imagePesquisa = ImageTk.PhotoImage(Image.open('./icons/30/Calendar30px.png'))
        btPesquisa = ttk.Button(filtros,text='Buscar',compound=TOP,image=imagePesquisa,command=partial(buscaTexto,dictAlunos))
        btPesquisa.grid(row=0,column=6,ipady=altura)
        btPesquisa.image = imagePesquisa

    #Suporte2
    suporte2 = ttk.Label(frameGeral,text='')
    suporte2.grid(row=4,column=0,sticky=W+E)
    suporte2['style'] = 'branco.TLabel'

    #Label para edição de campos
    editLabel = ttk.Labelframe(frameGeral,text='MODIFICAR INFORMAÇÕES',width=largura2)
    editLabel['style'] = 'branco.TLabelframe'
    editLabel.grid(row=6,column=0,sticky=W)
    
    if codigoJanela == 1:
        #Frame contendo os campos para edição
        frameEdit = ttk.Frame(editLabel)
        frameEdit.grid(row=0,column=0,columnspan=9,sticky=W+E)
        frameEdit['style'] = 'branco.TLabel'

        #Nome
        nome = ttk.Label(frameEdit,text='NOME',font=fonteTopo3)
        nome.grid(row=0,column=0,sticky=W)
        nome['style'] = 'branco.TLabel'

        global inNome
        inNome = ttk.Entry(frameEdit, font=fonteTopo2)
        inNome.grid(row=1,column=0,columnspan=15,sticky=W+E)
        
        #Código
        codigo = ttk.Label(frameEdit,text='CÓDIGO',font=fonteTopo3)
        codigo.grid(row=2,column=0,sticky=W)
        codigo['style'] = 'branco.TLabel'

        global inCodigo
        inCodigo = ttk.Entry(frameEdit, font=fonteTopo2)
        inCodigo.grid(row=3,column=0,sticky=W+E)

        #MEIO1
        meio1 = ttk.Label(frameEdit,text='')
        meio1.grid(row=3,column=4)
        meio1['style'] = 'branco.TLabel'
        #Turno
        turno = ttk.Label(frameEdit,text='TURNO',font=fonteTopo3)
        turno.grid(row=2,column=5,sticky=W)
        turno['style'] = 'branco.TLabel'

        global inTurno
        inTurno = ttk.Combobox(frameEdit, font=fonteTopo2)
        #Implementar a leitura desses valores em arquivos
        inTurno['values'] = ('Selecionar','Manhã','Tarde','Noite','Integral', 'Semi-integral')
        inTurno.current(0)
        inTurno.grid(row=3,column=5,sticky=W+E)

        #MEIO2
        meio2 = ttk.Label(frameEdit,text='')
        meio2.grid(row=3,column=9)
        meio2['style'] = 'branco.TLabel'

        #Turma
        turma = ttk.Label(frameEdit,text='TURMA',font=fonteTopo3)
        turma.grid(row=2,column=10,sticky=W)
        turma['style'] = 'branco.TLabel'

        global inTurma
        inTurma = ttk.Combobox(frameEdit, font=fonteTopo2)
        #Implementar a leitura desses valores em arquivos
        inTurma['values'] = ('Selecionar','1°Ano','2°Ano','3°Ano','4°Ano', '5°Ano')
        inTurma.current(0)
        inTurma.grid(row=3,column=10,sticky=W+E)

        #Ano
        ano = ttk.Label(frameEdit,text='ANO',font=fonteTopo3)
        ano.grid(row=6,column=0,sticky=W)
        ano['style'] = 'branco.TLabel'

        global inAno
        inAno = ttk.Spinbox(frameEdit, font=fonteTopo2,from_=1950,to=2200)
        inAno.grid(row=7,column=0,sticky=W+E)
        '''
        #Status A/N
        status = ttk.Label(frameEdit,text='STATUS',font=fonteTopo3)
        status.grid(row=8,column=0,sticky=W)
        status['style'] = 'branco.TLabel'

        global inStatus
        inStatus = ttk.Combobox(frameEdit, font=fonteTopo2)
        inStatus.grid(row=9,column=0,sticky=W+E)
    '''
    elif codigoJanela == 2:
        #Frame contendo os campos para edição
        frameEdit = ttk.Frame(editLabel)
        frameEdit.grid(row=0,column=0,columnspan=9,sticky=W+E)
        frameEdit['style'] = 'branco.TLabel'

        #Nome
        nome = ttk.Label(frameEdit,text='NOME',font=fonteTopo3)
        nome.grid(row=0,column=0,sticky=W)
        nome['style'] = 'branco.TLabel'

        global inNomeUser
        inNomeUser = ttk.Entry(frameEdit, font=fonteTopo2)
        inNomeUser.grid(row=1,column=0,columnspan=15,sticky=W+E)
        
        #Código
        codigo = ttk.Label(frameEdit,text='CÓDIGO',font=fonteTopo3)
        codigo.grid(row=2,column=0,sticky=W)
        codigo['style'] = 'branco.TLabel'

        global inCpfUser
        inCpfUser = ttk.Entry(frameEdit, font=fonteTopo2)
        inCpfUser.grid(row=3,column=0,sticky=W+E)

        #MEIO1
        meio1 = ttk.Label(frameEdit,text='')
        meio1.grid(row=3,column=4)
        meio1['style'] = 'branco.TLabel'
        #Turno
        turno = ttk.Label(frameEdit,text='LEVEL',font=fonteTopo3)
        turno.grid(row=2,column=5,sticky=W)
        turno['style'] = 'branco.TLabel'

        global inLevel
        inLevel = ttk.Combobox(frameEdit, font=fonteTopo2)
        #Implementar a leitura desses valores em arquivos
        inLevel['values'] = ('Selecionar','3','4','6')
        inLevel.current(0)
        inLevel.grid(row=3,column=5,sticky=W+E)

        #MEIO2
        meio2 = ttk.Label(frameEdit,text='')
        meio2.grid(row=3,column=9)
        meio2['style'] = 'branco.TLabel'

    #Suporte3
    suporte3 = ttk.Label(frameGeral,text='')
    suporte3.grid(row=7,column=0,sticky=W+E)
    suporte3['style'] = 'branco.TLabel'

    #Frame para agrupar os botões 
    botoes = ttk.Frame(frameGeral)
    botoes.grid(row=8,column=0,sticky=W+S+N+E)
    botoes['style'] = 'branco.TFrame'
    if codigoJanela == 1:
        imagePrint = ImageTk.PhotoImage(Image.open('./icons/30/Print30px.png'))
        btImprimir = ttk.Button(botoes,text='Imprimir',width=largura,compound=TOP,image=imagePrint,command=partial(imprimeUnico,boxAlunos,dictAlunos,inCodigo))
        btImprimir.grid(row=0,column=0,ipady=altura)
        btImprimir.image = imagePrint
        
        imagePrintTudo = ImageTk.PhotoImage(Image.open('./icons/30/SendtoPrinter30px.png'))
        btImprimirTudo = ttk.Button(botoes,text='Imprimir Tudo',width=largura,compound=TOP,image=imagePrintTudo,command=partial(imprimeGeral,boxAlunos,dictAlunos))
        btImprimirTudo.grid(row=0,column=1,ipady=altura)
        btImprimirTudo.image = imagePrintTudo
    
    imageSalvar = ImageTk.PhotoImage(Image.open('./icons/30/Save30px.png'))
    if codigoJanela == 1:
        btSalvar = ttk.Button(botoes,text='Salvar',width=largura,compound=TOP,image=imageSalvar,command=partial(ponte,inCodigo,inNome,inTurma,inTurno,inAno,login,dictAlunos,1))
    elif codigoJanela == 2:    
        btSalvar = ttk.Button(botoes,text='Salvar',width=largura,compound=TOP,image=imageSalvar,command=partial(ponte2,inCpfUser,inNomeUser,inLevel,dictUsers,1))
    btSalvar.grid(row=0,column=2,ipady=altura)
    btSalvar.image = imageSalvar

    imageExcluir = ImageTk.PhotoImage(Image.open('./icons/30/TrashCan30px.png'))
    if codigoJanela == 1 :
        btExcluir = ttk.Button(botoes,text='Excluir',width=largura,compound=TOP,image=imageExcluir,command=partial(ponte,inCodigo,inNome,inTurma,inTurno,inAno,login,dictAlunos,2))
    elif codigoJanela == 2:
        btExcluir = ttk.Button(botoes,text='Excluir',width=largura,compound=TOP,image=imageExcluir,command=partial(ponte2,inCpfUser,inNomeUser,inLevel,dictUsers,2))
    btExcluir.grid(row=0,column=3,ipady=altura)
    btExcluir.image = imageExcluir

    imageVoltar = ImageTk.PhotoImage(Image.open('./icons/30/Cancel30px.png'))
    btVoltar = ttk.Button(botoes,text='Voltar',width=largura,compound=TOP,image=imageVoltar,command=partial(funcaoFechar,login,usuario,nivel,dictAlunos,janelaPai,frameGeral))
    btVoltar.grid(row=0,column=4,ipady=altura)
    btVoltar.image = imageVoltar

    #Suporte4
    suporte4 = ttk.Label(frameGeral,text='')
    suporte4.grid(row=9,column=0,sticky=W+E)
    suporte4['style'] = 'branco.TLabel'

def buscaTexto(dictAlunos):
    string = campoBusca.get()
    encontraSubstring(boxAlunos,dictAlunos,string)  
def carregaParaEdicao(evt):
    '''
    Carrega valores selecionados no listbox para a função colocaFrame
    '''
    try:
        wid = evt.widget
        valor1 = wid.get(wid.curselection()[0])
        valor2 = valor1.split(' - ')

        limpa()

        alunos = {}
        carregaAlunosArquivo(arqAlunos,alunos)
        try:
            codAluno = valor2[0]
            infoCompleta = alunos[codAluno]
        except:
            codAluno = valor2[-1]
            infoCompleta = alunos[codAluno]

        colocaFrame(infoCompleta)
    except:
        pass



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

def limpa2():
    inCpfUser.configure(state=NORMAL)
    inCpfUser.delete(0,'end')

    inNomeUser.configure(state=NORMAL)
    inNomeUser.delete(0,'end')

    inLevel.delete(0,'end')

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

    if codigo == '':
        messagebox.showerror('Ops!','Aluno não selecionado!')
    else:
        if opcao == 1:
            salvarModificacoesAlunos(codigo,nome,turma,turno,ano,cpf,dictAlunos)
            acao = 'MODIFICOU INFORMAÇÕES DO ALUNO(A) ('+ codigo +')' 
            messagebox.showinfo('','As modificações foram salvas')
            colocaLog(infoUser[0],infoUser[2],infoUser[1],acao)
        elif opcao == 2:
            excluirAluno(codigo,nome,turma,turno,ano,cpf,dictAlunos)
            acao = 'EXCLUIU ALUNO(A) ('+ codigo +')' 
            messagebox.showinfo('','Aluno excluído do sistema.')
            colocaLog(infoUser[0],infoUser[2],infoUser[1],acao)
            limpa()
        boxAlunos.delete(0,END)
        carregaAlunosBox(boxAlunos,dictAlunos)

def ponte2(inCpfUser,inNomeUser,inLevel,dictUsers,opcao):
    cpf = inCpfUser.get()
    cpf = cpf.upper()

    nome = inNomeUser.get()
    nome = nome.upper()

    level = inLevel.get()
    level = level.upper()

    if cpf == '':
        messagebox.showerror('ops!','Usuário não selecionado!')
    else:
        if opcao == 1:
            salvarModificacoesUser(cpf,nome,level,dictUsers)
            acao = 'MODIFICOU INFORMAÇÕES DO USUÁRIO(A) ('+ cpf +')' 
            messagebox.showinfo('','As modificações foram salvas')
            colocaLog(infoUser[0],infoUser[2],infoUser[1],acao)
        elif opcao == 2:
            excluirUser(cpf,nome,level,dictUsers)
            acao = 'EXCLUIU USUÁRIO(A) ('+ cpf +')' 
            messagebox.showinfo('','Usuário excluído do sistema!')
            colocaLog(infoUser[0],infoUser[2],infoUser[1],acao)
            limpa2()
        boxAlunos.delete(0,END)
        carregaUsersBox(boxAlunos,dictUsers)

def carregaParaEdicao2(evt):
    '''
    Carrega valores selecionados no listbox para a função colocaFrame
    '''
    try:
        wid = evt.widget
        valor1 = wid.get(wid.curselection()[0])
        valor2 = valor1.split(' - ')

        limpa2()

        users = {}
        carregaUsersArquivo(arqUsers,users)
        try:
            codUser = valor2[0]
            infoCompleta = users[codUser]
        except:
            codUser = valor2[-1]
            infoCompleta = users[codUser]

        colocaFrame2(infoCompleta)
    except:
        pass

def colocaFrame2(info):
    '''
    Coloca as informações recebidas no frame para modificação (Usuários)
    '''
    inNomeUser.delete(0,'end')
    inNomeUser.insert(0,info[2])
    inNomeUser.configure(state='readonly')

    inCpfUser.delete(0,'end')
    inCpfUser.insert(0,info[0])
    inCpfUser.configure(state='readonly')

    inLevel.delete(0,'end')
    inLevel.insert(0,info[4])

    #inStatus.delete(0,'end')
    #inStatus.insert(0,info[6])