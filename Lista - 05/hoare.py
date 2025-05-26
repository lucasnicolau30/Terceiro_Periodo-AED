class Par: 
  def __init__(self, chave, valor): 
    self.chave = chave 
    self.valor = valor 

  def __lt__(self, other): 
    return self.chave < other.chave 

  def __repr__(self): 
    return str(self.valor) 

def hoare(lis): 
  meio = (len(lis) - 1) // 2 
  pivo = lis[meio] 
  i , j = -1 , len(lis) 
  
  while True: 
    i = i + 1

    while lis[i] < pivo: 
      i = i + 1 
      j = j - 1 
      
    while lis[j] > pivo: 
      j = j - 1
      
      if i >= j: 
        return j 
      else: 
        lis[i] , lis[j] = lis[j] , lis[i]

caso = eval(input()) 
j = 1 
while caso != []: 
  vet = [] 
  for chave , valor in caso: 
    vet.append(Par(chave, valor)) 
    
corte = hoare(vet) 
print(f'Caso {j}') 
print('esq:' , end = ' ') 
for i in range (corte + 1): 
  print(vet[i] , end = ' ') 
print() 

i = corte + 1 
print('dir:' , end = ' ') 
for i in range (i , len(vet)): 
  print(vet[i] , end = ' ') 
print() 

j = j + 1 
caso = eval(input())
