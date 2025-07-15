tam = int(input()) 
qnt = int(input())  

tabela = [None] * tam

def f(c):
    if c == '-':
        return 0
    return ord(c) - ord('a') + 1

for _ in range(qnt):
    chave = input().strip()
    h = sum(f(c) for c in chave) % tam

    i = 0
    while True:
        pos = (h + i) % tam
        if tabela[pos] is None:
            tabela[pos] = chave
            break
        i += 1

for i in range(tam):
    if tabela[i] is not None:
        print("%d: %s" % (i, tabela[i]))
