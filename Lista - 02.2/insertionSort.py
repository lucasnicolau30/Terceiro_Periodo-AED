def imprime_insertion(lista): 
    print(lista) 
    n = len(lista) 
    for i in range(1 , n): 
        prox = lista[i] 
        j = i - 1 
        while j >= 0 and lista[j] > prox: 
            if lista[j + 1] != lista[j]: 
                lista[j + 1] = lista[j] 
                print(lista) 
            j-= 1 
        if lista[j + 1] != prox: 
            lista[j + 1] = prox 
            print(lista) 
                
leitura = input() 
lista = eval(leitura) 
imprime_insertion(lista)