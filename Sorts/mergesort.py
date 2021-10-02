def mergeSort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2  # separando a lista da esquerda e da direita
        l_E = lista[:meio]
        l_D = lista[meio:]
        print("Separando:", l_E, "-----", l_D)
        mergeSort(l_E)
        mergeSort(l_D)
        i = 0
        j = 0
        k = 0

        while i < len(l_E) and j < len(l_D):
            print("Comparando: ", l_E[i], " < ", l_D[j])
            if l_E[i] < l_D[j]:
                print("Coloca: ", l_E[i], "na posição", k, "da lista ", lista)
                lista[k] = l_E[i]
                i += 1
            else:
                print("Coloca ", l_D[j], "na posicao ", k, "da lista ", lista)
                lista[k] = l_D[j]
                j += 1
            k += 1

        while i < len(l_E):
            print("Substituindo. Coloca ", l_E[i], "na posicao ", k, " da lista", lista)
            lista[k] = l_E[i]
            i += 1
            k += 1
            print("Resulta em ", lista)

        while j < len(l_D):
            print("Substituindo o maior elemento na posicao correta. Coloca ", l_D[j], "na posicao ", k, " da lista",
                  lista)
            lista[k] = l_D[j]
            j += 1
            k += 1
            print("Resulta em ", lista)


lista = [25, 9, 18, 10, 5, 7, 15, 3]
print(lista)
mergeSort(lista)
print(lista)
