import os
import platform
import sys
'''
Genius(Lite) Login Main Backend 1.0 - GLMB
'''
def testeBotao():
    print('Funcionou')

def arquivos(codigoFuncao):
    pass

def criptografaInfo(texto):
    e = 71
    n = 1073
    antes = texto
    depois = ''
    for x in antes:
        numero = ord(x)
        convert = chr(numero**e%n)
        depois+=convert

    return depois

def descriptografaInfo(users):
    datab = open('users.genius','r',encoding='utf-8')
    d = 1079
    n = 1073
    cr = '*'
    depois = ''
    for x in datab:
        listaSuporte = []
        palavra = ''
        for y in x:
            #char(y^d mod n).
            numero = ord(y)
            convert = chr(numero**d%n)
            depois+=convert
        for y in depois:
            if (y != cr):
                palavra+=y
            else:
                listaSuporte.append(palavra)
                palavra = ''
        print(listaSuporte)
        users[listaSuporte[0]] = tuple(listaSuporte)
    datab.close()

def abrirCodigos(lista):
    data = open('codigos.genius','r')
    for x in data:
        lista.append(int(x))
    data.close()

def cadastraUsuario(acesso,login,senha,nome):
    data = open ('users.genius','a', encoding="utf-8")
    cr = '*'
    info = login+cr+senha+cr+str(acesso)+cr+nome+cr+'\n'
    gravar = criptografaInfo(info)
    print(gravar)
    data.write(gravar)    
    data.close()


def verificaLogin():
    pass

def mensagem():
    pass

codigosLiberados = []
users = {}
descriptografaInfo(users)
abrirCodigos(codigosLiberados)
print(codigosLiberados)
acesso = 3
login = input('Login:')
senha = input('Senha')
nome = input('Nome completo')
cadastraUsuario(acesso,login,senha,nome)
print(users)
