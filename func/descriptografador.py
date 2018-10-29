
arquivo = open('./data/log.genius','r',encoding='utf-8')

d = 1079
n = 1073
linhas = arquivo.readlines()
for x in linhas:
    texto = x.split('*')
    final = ''
    for y in texto:
        if y != '\n':
            codigoOrd = int(y)
            cripto = chr(codigoOrd**d%n)
            final+=cripto
    print(final)
    print('----------------------------------------------')

input('PRESSIONE ENTER PARA CONTINUAR')