#Funcional
from functools import partial
#Funções
from func.login import *
from func.log import *
from datetime import *
from menus.inicio_level6_func import *
from menus.cadastra_aluno import *
#TkInter
from tkinter import ttk
from tkinter import font
from tkinter import *
from PIL import ImageTk, Image
#Sistema
import sys
import platform
import getpass

def menuLevel(login,usuario,level,dictAlunos,janelaPai):
    '''
    Menu para usuários de diferentes níveis
    '''
    version = 'Genius (LITE) - 7.0.1'
    info        = 'Usuário nível ' + str(level)
    altura      = ''
    largura     = 30
    largura2     = 62
    espacamento1 = 50
    espacamento2 = 20
    #Style
    s = ttk.Style()
    s.configure('branco.TFrame',background='white')
    #Frame
    janela = ttk.Frame(janelaPai)
    janela.pack()
    level6 = ttk.Frame(janela)
    level6.grid(row=0,column=0)
    level6['style'] = 'branco.TFrame'
    level6['padding'] = (espacamento1,espacamento2)
    #Informações Usuário e logo
    fonteTopo = font.Font(family='Segoe Ui', size=18, weight='bold')
    fonteTopo2 = font.Font(family='Segoe Ui', size=14, weight='normal')
    fonteTopo3 = font.Font(family='Segoe Ui', size=12, weight='normal')
    fonteTopo4 = font.Font(family='Segoe Ui', size=24, weight='normal')

    imagemLogo = ImageTk.PhotoImage(Image.open('./icons/logoSmall2.png'))
    logo = Label(level6,text='GENIUS',image=imagemLogo)
    logo.image = imagemLogo
    logo.grid(row=0, column=0,columnspan=2,rowspan=2,sticky=W)
    logo['bg'] = 'white'

    labelUser = Label (level6, text=usuario, font=fonteTopo)
    labelUser.grid    (row=0, column=3,columnspan=2,sticky=E+S)
    labelUser['bg'] = 'white'
    labelLevel = Label(level6, text=info, font=fonteTopo2)
    labelLevel.grid   (row=1,column=3,columnspan=2,sticky=E+N)
    labelLevel['bg'] = 'white'
    #Cadastrar Alunos
    imagemCadastro = ImageTk.PhotoImage(Image.open('./icons/account80.png'))
    cadastra_aluno = ttk.Button(level6,width=largura,compound=TOP,text='Cadastrar Alunos',image=imagemCadastro,command=partial(cadastraAluno,login,level,usuario,dictAlunos,janelaPai,janela,btVoltarCadastroA))
    cadastra_aluno.image = imagemCadastro
    #cadastra_aluno.bind("<Button-1>",)
    cadastra_aluno.grid(row=4,column=0)
    #Pesquisar Alunos
    imagemPesquisa = ImageTk.PhotoImage(Image.open('./icons/search80.png'))
    pesquisa_aluno = ttk.Button(level6,width=largura,compound=TOP,text='Pesquisar Alunos',image=imagemPesquisa)
    pesquisa_aluno.image = imagemPesquisa
    pesquisa_aluno.grid(row=4,column=1)
    #Material Impresso
    imagemImpresso = ImageTk.PhotoImage(Image.open('./icons/exam80.png'))
    material_impresso = ttk.Button(level6,width=largura,compound=TOP,text='Material Impresso',image=imagemImpresso, command=partial(materialImpresso,login,usuario,level))
    material_impresso.image = imagemImpresso
    material_impresso.grid(row=4,column=2)
    #Gerar Códigos/Lançar Notas/Gerenciar Horários
    if str(level) == '3':
        imagemNotas = ImageTk.PhotoImage(Image.open('./icons/ReportCard80.png'))
        lancar_notas = ttk.Button(level6,width=largura,compound=TOP,text='Lançar Notas',image=imagemNotas,command=partial(lancaNotas,login,usuario,level))
        lancar_notas.image = imagemNotas
        lancar_notas.grid(row=4,column=3,sticky=W)
    elif str(level) == '4':
        imagemHorarios = ImageTk.PhotoImage(Image.open('./icons/WeekView80.png'))
        gerenc_horarios = ttk.Button(level6,width=largura,compound=TOP,text='Gerenciar Horários',image=imagemHorarios,command=partial(gerenciarHorarios,login,usuario,level))
        gerenc_horarios.image = imagemHorarios
        gerenc_horarios.grid(row=4,column=3,sticky=W)
    elif str(level) == '6':
        imagemCodigos = ImageTk.PhotoImage(Image.open('./icons/newDocument80.png'))
        gerar_codigo = ttk.Button(level6,width=largura,compound=TOP,text='Gerar Cógidos',image=imagemCodigos)
        gerar_codigo.image = imagemCodigos
        gerar_codigo.grid(row=4,column=3,sticky=W)
    #Gerenciar usuários/Frequencia/Avisos
    if str(level) == '3':
        imagemFrequencia = ImageTk.PhotoImage(Image.open('./icons/datasheetfilled80.png'))
        frequencia = ttk.Button(level6,width=largura,compound=TOP,text='Frequência',image=imagemFrequencia,command=partial(frequenciaAlunos,login,usuario,level))
        frequencia.image = imagemFrequencia
        frequencia.grid(row=5,column=0)
    elif str(level) == '4':
        imagemAvisos = ImageTk.PhotoImage(Image.open('./icons/Alert80.png'))
        avisos = ttk.Button(level6,width=largura,compound=TOP,text='Avisos',image=imagemAvisos,command=partial(avisosGer,login,usuario,level))
        avisos.image = imagemAvisos
        avisos.grid(row=5,column=0)
    elif str(level) == '6':
        imagemUsuarios = ImageTk.PhotoImage(Image.open('./icons/gruposDeUsuários80.png'))
        exibir_usuarios = ttk.Button(level6,width=largura,compound=TOP,text='Gerenciar Usuários',image=imagemUsuarios,command=partial(gerUsers,login,usuario,level))
        exibir_usuarios.image = imagemUsuarios
        exibir_usuarios.grid(row=5,column=0)
    #Log de Informações
    imagemLog = ImageTk.PhotoImage(Image.open('./icons/overview80.png'))
    exibir_log = ttk.Button(level6,width=largura,compound=TOP,text='Log de Informações',image=imagemLog)
    exibir_log.image = imagemLog
    exibir_log.grid(row=5,column=1)
    #Configurações
    imagemConfig = ImageTk.PhotoImage(Image.open('./icons/Automation80.png'))
    config = ttk.Button(level6,width=largura,compound=TOP,text='Configurações',image=imagemConfig)
    config.image = imagemConfig
    config.grid(row=5,column=2)
    #Sair
    imagemSair= ImageTk.PhotoImage(Image.open('./icons/cancel80.png'))
    sair = ttk.Button(level6,width=largura,compound=TOP,text='Sair',image=imagemSair,command=partial(btSair,login,usuario,level,janelaPai,janela))
    sair.image = imagemSair
    sair.grid(row=5,column=3,sticky=W)

    #Rodapé
    suporte1 = Label(level6,text='')
    suporte1.grid(row=6,column=0)
    suporte2 = Label(level6,text='')
    suporte2.grid(row=7,column=0)
    version_lb = Label(level6, text=version, font=fonteTopo3)
    version_lb.grid(row=8,column=0,sticky=W)

    data_atual = datetime.now()
    dt_at_frt = data_atual.strftime('%d/%m/%y')
    data = Label(level6, text=dt_at_frt, font=fonteTopo3)
    data.grid(row=8,column=3,sticky=E)

    suporte1['bg']   = 'white'
    suporte2['bg']   = 'white'
    version_lb['bg'] = 'white'
    data['bg']       = 'white'

    janelaPai.title('Genius (Lite) ' + ' - ' + usuario + ' - ' + info)
    janelaPai.resizable(FALSE,FALSE)
    janelaPai['bg'] = 'white'

def btVoltarCadastroA(login,usuario,level,dictAlunos,janelaPai,frameAtual):
    frameAtual.destroy()
    menuLevel(login,usuario,level,dictAlunos,janelaPai)