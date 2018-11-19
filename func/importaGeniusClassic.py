#Sidney Alex
#Genius Lite
from tkinter import *
from datetime import *
import time
from cripto import *
import os
import platform
import sys
from tkinter import messagebox

arqAlunos = './data/database.genius'
arqImport = './data/classic.txt'

def cadastrarAlunosArquivo():
    try:
        arquivo = open(arqImport,'r',charset='utf-8')
        linhas = arquivo.readlines()
    except:
        arquivo = open(arqImport,'r')
        linhas = arquivo.readlines()
    
    for x in linhas:
        data = x.split('\t')
        nomeAluno = data[0]
        turma = data[1]
        turno = data[3]
        ano = data[4]
        cpfUser = '12126688470' 
        codigoAluno1 = datetime.now()
        codigoAluno2 = str(codigoAluno1.strftime('%y%m%d%H%M%S'))
        time.sleep(1)
        print(nomeAluno + ' - ' + codigoAluno2)
        arquivo2 = open(arqAlunos, 'a', encoding='utf-8')
        ch = '*'
        info = codigoAluno2 + ch + codigoAluno2 + ch + nomeAluno + ch + turma + ch + turno + ch + ano + ch + cpfUser + ch 
        info2 = criptografaTexto(info) + '\n'
        arquivo2.write(info2)
        arquivo2.close()
    arquivo.close()
cadastrarAlunosArquivo()

input()