def max_heapify(heap, inicio, tamanho): 
  maior = inicio esq = 2 * inicio + 1 
  dir = 2 * inicio + 2 
  
  if esq < tamanho and heap[esq] > heap[maior]: 
    maior = esq 
  if dir < tamanho and heap[dir] > heap[maior]: 
    maior = dir 
  if maior is not inicio: 
    heap[maior] , heap[inicio] = heap[inicio] , heap[maior] 
    max_heapify(heap, maior, tamanho) 
    
def heap_sort(heap): 
  tamanho = len(heap) 
  monta_heap(heap, tamanho) 
  
  while tamanho > 1:
    heap[0], heap[tamanho - 1] = heap[tamanho - 1], heap[0] 
    tamanho -=1 
    max_heapify(heap, 0, tamanho) 
    
def monta_heap(heap, tamanho): 
  primeiro_com_filho = (tamanho // 2) - 1 
  for i in range(primeiro_com_filho, -1, -1): 
    max_heapify(heap, i, tamanho) 
    
entrada = eval(input()) 
while entrada != []: 
  heap_sort(entrada) 
  print(entrada) 
  entrada = eval(input())
