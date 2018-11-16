#Sidney Alex
#Genius Lite
from tkinter import *
from datetime import *
from func.cripto import *
import os
import platform
import sys

arqAlunos = './data/database.genius'

def cadastrarAlunosArquivo(nomeAluno,codigoAluno,turma,turno,ano,cpfUser,dictAlunos):
    arquivo = open(arqAlunos, 'a', encoding='utf-8')
    ch = '*'
    info = codigoAluno+ ch + codigoAluno + ch + nomeAluno + ch + turma + ch + turno + ch + ano + ch + cpfUser + ch 
    info2 = criptografaTexto(info) + '\n'
    arquivo.write(info2)
    arquivo.close()
    dictAlunos.clear()
    carregaAlunosArquivo(arqAlunos,dictAlunos)

def carregaAlunosArquivo(arquivo,dictAlunos):
    arquivo = open(arqAlunos, 'r', encoding='utf-8')
    linhas = arquivo.readlines()
    for x in linhas:
        suporte = []
        linhaAt = descriptografaTexto(x)
        itens = linhaAt.split('*')
        tupla = (itens[1],itens[2],itens[3],itens[4],itens[5],itens[6])
        dictAlunos[itens[0]] = tupla
    arquivo.close()

def carregaAlunosBox(widget,dictAlunos):
    '''
    Carregaa alunos no widget dado como parâmetro
    '''
    cont=0
    for x in dictAlunos:
    	item = x + ' - ' + str(dictAlunos[x][2]) + ' - ' + str(dictAlunos[x][3]) + ' - ' + str(dictAlunos[x][1])
    	widget.insert(END,item)
    	cont+=1
    

def salvarModificacoesAlunos(codigo,nome,turma,turno,ano,cpf,dictAlunos):
    ch = '*'
    valor = (codigo,nome,turma,turno,ano,cpf)
    dictAlunos.update(codigo = valor)

    arquivo = open(arqAlunos,'w',encoding='utf-8')
    for w in dictAlunos:
        x = dictAlunos[w]
        info = str(x[0]) + ch + str(x[0]) + ch + x[1] + ch + x[2] + ch + x[3] + ch + x[4] + ch + x[5] + ch
        info2 = criptografaTexto(info) + '\n'
        arquivo.write(info2)

    arquivo.close()
    dictAlunos.clear()
    carregaAlunosArquivo(arqAlunos,dictAlunos)

def excluirAluno(codigo,nome,turma,turno,ano,cpf,dictAlunos):
    ch = '*'
    valor = (codigo,nome,turma,turno,ano,cpf)
    dictAlunos.pop(codigo)

    arquivo = open(arqAlunos,'w',encoding='utf-8')
    for w in dictAlunos:
        x = dictAlunos[w]
        info = str(x[0]) + ch + str(x[0]) + ch + x[1] + ch + x[2] + ch + x[3] + ch + x[4] + ch + x[5] + ch
        info2 = criptografaTexto(info) + '\n'
        arquivo.write(info2)

    arquivo.close()
    dictAlunos.clear()
    carregaAlunosArquivo(arqAlunos,dictAlunos)

def organizaAlunosNome(widget,dictAlunos):
    pass

def organizaAlunosTurma(widget,dictAlunos,turma):
    pass

def organizaAlunosTurno(widget,dictAlunos,turno):
    pass

def organizaAlunosAno(widget,dictAlunos,ano):
    pass

def organizaAlunosStatus(widget,dictAlunos,status):
    '''
    Situação, Ativo ou Inativo
    '''
    pass


    