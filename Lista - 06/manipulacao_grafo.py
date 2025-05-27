def inicializar_grafo(num_vertices):
    return [[] for _ in range(num_vertices)]

def adicionar_aresta(grafo, u, v, w):
    def atualizar_ou_adicionar(lista, vertice, peso):
        for i, (adj, p) in enumerate(lista):
            if adj == vertice:
                lista[i] = (vertice, peso)
                return
        lista.append((vertice, peso))

    atualizar_ou_adicionar(grafo[u], v, w)
    if u != v:
        atualizar_ou_adicionar(grafo[v], u, w)

def remover_aresta(grafo, u, v):
    def remover(lista, vertice):
        for i, (adj, p) in enumerate(lista):
            if adj == vertice:
                lista.pop(i)
                return
    remover(grafo[u], v)
    if u != v:
        remover(grafo[v], u)

def consultar_aresta(grafo, u, v):
    for adjacente, peso in grafo[u]:
        if adjacente == v:
            print("%d,%d: %d" % (u, v, peso))
            return

num_caso = 0
num_vertices = int(input())

while num_vertices != 0:
    num_caso += 1
    print("Caso de teste %d" % num_caso)

    grafo = inicializar_grafo(num_vertices)

    num_arestas = int(input())
    for _ in range(num_arestas):
        u, v, w = [int(x) for x in input().split(',')]
        if w == 0:
            remover_aresta(grafo, u, v)
        else:
            adicionar_aresta(grafo, u, v, w)

    num_consultas = int(input())
    for _ in range(num_consultas):
        u, v = [int(x) for x in input().split(',')]
        consultar_aresta(grafo, u, v)

    input()  # descarta linha em branco
    num_vertices = int(input())
    print()
