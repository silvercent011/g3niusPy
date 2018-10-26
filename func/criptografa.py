
texto = input('Digite texto para criptografar:')

final = ''
d = 1079
n = 1073
for x in texto:
    codigoOrd = ord(x)
    cripto = chr(codigoOrd**d%n)
    final+=cripto

arquivo = open('cripto.txt','w',encoding='utf-8')
arquivo.write(final)
arquivo.close()

    
