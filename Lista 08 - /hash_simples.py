tam = int(input()) 
qnt = int(input())  

tabela = [None] * tam

for _ in range(qnt):
    num = int(input())
    i = 0
    while True:
        pos = (num + i) % tam
        if tabela[pos] is None:
            tabela[pos] = num
            break
        i += 1

for i in range(tam):
    if tabela[i] is not None:
        print("%d: %d" % (i, tabela[i]))
