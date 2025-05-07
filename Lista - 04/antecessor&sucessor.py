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

def arvore_busca(arvore, chave): 
    if arvore is None: 
        return None 
    if arvore['valor'] == chave: 
        return arvore 
    elif arvore['valor'] > chave: 
        return arvore_busca(arvore['esq'] , chave) 
    else: 
        return arvore_busca(arvore['dir'] , chave) 

def busca_antecessor_sucessor(arvore , chave): 
    arvore = arvore_busca(arvore, chave) 
    
    if arvore is None: 
        return None , None 
    if chave < arvore['valor']: 
        arvore['esq'] = busca_antecessor_sucessor(arvore['esq'] , chave) 
    elif chave > arvore['valor']: 
        arvore['dir'] = busca_antecessor_sucessor(arvore['dir'] , chave) 
    else: 
        antecessor = None 
        sucessor = None 
        
        if arvore['esq']: 
            antecessor = arvore['esq'] 
            while antecessor and antecessor['dir'] is not None: 
                antecessor = antecessor['dir'] 
        
        if arvore['dir']: 
            sucessor = arvore['dir'] 
            while sucessor and sucessor['esq'] is not None: 
                sucessor = sucessor['esq'] 
                
    return antecessor , sucessor 
    
caso = eval(input()) 
chaves = eval(input()) 

arvore = cria_arvore() 
for valor in caso: 
    arvore = insere(arvore , valor) 
    
for chave in chaves: 
    antecessor , sucessor = busca_antecessor_sucessor(arvore , chave) 
    antecessor_valor = antecessor['valor'] if antecessor else None 
    sucessor_valor = sucessor['valor'] if sucessor else None 
    print(f'Chave {chave} tem antecessor {antecessor_valor} e sucessor {sucessor_valor}')