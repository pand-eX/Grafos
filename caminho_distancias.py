from igraph import Graph
from igraph import plot

#supondo e q um mapa e cada ponto e um local e os pesos estão nas aresta são a distâncias.
# Criação de grafo direcionado com pesos entre as arestas
grafo = Graph(edges = [(0,2),(0,1),(1,4),(1,5),(2,3),(6,7),(3,7),(4,7),(5,6)],
                                directed = True)
grafo.vs["label"] = ["A", "B", "C", "D", "E", "F", "G", "H"]
grafo.es["weight"] = [2,1,2,1,2,1,3,1]

# Visualização do grafo com os pesos
plot(grafo, bbox = (0,0,300,300), edge_label = grafo.es["weight"])

# Caminho entre os vértices A - H
caminho_vertice = grafo.get_shortest_paths(0,7, output = 'vpath')#consiga o caminho mais curto e retorno os vértices
for n in caminho_vertice[0]:
    print(grafo.vs[n]['label'])#impressão dos resultado atraves de label

# Obtenção dos caminhos mais curtos entre 0 e 7
caminho_aresta = grafo.get_shortest_paths(0,7, output = 'epath')
caminho_aresta

# Mostrar o caminho 
caminho_aresta_id = []
for n in caminho_aresta[0]:
    caminho_aresta_id.append(n)
caminho_aresta_id

# Somatório dos pesos (ou distâncias) entre os vértices do caminho
distancia = 0
for e in grafo.es:
    #print(e.index)
    if e.index in caminho_aresta_id:
        distancia += grafo.es[e.index]['weight']
distancia        

