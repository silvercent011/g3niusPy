#Sidney Alex
#Genius Lite
from tkinter import *
from datetime import *
from func.cripto import *
import os
import platform
import sys
from tkinter import messagebox

arqAlunos = './data/users.genius'

def carregaUsersArquivo(arquivo,dictUsers):
    arquivo = open(arqAlunos, 'r', encoding='utf-8')
    linhas = arquivo.readlines()
    for x in linhas:
        suporte = []
        linhaAt = descriptografaTexto(x)
        itens = linhaAt.split('*')
        tupla = (itens[0],itens[1],itens[2],itens[3],itens[4])
        dictUsers[itens[0]] = tupla
    arquivo.close()

def carregaUsersBox(widget,dictUsers):
    '''
    Carregaa alunos no widget dado como parâmetro
    '''
    cont=0
    for x in dictUsers:
    	item = x + ' - ' + str(dictUsers[x][2]) + ' - ' + str(dictUsers[x][4])
    	widget.insert(END,item)
    	cont+=1
    

def salvarModificacoesUser(cpf,nome,nivel,dictUsers):
    senha = dictUsers[cpf][1]
    nomeRed = dictUsers[cpf][3]
    ch = '*'
    valor = (cpf,senha,nome,nomeRed,nivel)
    dictUsers.update(cpf = valor)

    arquivo = open(arqAlunos,'w',encoding='utf-8')
    for w in dictUsers:
        x = dictUsers[w]
        info = str(x[0]) + ch + str(x[1]) + ch + x[2] + ch + x[3] + ch + str(x[4])  + ch
        info2 = criptografaTexto(info) + '\n'
        arquivo.write(info2)

    arquivo.close()
    dictUsers.clear()
    carregaUsersArquivo(arqAlunos,dictUsers)

def excluirUser(cpf,nome,nivel,dictUsers):
    senha = dictUsers[cpf][1]
    nomeRed = dictUsers[cpf][3]
    ch = '*'
    valor = (cpf,senha,nome,nomeRed,nivel)
    dictUsers.pop(cpf)

    arquivo = open(arqAlunos,'w',encoding='utf-8')
    for w in dictUsers:
        x = dictUsers[w]
        info = str(x[0]) + ch + str(x[1]) + ch + x[2] + ch + x[3] + ch + str(x[4])  + ch
        info2 = criptografaTexto(info) + '\n'
        arquivo.write(info2)

    arquivo.close()
    dictUsers.clear()
    carregaUsersArquivo(arqAlunos,dictUsers)
