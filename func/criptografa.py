#Função terminal para cripto

def criptografaTexto(texto):
    '''
    Função recebe uma string e a retorna criptogradafa
    '''
    final = ''
    e = 71
    n = 1073
    for x in texto:
        codigoOrd = ord(x)
        cripto = codigoOrd**e%n
        info = str(cripto) + '*'
        final+=info
    
    return final

texto = input('Digite texto para criptografar:')
linha = criptografaTexto(texto) + '\n'
arquivo = open('cripto.txt','w',encoding='utf-8')
arquivo.write(linha)
arquivo.close()

    
