def cria_arvore(): 
    return None 
    
def cria_no(valor): 
    return {'valor': valor, 'esq': None, 'dir': None} 
    
def insere(arvore, valor): 
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

def sucessor_em_ordem(arvore): 
    arvore = arvore['dir'] 
    while arvore and arvore['esq'] is not None: 
        arvore = arvore['esq'] 
    return arvore 

def remove(arvore , valor): 
    if arvore is None: 
        return None 
    if valor < arvore['valor']: 
        arvore['esq'] = remove(arvore['esq'] , valor) 
    elif valor > arvore['valor']: 
        arvore['dir'] = remove(arvore['dir'] , valor) 
    else: 
        if arvore['esq'] is None: 
            return arvore['dir'] 
        elif arvore['dir'] is None: 
            return arvore['esq'] 
        else: 
            sucessor = sucessor_em_ordem(arvore) 
            arvore['valor'] = sucessor['valor'] 
            arvore['dir'] = remove(arvore['dir'] , sucessor['valor']) 
    return arvore 
    
caso = eval(input()) 
chaves = eval(input()) 

arvore = cria_arvore() 
for valor in caso: 
    arvore = insere(arvore , valor) 

print("Arvore inicial: " , end = "") 
pre_ordem(arvore) 
print() 

for valor in chaves: 
    arvore = remove(arvore , valor) 
    print(f'Depois de remover {valor}: ' , end = "")

    if arvore is None: 
        print('vazia!') 
    else: 
        pre_ordem(arvore) 
        print()