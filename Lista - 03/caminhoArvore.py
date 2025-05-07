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
        
arvore = eval(input()) 

print("Pre-ordem:" , end = " ")     
pre_ordem(arvore) 
print() 
        
print("In-ordem:" , end = " ") 
in_ordem(arvore)     
print() 
        
print("Pos-ordem:" , end = " ") 
pos_ordem(arvore) 
print()