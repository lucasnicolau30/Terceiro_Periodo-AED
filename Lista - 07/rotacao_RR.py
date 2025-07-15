def cria_arvore(): 
  return None 
  
def cria_no(valor): 
  return {'valor': valor , 'esq': None , 'dir': None} 
  
def insere(arvore , valor): 
  if arvore is None: 
    return cria_no(valor) 
  if valor < arvore['valor']: 
    arvore['esq'] = insere(arvore['esq'] , valor) 
  else: 
    arvore['dir'] = insere(arvore['dir'] , valor) 
  return arvore 
  
def pre_ordem(arvore): 
  if arvore is not None: 
    print(arvore['valor'] , end = " ") 
    pre_ordem(arvore['esq']) 
    pre_ordem(arvore['dir']) 
    
def pos_ordem(arvore): 
  if arvore is not None: 
    pos_ordem(arvore['esq']) 
    pos_ordem(arvore['dir']) 
    print(arvore['valor'] , end = " ") 
    
def rotacaoRR(T): 
  if T is None or T['dir'] is None: 
    return T 
  nova_raiz = T['dir'] 
  T['dir'] = nova_raiz['esq']
  nova_raiz['esq'] = T 
  return nova_raiz 
  
contador = 1 
caso = eval(input()) 

while caso != []: 
  arvore = cria_arvore() 
  for valor in caso: 
    arvore = insere(arvore , valor) 
    
  arvore = rotacaoRR(arvore) 
  
  print(f'Arvore {contador}') 
  print("pre:" , end = " ") 
  pre_ordem(arvore) 
  print() 
  
  print("pos:" , end = " ") 
  pos_ordem(arvore) 
  print() 
  
  caso = eval(input()) 
  contador += 1
