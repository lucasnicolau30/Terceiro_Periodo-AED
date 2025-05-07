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
        
def in_ordem(arvore): 
    if arvore is not None: 
        in_ordem(arvore['esq']) 
        print(arvore['valor'] , end = " ") 
        in_ordem(arvore['dir']) 

def pos_ordem(arvore): 
    if arvore is not None: 
        pos_ordem(arvore['esq']) 
        pos_ordem(arvore['dir']) 
        print(arvore['valor'] , end = " ") 
        
caso = eval(input()) 

contador = 1 
while caso != []: 
    arvore = cria_arvore() 
    for valor in caso: 
        arvore = insere(arvore , valor)

    print(f'Arvore {contador}') 
    print("Pre-ordem:" , end = " ") 
    pre_ordem(arvore) 
    print() 
        
    print("In-ordem:" , end = " ") 
    in_ordem(arvore) 
    print() 
        
    print("Pos-ordem:" , end = " ") 
    pos_ordem(arvore) 
    print()

    caso = eval(input()) 
    contador += 1