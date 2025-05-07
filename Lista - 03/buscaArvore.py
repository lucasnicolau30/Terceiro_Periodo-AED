def arvore_busca(arvore, chave): 
    if arvore is None: 
        return None 
    if arvore['valor'] == chave: 
        return arvore 
    elif arvore['valor'] > chave: 
        return arvore_busca(arvore['esq'] , chave) 
    else: 
        return arvore_busca(arvore['dir'] , chave) 
        
arvore = eval(input()) 
chaves = eval(input()) 

for k in chaves: 
    if arvore_busca(arvore, k): 
        print("Chave", k, "encontrada") 
    else: 
        print("Chave", k, "nao encontrada")