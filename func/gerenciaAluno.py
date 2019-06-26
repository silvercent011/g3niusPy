#Sidney Alex
#Genius Lite
from tkinter import *
from datetime import *
from func.cripto import *
from func.b_sort import *
import os
import platform
import sys
from tkinter import messagebox

arqAlunos = './data/database.genius'

def cadastrarAlunosArquivo(nomeAluno,codigoAluno,turma,turno,ano,cpfUser,dictAlunos):
    '''
    Cadastra os dados inseridos nos parâmetros no arquivo database
    '''
    with open(arqAlunos, 'a', encoding='utf-8') as arquivo:
        ch = '*'
        info = codigoAluno+ ch + codigoAluno + ch + nomeAluno + ch + turma + ch + turno + ch + ano + ch + cpfUser + ch 
        info2 = criptografaTexto(info) + '\n'
        arquivo.write(info2)

    dictAlunos.clear()
    carregaAlunosArquivo(arqAlunos,dictAlunos)

def carregaAlunosArquivo(arquivo,dictAlunos):
    '''
    Carrega os alunos do arquivo database para o dicionário de alunos
    '''
    with open(arqAlunos, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        for x in linhas:
            suporte = []
            linhaAt = descriptografaTexto(x)
            itens = linhaAt.split('*')
            tupla = (itens[1],itens[2],itens[3],itens[4],itens[5],itens[6])
            dictAlunos[itens[0]] = tupla

def carregaAlunosBox(widget,dictAlunos):
    '''
    Carrega alunos no widget dado como parâmetro
    '''
    organizaAlunosNome(widget,dictAlunos)
    
def salvarModificacoesAlunos(codigo,nome,turma,turno,ano,cpf,dictAlunos):
    '''
    Salva modificações feitas no arquivo
    '''
    ch = '*'
    valor = (codigo,nome,turma,turno,ano,cpf)
    dictAlunos.update(codigo = valor)

    with open(arqAlunos,'w',encoding='utf-8') as arquivo:
        for w in dictAlunos:
            x = dictAlunos[w]
            info = str(x[0]) + ch + str(x[0]) + ch + x[1] + ch + x[2] + ch + x[3] + ch + x[4] + ch + x[5] + ch
            info2 = criptografaTexto(info) + '\n'
            arquivo.write(info2)

    dictAlunos.clear()
    carregaAlunosArquivo(arqAlunos,dictAlunos)

def excluirAluno(codigo,nome,turma,turno,ano,cpf,dictAlunos):
    '''
    Exclui aluno do arquivo e dicionário
    '''
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
    '''
    Organiza alunos no widget pela ordem alfabética dos nomes
    '''
    widget.delete(0,END)
    alunos = []
    ch = ' - '
    for x in dictAlunos:
        info = dictAlunos[x]
        info2 = (info[0],info[1],info[2],info[3],info[4])
        alunos.append(info2)
    bSortIndex(alunos,1)

    alunos2 = []
    for x in alunos:
        info = x
        info2 = x[0] + ch + x[1] + ch + x[2] + ch + x[3] + ch + x[4]
        alunos2.append(info2)
    
    widget.insert(END,*alunos2)

def organizaAlunosTurma(widget,dictAlunos):
    '''
    Organiza alunos no widget pela ordem crescente das turmas
    '''
    widget.delete(0,END)
    alunos = []
    ch = ' - '
    for x in dictAlunos:
        info = dictAlunos[x]
        info2 = (info[0],info[1],info[2],info[3],info[4])
        alunos.append(info2)
    bSortIndex(alunos,2)

    alunos2 = []
    for x in alunos:
        info = x
        info2 = x[0] + ch + x[1] + ch + x[2] + ch + x[3] + ch + x[4]
        alunos2.append(info2)
    
    widget.insert(END,*alunos2)

def organizaAlunosChave(widget,dictAlunos):
    '''
    Organiza alunos no widget pela ordem crescente das chaves
    '''
    widget.delete(0,END)
    alunos = []
    ch = ' - '
    for x in dictAlunos:
        info = dictAlunos[x]
        info2 = (info[0],info[1],info[2],info[3],info[4])
        alunos.append(info2)
    bSortIndex(alunos,0)

    alunos2 = []
    for x in alunos:
        info = x
        info2 = x[0] + ch + x[1] + ch + x[2] + ch + x[3] + ch + x[4]
        alunos2.append(info2)
    
    widget.insert(END,*alunos2)

def imprimeUnico(widget,dictAlunos,valor):
    '''
    Imprime valor selecionado no arquivo
    '''
    codigo = valor.get()
    if codigo == '':
        messagebox.showerror('Ops!','Aluno não selecionado.')
    else:
        ch = ' - '
        linha = '---------------------------------------------------------------------------------------------------------\n'
        with open('infoUnico.txt','w',encoding='utf-8') as arquivo:
            arquivo.write(linha)
            info = dictAlunos[codigo]
            value = info[0] + ch + info[1] + ch + info[2] + ch + info[3] + ch + info[4] + '\n'
            arquivo.write(value)
            arquivo.write(linha)
            
        messagebox.showinfo('Olá','Dados impressos no arquivo!')

def imprimeGeral(widget,dictAlunos):
    '''
    Imprime todos os dados em um arquivo
    '''
    ch = ' - '
    linha = '---------------------------------------------------------------------------------------------------------\n'
    with open('info.txt','w',encoding='utf-8') as arquivo:
        arquivo.write(linha)
        cont = 1
        listaSuporte = []
        for x in dictAlunos:
            info = dictAlunos[x]
            value = info[0] + ch + info[1] + ch + info[2] + ch + info[3] + ch + info[4]
            listaSuporte.append(value)

        bSort(listaSuporte)

        for x in listaSuporte:
            number = '(' + str(cont) +')'
            atual = x
            value = number + ch + atual + '\n'
            arquivo.write(value)
            arquivo.write(linha)
            cont+=1

    messagebox.showinfo('Olá','Dados impressos no arquivo!')


def organizaAlunosTurno(widget,dictAlunos):
    '''
    Organiza alunos no widget pela ordem crescente do ano letivo
    '''
    widget.delete(0,END)
    alunos = []
    ch = ' - '
    for x in dictAlunos:
        info = dictAlunos[x]
        info2 = (info[0],info[1],info[2],info[3],info[4])
        alunos.append(info2)
    bSortIndex(alunos,3)

    alunos2 = []
    for x in alunos:
        info = x
        info2 = x[0] + ch + x[1] + ch + x[2] + ch + x[3] + ch + x[4]
        alunos2.append(info2)
    
    widget.insert(END,*alunos2)

def organizaAlunosAno(widget,dictAlunos):
    '''
    Organiza alunos no widget pela ordem crescente do ano letivo
    '''
    widget.delete(0,END)
    alunos = []
    ch = ' - '
    for x in dictAlunos:
        info = dictAlunos[x]
        info2 = (info[0],info[1],info[2],info[3],info[4])
        alunos.append(info2)
    bSortIndex(alunos,4)

    alunos2 = []
    for x in alunos:
        info = x
        info2 = x[0] + ch + x[1] + ch + x[2] + ch + x[3] + ch + x[4]
        alunos2.append(info2)
    
    widget.insert(END,*alunos2)

def encontraSubstring(widget,dictAlunos,string):
    '''
    Encontra substring em nome de alunos
    '''
    string = string.upper()
    widget.delete(0,END)
    alunos = []
    ch = ' - '
    for x in dictAlunos:
        info = dictAlunos[x]
        info2 = (info[0],info[1],info[2],info[3],info[4])
        alunos.append(info2)
    bSortIndex(alunos,1)

    alunos2 = []
    for x in alunos:
        info = x
        if string in x[1]:
            info2 = x[0] + ch + x[1] + ch + x[2] + ch + x[3] + ch + x[4]
            alunos2.append(info2)
    
    widget.insert(END,*alunos2)