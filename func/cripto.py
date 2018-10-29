#Sidney Alex
##Criptografia Genius Lite
from random import randint
import os
import platform
import sys

'''
Genius(Lite) Cripto 2.0
'''

criptoPublic = './data/chavePublica.txt'
criptoPrivate = './data/chavePrivada.txt'
def carregaChave(chave):
    if (chave == 1):
        arquivo = open(criptoPublic,'r',encoding='utf-8')
        leituraAtual = ''
        chaves = []
        for x in arquivo:
            for y in x:
                if y != '*':
                    leituraAtual += y
                else:
                    chaves.append(leituraAtual)
                    leituraAtual = ''
        return chaves
        arquivo.close()
    elif (chave == 2) :
        arquivo = open(criptoPrivate,'r',encoding='utf-8')
        leituraAtual = ''
        chaves = []
        for x in arquivo:
            for y in x:
                if y != '*':
                    leituraAtual += y
                else:
                    chaves.append(leituraAtual)
                    leituraAtual = ''
        return chaves
        arquivo.close()

def criptografaTexto(texto):
    '''
    Função recebe uma string e a retorna criptogradafa
    '''
    chave = carregaChave(1)
    final = ''
    e = int(chave[0])
    n = int(chave[1])
    for x in texto:
        codigoOrd = ord(x)
        cripto = codigoOrd**e%n
        info = str(cripto) + '*'
        final+=info
    
    return final

def descriptografaTexto(texto):
    '''
    Função recebe uma string criptogradafa e retorna legível
    '''
    chave = carregaChave(2)
    final = ''
    d = int(chave[0])
    n = int(chave[1])
    caracteres = texto.split('*')
    for x in caracteres:
        if x != '\n':
            codigoOrd = int(x)
            cripto = chr(codigoOrd**d%n)
            final+=cripto
    
    return final

