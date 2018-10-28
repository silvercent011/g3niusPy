import os
import platform

def limpaTela():
    '''
    Limpa o terminal de sistemas operacionais
    '''
    sistemaOperacional = platform.system()
    if sistemaOperacional == 'Windows':
        os.system('cls') #Windows
    elif sistemaOperacional == 'Linux' or sistemaOperacional == 'Darwin':
        os.system('clear') #Linux #MacOS
    else:
        os.system('clear') #Default

def exibeLinha():
    print('---------------------------------------')