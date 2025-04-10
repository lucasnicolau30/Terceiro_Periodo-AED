leitura = int(input()) 
maior = leitura 
menor = leitura 

for i in range (4): 
  leitura = int(input()) 
  if leitura > maior: 
    maior = leitura 
  if leitura < menor:
    menor = leitura
print(menor , maior)
