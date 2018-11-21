
def bSort(lista):
    '''
    Organiza listas
    '''
    tamanho = len(lista) - 1
    suporte = False
    while suporte == False:
        cont=0
        for x in range(tamanho):
            if lista[x] > lista[x+1]:
                lista[x], lista[x+1] = lista[x+1],lista[x]
                cont+=1
        
        if cont == 0:
            suporte = True

'''
abc = [4,7,2,7,2,8,2,8,2,8,3,2]

print(abc)
recebeLista(abc)
'''