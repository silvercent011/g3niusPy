#Sidney Alex
#Genius Lite
from datetime import *
from func.cripto import *
import os
import platform
import sys
from tkinter import *

log_file = './data/log.genius'
log_file_txt = './data/log.txt'

data_atual = datetime.now()
dt_at_frt = data_atual.strftime('%d/%m/%y')
hora_atual = data_atual.strftime('%H:%M')

def colocaLog(codigo,nome,nivel,acao):
    arquivo = open(log_file,'a',encoding='utf-8')
    ch = '*'
    info = str(codigo) + ch + str(nivel) +ch+ nome + ch + acao + ch + dt_at_frt + ch + hora_atual + ch
    info2 = criptografaTexto(info) + '\n'
    arquivo.write(info2)
    arquivo.close()

    arquivo = open(log_file_txt,'a',encoding='utf-8')
    ch = '*'
    info = str(codigo) + ch + str(nivel) +ch+ nome + ch + acao + ch + dt_at_frt + ch + hora_atual + ch
    info2 = info + '\n'
    arquivo.write(info2)
    arquivo.close()
    

def carregaLog(dicionario):
    arquivo = open(log_file,'r',encoding='utf-8')
    ch = '*'
    linhas = arquivo.readlines()
    cont = 0
    for x in linhas:
        info = descriptografaTexto(x)
        listaSuporte = info.split(ch)
        cont += 1
        tupla = (listaSuporte[0],listaSuporte[1],listaSuporte[2],listaSuporte[3],listaSuporte[4],listaSuporte[5])
        dicionario[cont] = tupla                
    arquivo.close()

def carregaLogWidget(widget):
    arquivo = open(log_file,'r',encoding='utf-8')
    linhas = arquivo.readlines()
    ch = ' - '
    for x in linhas:
        atual = descriptografaTexto(x)
        info = atual.split('*')
        info2 = info[0] + ch + 'Level' + info[1] + ch + info[2] + ch + info[4] + ch + info[5] + ch + info[3]
        widget.insert(END,info2) 
