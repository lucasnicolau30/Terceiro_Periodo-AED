def max_heapify(heap, inicio, tamanho): 
  maior = inicio esq = 2 * inicio + 1 
  dir = 2 * inicio + 2 
  
  if esq < tamanho and heap[esq] > heap[maior]:
    maior = esq 
  if dir < tamanho and heap[dir] > heap[maior]: 
    maior = dir 
  if maior is not inicio: 
    heap[maior] , heap[inicio] = heap[inicio] , heap[maior]

entrada = eval(input()) 
while entrada != []: 
  max_heapify(entrada, 0, len(entrada)) 
  print(entrada) 
  entrada = eval(input())
