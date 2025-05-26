class Par: 
  def __init__(self, chave, valor): 
    self.chave = chave 
    self.valor = valor 

  def __lt__(self, other): 
    return self.chave < other.chave 

  def __repr__(self): 
    return str(self.valor) 
  
def merge_sort(vetor , inicio, fim): 
  if inicio < fim: 
    meio = (inicio + fim) // 2 
    esquerda = merge_sort(vetor, inicio, meio) 
    direita = merge_sort(vetor, meio + 1, fim) 
    vet = intercala(esquerda, direita) 
    return vet 
  return [vetor[inicio]] 

def intercala(vetorEsq, vetorDir): 
  i, j = 0, 0 
  vet = [] 
  for k in range (len(vetorEsq) + len(vetorDir)): 
    if j < len(vetorDir) and (len(vetorEsq) <= i or vetorDir[j] < vetorEsq[i]): 
      vet.append(vetorDir[j]) 
      j += 1 
    else: 
      vet.append(vetorEsq[i]) 
      i += 1 
  return vet 
  
caso = eval(input()) 
j = 1 
while caso != []: 
  vet = [] 
  for chave , valor in caso: 
    vet.append(Par(chave, valor)) 
    
  inicio = 0 fim = len(vet) - 1 
  vet = merge_sort(vet, inicio, fim) 
  print(f'Caso {j}') 
  for i in range (len(vet)): 
    print(vet[i]) 
  print() 
  j = j + 1 
  caso = eval(input())
