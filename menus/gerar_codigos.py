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


arqCod = './data/codigos.genius'

def gerarCodigos(login,nivel,usuario,janelaPai,janelaFechar, funcaoFechar):
    codigos = {}
    carregaCodigos(codigos)
    janelaFechar.destroy()

    version = 'Genius (LITE) - 7.0.1'
    altura       = 10
    largura      = 20
    largura2     = 62
    largura3	 = 17
    espacamento1 = 50
    espacamento2 = 20

    r = ttk.Style()
    r.configure('branco.TFrame',background='white')

    s = ttk.Style()
    s.configure('branco.TLabel',background='white')

    frameGeral = ttk.Frame(janelaPai)
    frameGeral.grid(row=0,column=0)
    frameGeral['style'] = 'branco.TFrame'
    frameGeral['padding'] = (espacamento1,espacamento2)

    #Fontes e estilos
    fonteTo5 = font.Font(family='Segoe Ui', size=18, weight='bold')
    fonteTopo2 = font.Font(family='Segoe Ui', size=14, weight='normal')
    fonteTopo3 = font.Font(family='Segoe Ui', size=12, weight='normal')
    fonteTopo4 = font.Font(family='Segoe Ui', size=24, weight='bold')
    fonteTopo5 = font.Font(family='Segoe Ui', size=35, weight='bold')
    fonteTopo6 = font.Font(family='Segoe Ui', size=14, weight='bold')

    label1 = ttk.Label(frameGeral,text='GERAR CÓDIGOS',font=fonteTopo4)
    label1.grid(row=0,column=1,sticky=W)
    label2 = ttk.Label(frameGeral,text='Selecione o nível:',font=fonteTo5)
    label2.grid(row=1,column=1,sticky=W)
    levels = StringVar()
    niveis = ttk.Combobox(frameGeral,textvariable=levels,font=fonteTopo3)
    niveis['values'] = ('Selecionar','3','4','6')
    niveis.grid(row=2,column=1,sticky=W+E)

    label3 = ttk.Label(frameGeral,text='',font=fonteTopo3)
    label3.grid(row=4,column=1,sticky=W)

    salvar = ttk.Button(frameGeral,text='Salvar',command=partial(ponte,login,nivel,usuario,niveis,label3,codigos))
    salvar.grid(row=10,column=1)    

    voltar = ttk.Button(frameGeral,text='Voltar',command=partial(funcaoFechar,login,usuario,nivel,janelaPai,frameGeral))
    voltar.grid(row=10,column=2)

def ponte(login,level,usuario,nivel,status,dictCodigos):
    nivel2 = nivel.get()
    nivel2 = nivel2.upper()

    if nivel2 == '' or nivel2 == 'SELECIONAR':
        messagebox.showerror('ops!','Nível de usuário não selecionado!')
    else:
        conectaCadastroCodigo(login,level,usuario,nivel2,status,dictCodigos)
    
def conectaCadastroCodigo(login,level,usuario,nivel,status,dictCodigos):
    codigo_final = geraCodigos(nivel,dictCodigos)
    status['text'] = 'Anote seu código: ' + codigo_final
    acao = 'Cadastrou código ' + codigo_final + ' no sistema'
    colocaLog(login,usuario,level,acao)

