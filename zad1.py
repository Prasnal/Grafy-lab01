import networkx
import matplotlib.pyplot as plt
from funkcje import * # wierzcholki, krawedzie

wierzcholki=wierzcholki() #wywoluje funkcje z funkcje zwracajaca liste wierzcholkow
krawedzie=krawedzie() #wywoluje funkcje zwracajaca liste krawedzi
G=networkx.Graph() #tworzy graf

G.add_nodes_from(wierzcholki) #dodaje wierzcholki
G.add_edges_from(krawedzie) #dodaje krawedzie i je laczy z wierzcholkami
pos=networkx.circular_layout(G) #umieszcza na kole

for v in G.nodes():
    G.node[v]['state']=int(v) #opisuje wierzcholki

node_labels = networkx.get_node_attributes(G,'state') #przypisuje atrybuty
networkx.draw_networkx_labels(G, pos, labels = node_labels) #wypisuje opis 



networkx.draw(G, pos) #rysuje graf
plt.show() #pokazuje graf
