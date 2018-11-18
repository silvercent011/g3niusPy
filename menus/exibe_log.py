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

log_file = './data/log.genius'

def janela_log(login,nivel,usuario,janelaPai,janelaFechar, funcaoFechar):
    janelaFechar.destroy()

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

    frameGeral = ttk.Frame(janelaPai)
    frameGeral.grid(row=0,column=0)
    frameGeral['padding'] = (espacamento1,espacamento2)
    frameGeral['style'] = 'branco.TFrame'

    #Fontes e estilos
    fonteTo5 = font.Font(family='Segoe Ui', size=18, weight='bold')
    fonteTopo2 = font.Font(family='Segoe Ui', size=14, weight='normal')
    fonteTopo3 = font.Font(family='Segoe Ui', size=12, weight='normal')
    fonteTopo4 = font.Font(family='Segoe Ui', size=24, weight='bold')
    fonteTopo5 = font.Font(family='Segoe Ui', size=35, weight='bold')
    fonteTopo6 = font.Font(family='Segoe Ui', size=14, weight='bold')

    global boxLog
    boxLog = Listbox(frameGeral,width=largura2)
    boxScroll = Scrollbar(frameGeral,orient=VERTICAL,command=boxLog.yview)
    boxLog.configure(yscrollcommand=boxScroll.set)
    boxLog.grid(row=1,column=0,sticky=W+E)
    boxScroll.grid(row=1,column=0,sticky=E+S+N)
    carregaLogWidget(boxLog)

    imageVoltar = ImageTk.PhotoImage(Image.open('./icons/30/Cancel30px.png'))
    btVoltar = ttk.Button(frameGeral,text='Voltar',width=largura,compound=TOP,image=imageVoltar,command=partial(funcaoFechar,login,usuario,nivel,janelaPai,frameGeral))
    btVoltar.grid(row=2,column=0,ipady=altura)
    btVoltar.image = imageVoltar