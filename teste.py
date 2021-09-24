def ordenacao_bolha(lista):
    troca = True
    i = 0
    while True: # repetimos o processo len(lista) vezes
        for j in range(1, len(lista)-i):
        # a cada repetição do processo, comparamos lista[j-1] com lista[j] at ́e o final da sublista n~ao-ordenada
            if lista[j-1] > lista[j]:
                troca = True
                temp = lista[j-1]
                lista[j-1] = lista[j]
                lista[j] = temp
        i += 1
        troca = False
        
print(ordenacao_bolha([21, 60, 44, 57, 80]))