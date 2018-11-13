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
    largura2     = 90
    largura3	 = 17
    espacamento1 = 50
    espacamento2 = 20

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

    boxAlunos = ttk.Treeview(frameGeral)
    boxScroll = Scrollbar(frameGeral,orient=VERTICAL,command=boxAlunos.yview)
    boxAlunos.configure(yscrollcommand=boxScroll.set)
    boxAlunos.grid(row=1,column=0,sticky=W)
    boxScroll.grid(row=1,column=0,sticky=E+S+N)
    carregaAlunosBox(boxAlunos,dictAlunos)

   
    #Frame para agrupar os botões 
    botoes = ttk.Frame(frameGeral)
    botoes.grid(row=10,column=0)

    btImprimir = ttk.Button(botoes,text='Imprimir')
    btImprimir.grid(row=0,column=0)

    btFiltrar = ttk.Button(botoes,text='Filtrar')
    btFiltrar.grid(row=0,column=1)

    btEditar = ttk.Button(botoes,text='Editar')
    btEditar.grid(row=0,column=2)

    btVoltar = ttk.Button(botoes,text='Voltar',command=partial(funcaoFechar,login,usuario,nivel,dictAlunos,janelaPai,frameGeral))
    btVoltar.grid(row=0,column=3)