# coding:utf-8

import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_gexf('cooccurrences_cities.gexf')
nodes = set()
for (u, v, c) in G.edges(data='century'):
    if c == 'XIX':
        nodes.add(u)
        nodes.add(v)
        #print('(%s, %s, %s)' % (u, v, c))
h = G.subgraph(nodes)
git
nx.draw(h, node_size=30)
#nx.draw_networkx_labels(G,pos=nx.spring_layout(G),labels=G.nodes())
plt.show()
plt.savefig("cities_XIX.png")