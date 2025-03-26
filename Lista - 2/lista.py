num = input() 
lista = num.split() 
inicio = int(lista[0]) 
fim = int(lista[1]) 
contaTamanho = 0 
for i in range(inicio , fim + 1): 
    contaTamanho = contaTamanho + 1 
    
lista = [0] * contaTamanho 

j = 0 
for i in range(inicio , fim + 1): 
    lista[j] = i 
    j = j + 1 
    
print(lista)