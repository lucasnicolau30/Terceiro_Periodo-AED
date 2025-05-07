def calculaPontuacao(n1 , n2 , n3): 
    return n1 + n2 + n3 - min(n1 , n2 , n3) 
    
def bubbleSort(competidores): 
    n = len(competidores) 
    for i in range(n - 1 , 0 , -1): 
        trocou = False 
        for j in range(i): 
            if (competidores[j][1] < competidores[j + 1][1]) or (competidores[j][1] == competidores[j + 1][1] and competidores[j][2] > competidores[j + 1][2]): 
                competidores[j] , competidores[j + 1] = competidores[j + 1] , competidores[j] 
                trocou = True 
        if not trocou: 
            break 
            
n = int(input()) 
competidores = [] 
for i in range(1 , n + 1): 
    leitura = eval(input()) 
    nome , n1 , n2 , n3 = leitura 
    pontuacao = calculaPontuacao(n1 , n2 , n3) 
    competidores.append((nome , pontuacao , i)) 
    
bubbleSort(competidores) 

for nome , pontuacao , _ in competidores: 
    print(f"{nome}: {pontuacao}")