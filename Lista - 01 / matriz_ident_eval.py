def identidade(matriz): 
  for i in range (len(matriz)): 
    for j in range (len(matriz[0])): 
        if i == j and matriz[i][j] != 1: 
            return False 
        if i != j and matriz[i][j] != 0: 
            return False 
  return True 

matriz = eval(input()) 
if identidade(matriz): 
    print('sim') 
else: 
    print('nao')
