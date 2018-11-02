#Sidney Alex
#Genius Lite
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
