def altura(no): 
  return no['altura'] if no else 0 
  
def atualiza_altura(no): 
  if no: 
    no['altura'] = 1 + max(altura(no['esq']) , altura(no['dir'])) 
    
def fator_balanceamento(no): 
  return altura(no['dir']) - altura(no['esq']) if no else 0 
  
def cria_no(valor): 
  return {'valor': valor , 'esq': None , 'dir': None , 'altura' : 1} 
  
def rotacaoLL(z): 
  if z is None: 
    return None 
  y = z['esq'] 
  if y is None: 
    return z 
  z['esq'] = y['dir'] 
  y['dir'] = z 
  atualiza_altura(z) 
  atualiza_altura(y) 
  return y

def rotacaoRR(z): 
  if z is None: 
    return None 
  y = z['dir'] 
  if y is None: 
    return z 
  z['dir'] = y['esq'] 
  y['esq'] = z 
  atualiza_altura(z) 
  atualiza_altura(y) 
  return y 
  
def rotacaoLR(z): 
  if z is None: 
    return None 
  z['esq'] = rotacaoRR(z['esq']) 
  return rotacaoLL(z) 
  
def rotacaoRL(z): 
  if z is None: 
    return None 
  z['dir'] = rotacaoLL(z['dir']) 
  return rotacaoRR(z) 
  
def balanceia(no): 
  atualiza_altura(no) 
  fb = fator_balanceamento(no) 
  if fb < -1: 
    if fator_balanceamento(no['esq']) <= 0: 
      return rotacaoLL(no) 
    else: 
      return rotacaoLR(no) 
  elif fb > 1: 
    if fator_balanceamento(no['dir']) >= 0: 
      return rotacaoRR(no) 
    else: 
      return rotacaoRL(no) 
  return no 
  
def insere(arvore , valor): 
  if arvore is None: 
    return cria_no(valor) 
  if valor < arvore['valor']: 
    arvore['esq'] = insere(arvore['esq'] , valor) 
  else: 
    arvore['dir'] = insere(arvore['dir'] , valor) 
  return balanceia(arvore) 
  
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
    
contador = 1 
caso = eval(input()) 

while caso != []: 
  arvore = None 
  for valor in caso: 
    arvore = insere(arvore , valor)
    
  print(f'Arvore {contador}') 
  
  print("pre:" , end = " ") 
  pre_ordem(arvore) 
  print() 
  
  print("pos:" , end = " ") 
  pos_ordem(arvore) 
  print() 
  
  caso = eval(input()) 
  contador += 1
