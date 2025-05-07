def bubble_parcial(lis, K): 
    # Escreva aqui seu Bubble Sort para ordenação parcial 
    n = len(lis) 
    for i in range(K): 
        trocou = False 
        for j in range(n - 1 , i , -1): 
            if lis[j] < lis[j - 1]: 
                lis[j] , lis[j - 1] = lis[j - 1] , lis[j] 
                trocou = True 
        if not trocou: 
            return 
            
entrada = eval(input()) 

# Enquanto essa linha não contiver a tupla vazia... 
while entrada != (): 
    # Separa o inteiro K da lista a ser ordenada 
    K, lis = entrada[0], entrada[1] 
    # Chama a função para ordenação parcial 
    bubble_parcial(lis, K) 
    # Imprime a lista parcialmente ordenada 
    print(lis) 
    # Lê a próxima linha da entrada 
    entrada = eval(input())