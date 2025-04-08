def selection_sort(lista):
    n = len(lista)

    for i in range(n):
        menor_indice = i
        for j in range(i + 1 , n):
            if lista[menor_indice] > lista[j]:
                menor_indice = j
        lista[i] , lista[menor_indice] = lista[menor_indice] , lista[i]

lista = [12, 1, 2, 3, 4, 5, 7, 6, 8, 9, 11, 10]	    
selection_sort(lista)
print(lista)