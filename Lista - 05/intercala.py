lista1 = eval(input()) 
lista2 = eval(input()) 

tamanho3 = len(lista1) + len(lista2) 
lista3 = [0] * tamanho3 

i, j = 0, 0 
for k in range (tamanho3): 
    if i < len(lista1) and (j >= len(lista2) or lista1[i] <= lista2[j]): 
        lista3[k] = lista1[i] 
        i += 1 
    elif j < len(lista2) and (i >= len(lista1) or lista1[i] > lista2[j]): 
        lista3[k] = lista2[j] 
        j += 1 

print(lista3)
