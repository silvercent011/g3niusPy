#Funcional
from functools import partial
#Funções
from func.login import *
from func.log import *
from datetime import *
#TkInter
from tkinter import *
from tkinter import ttk, font, messagebox
#Sistema
import sys, platform, getpass

#Funçãonãoimplmentada
def ops():
    messagebox.showerror('Ops!','A função ainda não foi implementada')

#Botão Sair  

def btSair(loginEntrada,usuario,nivel,janelaPai,frame):
	
    colocaLog(loginEntrada,usuario,nivel,'SAIU DO SISTEMA')
    exit()

def materialImpresso(loginEntrada,usuario,nivel):
    ops()

def lancaNotas(loginEntrada,usuario,nivel):
    ops()

def gerenciarHorarios(loginEntrada,usuario,nivel):
    ops()

def frequenciaAlunos(loginEntrada,usuario,nivel):
    ops()

def avisosGer(loginEntrada,usuario,nivel):
    ops()

def gerUsers(loginEntrada,usuario,nivel):
    ops()