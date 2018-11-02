from cripto import *
'''
Genius (Lite) - Backend Input Data
- Cadastro de Alunos
- Cadastro de Turmas

'''
data1 = './data/database_intern.genius'
data2 = './data/hrrq.genius'
dataAlunos = './data/database.genius'

def cadastraAluno(nome,turma,turno,ano,dicionario,USER,LOGIN,LEVEL):
    pass

def cadastraTurma(turma,dictTurmas):
    ch = '*'
    if turma in dictTurmas:
        print('A turma já existe')
    else:
        dictTurmas[turma] = turma
        arquivo = open(data1,'w',encoding='utf-8')
        for x in dictTurmas:
            info = x[0] + ch + x[0] + ch
            info2 = criptografaTexto(info) + '\n'
            arquivo.write(info2)
        arquivo.close()

def defineProfessor(login,user,turno,turma,dictResp,dictTurmas):
    '''
    Linka Usuários nível 3 a uma ou mais turmas
    '''
    ch = '*'
    if turma in dictTurmas:
        tupla = (turma,turno,login)
        dictResp[turma] = tupla
        arquivo = open(data2,'w',encoding='utf-8')
        for x in dictResp:
            #turma*turma*turno*login(cpf)
            info = x[0] + ch + x[0] + ch + x[1] + ch + x[2] + ch
            info2 = criptografaTexto(info) + '\n'
            arquivo.write(info2)
        arquivo.close()
    else:
        print('Turma não encontrada')

def procuraCodigo(login,user,turno,turma,dictResp,dictTurmas,codigo):
    for x in dictResp:
        if codigo == x[2]:
            x[2] == login
            defineProfessor(login,user,turno,turma,dictResp,dictTurmas)
