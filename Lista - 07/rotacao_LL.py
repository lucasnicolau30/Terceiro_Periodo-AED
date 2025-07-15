def altura(no): 
  return no['altura'] if no else 0 
  
def atualiza_altura(no): 
  if no: 
    no['altura'] = 1 + max(altura(no['esq']) , altura(no['dir'])) 
    
def fator_balanceamento(no): 
  return altura(no['dir']) - altura(no['esq']) if no else 0 
  
def cria_no(valor): 
  return {'valor': valor , 'esq': None , 'dir': None , 'altura' : 1} 
  
def insere(arvore , valor): 
  if arvore is None: 
    return cria_no(valor) 
  if valor < arvore['valor']: 
    arvore['esq'] = insere(arvore['esq'] , valor) 
  else: 
    arvore['dir'] = insere(arvore['dir'] , valor) 
  atualiza_altura(arvore) 
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
 
def rotacaoLL(T): 
  if T is None or T['esq'] is None: 
    return T 
  nova_raiz = T['esq'] 
  T['esq'] = nova_raiz['dir'] 
  nova_raiz['dir'] = T 
  
  atualiza_altura(T) 
  atualiza_altura(nova_raiz) 
  return nova_raiz 
  
contador = 1 
caso = eval(input()) 

while caso != []: 
  arvore = None 
  for valor in caso: 
    arvore = insere(arvore , valor) 
    
  if arvore is not None and arvore['esq'] is not None: 
    arvore = rotacaoLL(arvore) 
  
  atualiza_altura(arvore) 
  
  print(f'Arvore {contador}') 
  print(f'h: {altura(arvore)}') 
  print(f'fb: {fator_balanceamento(arvore)}') 
  
  print("pre:" , end = " ") 
  pre_ordem(arvore) 
  print() 
  
  print("pos:" , end = " ") 
  pos_ordem(arvore) 
  print() 
  
  caso = eval(input()) 
  contador += 1
