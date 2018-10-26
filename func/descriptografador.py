
arquivo = open('./data/users.genius','r',encoding='utf-8')

d = 1079
n = 1073
for texto in arquivo:
    final = ''
    print('----------------------------------------------')
    for x in texto:
        codigoOrd = ord(x)
        cripto = chr(codigoOrd**d%n)
        final+=cripto
    print(final)
    print('----------------------------------------------')

input('PRESSIONE ENTER PARA CONTINUAR')