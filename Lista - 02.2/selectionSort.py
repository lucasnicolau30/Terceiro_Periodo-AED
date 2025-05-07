def imprime_selection(lista): 
    n = len(lista) 
    for i in range (n): 
        menor_indice = i 
        for j in range(i + 1 , n): 
            if lista[menor_indice] > lista[j]: 
                menor_indice = j 
            if menor_indice != i:
                print(f"{lista[i]} <-> {lista[menor_indice]}") 
                lista[i] , lista[menor_indice] = lista[menor_indice] , lista[i] 
                
    print(lista) 
    
leitura = input() 
lista = eval(leitura) 
imprime_selection(lista)