from random import randint
import os
import platform
import sys
'''
Genius(Lite) Cript + Login Backend 1.0 - GCLB
'''
#Arquivos
codigos_genius = './data/codigos.genius'
users_genius = './data/users.genius'
log_genius = './data/users.genius'
def criptografaTexto(texto):
    '''
    Função recebe uma string e a retorna criptogradafa
    '''
    final = ''
    e = 71
    n = 1073
    for x in texto:
        codigoOrd = ord(x)
        cripto = chr(codigoOrd**e%n)
        final+=cripto
    
    return final

def descriptografaTexto(texto):
    '''
    Função recebe uma string criptogradafa e retorna legível
    '''
    final = ''
    d = 1079
    n = 1073
    for x in texto:
        codigoOrd = ord(x)
        cripto = chr(codigoOrd**d%n)
        final+=cripto
    
    return final

def carregaLogin(users):
    '''
    Carrega dados dos usuários do arquivo para os dicionários
    '''
    arquivo = open(users_genius,'r',encoding='utf-8')
    for x in arquivo:
        info = descriptografaTexto(x)
        listaSuporte = []
        stringSuporte = ''
        for y in info:
            if (y == '*'):
                listaSuporte.append(stringSuporte)
                stringSuporte = ''
            elif (y=='\n'):
                login = listaSuporte[0]
                senha = listaSuporte[1]
                nomeCompleto = listaSuporte[2]
                nomeExib = listaSuporte[3]
                nivel = int(listaSuporte[4])
                users[login] = (login,senha,nomeCompleto,nomeExib,nivel)
                listaSuporte = []
            else:
                stringSuporte+=y    

def cadastraUsuario(login,senha,nome,verificador,chaves,usuarios):
    '''
    Cadastra usuários no arquivo e no dicionário
    login*senha*nomeCompleto*nomeExibicao*niveldeacesso*
    '''
    ch = '*'
    loginstr = str(login)
    tamanhoLogin = len(loginstr)
    if (tamanhoLogin < 11):
        print('Você digitou o CPF inteiro?')
        input('Pressione Enter para tentar novamente')
        return 0
    elif(tamanhoLogin > 11):
        print('Seu CPF tomou bomba amigo?')
        input('Pressione Enter para tentar novamente')
        return 0
    else:
        print('Passou')
    if (verificador in chaves):
        if (login in usuarios):
            print('Usuário já cadastrado no sistema!')
            input()
        else:
            listaNome = nome.split(' ')
            nomeExib = ''

            if (len(listaNome) == 1):
                nomeExib = listaNome[0]
            else:
                nomeExib = listaNome[0] + ' ' + listaNome[-1]
            #Verificar a chave de acesso para saber o nível do usuário
            nivelFinal = 0
            if  (chaves[verificador][1] == 1):
                nivelFinal = 1
            elif(chaves[verificador][1] == 2):
                nivelFinal = 2
            elif(chaves[verificador][1] == 3):
                nivelFinal = 3
            elif(chaves[verificador][1] == 4):
                nivelFinal = 4
            elif(chaves[verificador][1] == 5):
                nivelFinal = 5
            elif(chaves[verificador][1] == 6):
                nivelFinal = 6
            elif(chaves[verificador][1] == 7):
                nivelFinal = 7
            elif(chaves[verificador][1] == 8):
                nivelFinal = 8
            elif(chaves[verificador][1] == 9):
                nivelFinal = 9
            elif(chaves[verificador][1] == 10):
                nivelFinal = 10
                
            #Conversão explicita
            loginStr = str(login)
            nivelFinalStr = str(nivelFinal)
            #login*senha*nomeCompleto*nomeExibicao*niveldeacesso*
            info = loginStr+ch+senha+ch+nome+ch+nomeExib+ch+nivelFinalStr+ch+'\n'
            usuarios[login] = (login,senha,nome,nomeExib,nivelFinal)
            infoCripto = criptografaTexto(info)
    
            arquivo = open(users_genius,'a',encoding='utf-8')
            arquivo.write(infoCripto)
            arquivo.close()
            excluiCodigo(verificador,chaves)
    else:
        print('Chave verificação inválida,tente novamente!')
        input()

def carregaCodigos(codigos):
    '''
    Carrega os códigos de cadastro para o dicionário específico
    '''
    arquivo = open(codigos_genius,'r',encoding='utf-8')
    for x in arquivo:
        info = descriptografaTexto(x)
        listaSuporte = []
        stringSuporte = ''
        for y in info:
            if (y == '*'):
                listaSuporte.append(stringSuporte)
                stringSuporte = ''
            elif (y == '\n'):
                chave = int(listaSuporte[0])
                codigo1 = int(listaSuporte[1])
                codigo2 = int(listaSuporte[2])
                dataIn = (codigo1,codigo2)
                codigos[chave] = dataIn
                listaSuporte = []
            else:
                stringSuporte += y
            
    arquivo.close()

def excluiCodigo(codigo,dicionario):
    del dicionario[codigo]
    arquivo = open(codigos_genius,'w',encoding='utf-8')
    ch = '*'
    for x in dicionario:
        chave = str(dicionario[x][0])
        nivel = str(dicionario[x][1])
        info = chave+ch+chave+ch+nivel+ch+'\n'
        infoCripto = criptografaTexto(info)
        arquivo.write(infoCripto)
    arquivo.close()
    dicionario.clear()
    carregaCodigos(dicionario)

def geraCodigos(nivel,dicionario):
    '''
    Cadastra códigos em arquivo, Nível 6+
    '''
    arquivo = open(codigos_genius,'a',encoding='utf-8')
    codigo = randint(111111,999999)
    ch = '*'
    info = str(codigo)+ch+str(codigo)+ch+str(nivel)+ch+'\n'
    infoCripto = criptografaTexto(info)
    arquivo.write(infoCripto)
    arquivo.close()
    data = (codigo,nivel)
    dicionario[codigo] = data
    return codigo

def esqueceuSenha(login,verificador):
    pass

def arquivosDefault():
    pass

#Lembrar de montar as funções de esquecer senha e arquivos default, ocultar pastas
#e remover as chaves já utilizadas do arquivo, talvez mexer no sistema de arquivos
codes = {}
users = {}