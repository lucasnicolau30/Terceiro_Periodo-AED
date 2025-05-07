def imprime_bubble(lista): 
    n = len(lista) 
    for i in range (n - 1 , 0 , -1): 
        trocou = False 
        for j in range(i): 
            if lista[j] > lista[j + 1]: 
                print(f"{lista[j]} <-> {lista[j + 1]}") 
                lista[j] , lista[j + 1] = lista[j + 1] , lista[j] 
                trocou = True 
            if not trocou: 
                break 
                
    print(lista) 
            
leitura = input() 
lista = eval(leitura) 
imprime_bubble(lista)