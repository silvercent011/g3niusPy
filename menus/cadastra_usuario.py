#TkInter
from func.login import *
from tkinter import *
from tkinter import font, ttk, messagebox
from PIL import ImageTk, Image
#Funcional
from functools import partial
#Sistema
import sys
import platform
import getpass
def cadastraUsuarios(chaves,usuarios):
    '''
    Menu para cadastro
    '''
    version = 'Genius (LITE) - 7.0.1'
    altura       = 10
    largura      = 20
    largura2     = 62
    largura3	 = 17
    espacamento1 = 50
    espacamento2 = 20

    janela = Toplevel()
    janela.resizable(FALSE,FALSE)

    r = ttk.Style()
    r.configure('branco.TFrame',background='white')

    s = ttk.Style()
    s.configure('branco.TLabel',background='white')
    
    frameGeral = ttk.Frame(janela)
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

    label00 = ttk.Label(frameGeral,text='CADASTRAR USUÁRIOS',font=fonteTopo4)
    label00['style'] = 'branco.TLabel'
    label00.grid(row=0,column=0,columnspan=6,sticky=W)

    imagemUser = ImageTk.PhotoImage(Image.open('./icons/AddUserMale80px.png'))
    label0 = ttk.Label(frameGeral,text='',image=imagemUser)
    label0.image = imagemUser
    label0['style'] = 'branco.TLabel'
    label0.grid(row=0,column=7,sticky=E)

    label1 = ttk.Label(frameGeral, text='NOME COMPLETO',font=fonteTopo3)
    label1.grid(row=1,column=0,sticky=W)
    label1['style'] = 'branco.TLabel'
    nomeCompleto = ttk.Entry(frameGeral,font=fonteTopo3)
    nomeCompleto.grid(row=2,column=0,columnspan=10,sticky=W+E)

    label2 = ttk.Label(frameGeral, text='CPF (apenas números)',font=fonteTopo3)
    label2.grid(row=3,column=0,sticky=W)
    label2['style'] = 'branco.TLabel'
    cpf = ttk.Entry(frameGeral,font=fonteTopo3)
    cpf.grid(row=4,column=0,sticky=W+E)

    label3 = ttk.Label(frameGeral, text='SENHA',font=fonteTopo3)
    label3.grid(row=6,column=0,sticky=W)
    label3['style'] = 'branco.TLabel'
    senha = ttk.Entry(frameGeral,show='*',font=fonteTopo3)
    senha.grid(row=7, column=0,columnspan=6,sticky=W+E)

    labelSuporte0 = ttk.Label(frameGeral,text='')
    labelSuporte0.grid(row=6,column=6)
    labelSuporte0['style'] = 'branco.TLabel'

    label4 = ttk.Label(frameGeral, text='CONFIRMAR SENHA',font=fonteTopo3)
    label4.grid(row=6,column=7,sticky=W)
    label4['style'] = 'branco.TLabel'
    senhaC = ttk.Entry(frameGeral,show='*',font=fonteTopo3)
    senhaC.grid(row=7, column=7,sticky=W+E)

    labelSuporte1 = ttk.Label(frameGeral,text='')
    labelSuporte1.grid(row=9,column=0)
    labelSuporte1['style'] = 'branco.TLabel'

    labelSuporte2 = ttk.Label(frameGeral,text='')
    labelSuporte2.grid(row=10,column=0)
    labelSuporte2['style'] = 'branco.TLabel'

    label7 = ttk.Label(frameGeral,text='Codigo Verificador',font=fonteTopo3)
    label7.grid(row=12, column=0,sticky=W)
    label7['style'] = 'branco.TLabel'
    codigo = ttk.Entry(frameGeral,font=fonteTopo3)
    codigo.grid(row=13,column=0,columnspan=6,sticky=W+E)

    labelSuporte3 = ttk.Label(frameGeral,text='')
    labelSuporte3.grid(row=14,column=0)
    labelSuporte3['style'] = 'branco.TLabel'

    imagemEnviar = ImageTk.PhotoImage(Image.open('./icons/30/Approval30px.png'))
    enviar = ttk.Button(frameGeral, text='Cadastrar',compound=TOP,image=imagemEnviar,command=partial(ponte,nomeCompleto,cpf,senha,senhaC,codigo,chaves,usuarios))
    enviar.image = imagemEnviar
    enviar.grid(row=15,column=0,columnspan=6,sticky=W+E)

    imagemVoltar = ImageTk.PhotoImage(Image.open('./icons/30/Cancel30px.png'))
    voltar = ttk.Button(frameGeral, text='Voltar',compound=TOP,image=imagemVoltar,command=partial(fecharJanela,janela))
    voltar.image = imagemVoltar
    voltar.grid(row=15,column=7,sticky=W+E)

    janela['background'] = 'white'
    janela.title('Cadastrar usuários')
    janela.mainloop()

def fecharJanela(janela):
    janela.destroy()

def ponte(nomeCompleto,cpf,senha,senhaC,codigo,chaves,usuarios):
    nome2 = nomeCompleto.get()
    nome2 = nome2.upper()
    nomeCompleto.delete(0,END)
    cpf2 = cpf.get()
    cpf.delete(0,END)
    senha2 = senha.get()
    senha.delete(0,END)
    senhaC2 = senhaC.get()
    senhaC.delete(0,END)
    codigo2 = codigo.get()
    codigo.delete(0,END)
    cadastro(nome2,cpf2,senha2,senhaC2,codigo2,chaves,usuarios)

def cadastro(nome,cpf,senha,senhaC,codigo,chaves,usuarios):
    cpflen = len(cpf)
    if (cpf in usuarios):
        messagebox.showerror('Ops!','Um usuário com o mesmo CPF já está cadastrado!')
    else:
        if (cpflen>11 or cpflen<11):
            messagebox.showerror('Ops!', 'O cpf tá certo amigo?')
        else:
            if (senha != senhaC):
                messagebox.showinfo('Ops!', 'As senhas não conferem')
            else:
                if codigo in chaves:
                    cadastraUsuario(cpf,senha,nome,codigo,chaves,usuarios)
                    messagebox.showinfo('Parabéns!','Usuário Cadastrado com Sucesso')
                else:
                    messagebox.showerror('Ops!', 'Código Inválido')