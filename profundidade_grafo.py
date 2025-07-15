def inicializar_grafo(num_vertices):
    return [[] for _ in range(num_vertices)]

def adicionar_aresta(grafo, u, v):
    grafo[u].append(v)

def dfs(grafo, origem):
    visitados = set()

    def visitar(v):
        visitados.add(v)
        for vizinho in grafo[v]:
            if vizinho not in visitados:
                visitar(vizinho)

    visitar(origem)
    return visitados

num_caso = 0
num_vertices = int(input())

while num_vertices != 0:
    num_caso += 1
    print("Caso de teste %d" % num_caso)

    grafo = inicializar_grafo(num_vertices)


    arestas = eval(input())
    for u, v in arestas:
        adicionar_aresta(grafo, u, v)

    for i in range(num_vertices):
        visitados = dfs(grafo, i)
        print("%d: %d" % (i, len(visitados) - 1)) 

    num_vertices = int(input())
    print()
