class Par: 
  def __init__(self, chave, valor): 
    self.chave = chave 
    self.valor = valor 

  def __lt__(self, other): 
    return self.chave < other.chave 

  def __repr__(self): 
    return str(self.valor)

def hoare(lis , inicio, fim): 
  meio = (inicio + fim) // 2 
  pivo = lis[meio] 
  i = inicio - 1 
  j = fim + 1 
  
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
          
def quick_sort(lis, inicio, fim): 
  if inicio < fim: 
    pivo = hoare(lis, inicio, fim) 
    quick_sort(lis, inicio, pivo) 
    quick_sort(lis, pivo + 1, fim) 
    
caso = eval(input()) 
j = 1 
while caso != []: 
  vet = []
  
for chave , valor in caso: 
  vet.append(Par(chave, valor)) 
  
  quick_sort(vet , 0 , len(vet) - 1) 
  
  print(f'Caso {j}') 
  for item in vet: 
    print(f'{item.chave} {item.valor}') 
  print() 
  
  j = j + 1 
  caso = eval(input())
