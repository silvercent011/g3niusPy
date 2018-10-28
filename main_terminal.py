from func.login import *
from func.terminal_options import *
import sys
import platform
import getpass


def menu():
    suporte = False
    while suporte == False:
        limpaTela()
        exibeLinha()
        print('1 - Fazer Login')
        print('2 - Cadastrar Usuarios')
        exibeLinha()
        opcao = int(input())
        if opcao == 1:
            menuLogin(usuarios)
        elif opcao == 2:
            menuCadastro()
        else:
            suporte = False

def menuLogin(dicionario):
    suporte = False
    while suporte == False:
        limpaTela()
        login = input('Login:')
        senha = getpass.getpass('Senha: ')
        if login in dicionario:
            if dicionario[login][1] == senha:
                suporte = True
                menuUsuario(login)
            else:
                print('A senha está incorreta')
                input()
        else:
            print('Usuário não identificado')
            input()

def menuCadastro():
    suporte = False
    while suporte == False:
        limpaTela()
        exibeLinha()
        print('Bem-Vindo ao cadastro de usuarios V0.5 - Terminal')
        nome = input('Digite seu nome completo por favor:')
        nome = nome.upper()
        login = input('Digite seu cpf, apenas números por favor :) :')
        senha = getpass.getpass('Senha: ')
        codigo = int(input('Digite o código de verificação fornecido pelo seu administrador:'))
        exibeLinha()
        cadastraUsuario(login,senha,nome,codigo,codigos,usuarios)
        opcao = input('Deseja cadastrar outro usuario? S/N')
        if opcao == 's' or opcao == 'S':
            suporte = False
        else:
            suporte = True
            menu()

def menuUsuario(login):
    limpaTela()
    nome = usuarios[login][2]
    nomeExib = usuarios[login][3]
    acesso = usuarios[login][4]
    exibeLinha()
    print(nomeExib)
    print('Usuário level',acesso)
    exibeLinha
    menuLevels(acesso)
    
    input()

def menuLevels(codigo):
    if (codigo == 6):
        exibeLinha()
        print('1 - Cadastrar Alunos')
        print('2 - Gerar códigos')
        print('3 - Sair')
        escolha = input()
        exibeLinha()
        escolhaInt = int(escolha)
        if (escolhaInt == 1):
            pass
        elif (escolhaInt == 2):
            nivel = int(input('Escolha o nível do usuário a ser cadastrado'))
            codigo = geraCodigos(nivel,codigos)
            print('ANOTE O CÓDIGO COM ATENÇÃO:', codigo)
            input()
            menuLevels(6)
        else:
            exit()

#Inicio do Programa - Terminal
usuarios = {}
codigos = {}

carregaCodigos(codigos)
carregaLogin(usuarios)

menu()

