leitura = input() 
guarda = leitura.split() 
soma = 0 
for i in range (len(guarda)): 
  soma = soma + int(guarda[i]) 
print(soma)
