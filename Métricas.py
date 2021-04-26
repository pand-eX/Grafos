from igraph import Graph
from igraph import plot
import igraph

# Carregamento de grafo no formato graphml
grafo = igraph.load("Grafo.graphml")
print(grafo)


#visualizar
plot(grafo, bbox = (0,0,600,600))
# Visualização do grau de entrada, saída e entrada + saída do grafo
grafo.degree(mode = 'all')
grafo.degree(mode = 'in')
grafo.degree(mode = 'out')

# Obtendo e imprimindo somente os graus de entrada
grau = grafo.degree(mode = 'in')
print(grau)

#gerando o grafo com vertice proporcional ao grau
plot(grafo, vertex_size = grau ,bbox = (0,0,600,600))

# Retorno do diâmetro do grafo (maior distância entre os vértices)
grafo.diameter(directed = True)

# Retorno dos vértices que possuem a maior distância entre os pontos do grafo
grafo.get_diameter()

# Retorno dos vizinhos de cada vértice
grafo.neighborhood()

# Verificar se o grafo é isomórfico
grafo2 = grafo
grafo.isomorphic(grafo2)