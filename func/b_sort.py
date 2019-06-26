
def bSort(lista):
    '''
    Organiza listas pelo método Bubble Sort
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

def bSortIndex(lista,index):
    '''
    Organiza listas pelo método Bubble Sort usando o index como parâmetro
    ** Recomendado para listas de tuplas
    '''
    tamanho = len(lista) - 1
    suporte = False
    while suporte == False:
        cont=0
        for x in range(tamanho):
            if lista[x][index] > lista[x+1][index]:
                lista[x], lista[x+1] = lista[x+1],lista[x]
                cont+=1
        
        if cont == 0:
            suporte = True
