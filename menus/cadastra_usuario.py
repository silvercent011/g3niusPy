#TkInter
from tkinter import ttk
from func.login import *
from tkinter import *
from tkinter import messagebox
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
    frameGeral = Toplevel()

    label1 = ttk.Label(frameGeral, text='Nome completo')
    label1.grid(row=0,column=0)
    nomeCompleto = ttk.Entry(frameGeral)
    nomeCompleto.grid(row=1,column=0)

    label2 = ttk.Label(frameGeral, text='CPF (apenas números)')
    label2.grid(row=2,column=0)
    cpf = ttk.Entry(frameGeral)
    cpf.grid(row=3,column=0)

    label3 = ttk.Label(frameGeral, text='Senha')
    label3.grid(row=4,column=0)
    senha = ttk.Entry(frameGeral,show='*')
    senha.grid(row=5, column=0)

    label4 = ttk.Label(frameGeral, text='Confirmar Senha')
    label4.grid(row=6,column=0)
    senhaC = ttk.Entry(frameGeral,show='*')
    senhaC.grid(row=7, column=0)

    label5 = ttk.Label(frameGeral)
    label5.grid(row=8,column=0)
    label6 = ttk.Label(frameGeral,text=' ')
    label6.grid(row=9,column=0)

    label7 = ttk.Label(frameGeral,text='Codigo Verificador')
    label7.grid(row=10, column=0)

    codigo = ttk.Entry(frameGeral)
    codigo.grid(row=11,column=0)


    enviar = ttk.Button(frameGeral, width=30, text='Cadastrar',command=partial(ponte,nomeCompleto,cpf,senha,senhaC,codigo,chaves,usuarios))
    enviar.grid(row=13,column=0)

    frameGeral.geometry('850x400')
    frameGeral.title('Cadastrar usuários')
    frameGeral.mainloop()

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
                else:
                    messagebox.showerror('Ops!', 'Código Inválido')