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
    global nomeCompleto
    nomeCompleto = ttk.Entry(frameGeral,font=fonteTopo3)
    nomeCompleto.grid(row=2,column=0,columnspan=10,sticky=W+E)

    label2 = ttk.Label(frameGeral, text='CPF (apenas números)',font=fonteTopo3)
    label2.grid(row=3,column=0,sticky=W)
    label2['style'] = 'branco.TLabel'
    global cpf
    cpf = ttk.Entry(frameGeral,font=fonteTopo3)
    cpf.grid(row=4,column=0,sticky=W+E)

    label3 = ttk.Label(frameGeral, text='SENHA',font=fonteTopo3)
    label3.grid(row=6,column=0,sticky=W)
    label3['style'] = 'branco.TLabel'
    global senha
    senha = ttk.Entry(frameGeral,show='*',font=fonteTopo3)
    senha.grid(row=7, column=0,columnspan=6,sticky=W+E)

    labelSuporte0 = ttk.Label(frameGeral,text='')
    labelSuporte0.grid(row=6,column=6)
    labelSuporte0['style'] = 'branco.TLabel'

    label4 = ttk.Label(frameGeral, text='CONFIRMAR SENHA',font=fonteTopo3)
    label4.grid(row=6,column=7,sticky=W)
    label4['style'] = 'branco.TLabel'
    global senhaC
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
    global codigo
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
    cpf2 = cpf.get()
    senha2 = senha.get()
    senhaC2 = senhaC.get()
    codigo2 = codigo.get()
    cadastro(nome2,cpf2,senha2,senhaC2,codigo2,chaves,usuarios)

def cadastro(nome,cpf2,senha2,senhaC2,codigo2,chaves,usuarios):
    cpflen = len(cpf2)
    if nome == '' or cpf2 == '' or senha2 == '' or senhaC2 == '' or codigo == '':
        messagebox.showerror('Ops!', 'Você preencheu todos os campos?')
    else:
        if (cpf2 in usuarios):
            cpf.delete(0,END)
            messagebox.showerror('Ops!','Um usuário com o mesmo CPF já está cadastrado!')
        else:
            if (cpf2.isnumeric()):
                if (cpflen>11 or cpflen<11):
                    cpf.delete(0,END)
                    messagebox.showerror('Ops!', 'O cpf tá certo amigo?')
                else:
                    if (senha2 != senhaC2):
                        senha.delete(0,END)
                        senhaC.delete(0,END)
                        messagebox.showerror('Ops!', 'As senhas não conferem')
                    else:
                        if codigo2 in chaves:
                            cadastraUsuario(cpf2,senha2,nome,codigo2,chaves,usuarios)
                            nomeCompleto.delete(0,END)
                            cpf.delete(0,END)
                            senha.delete(0,END)
                            senhaC.delete(0,END)
                            codigo.delete(0,END)
                            messagebox.showinfo('Parabéns!','Usuário Cadastrado com Sucesso')
                        else:
                            codigo.delete(0,END)
                            messagebox.showerror('Ops!', 'Código Inválido') 
            else:
                cpf.delete(0,END)
                messagebox.showerror('Ops!','O campo de cpf só aceita números')