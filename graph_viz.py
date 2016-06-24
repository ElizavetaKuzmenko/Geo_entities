# coding:utf-8

import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_gexf('cooccurrences_countries.gexf')
nodes = set()
for (u, v, c) in G.edges(data='century'):
    if c == 'XIX':
        nodes.add(u)
        nodes.add(v)
        #print('(%s, %s, %s)' % (u, v, c))
#h = G.subgraph(nodes)

nx.draw(G, node_size=30)
#nx.draw_networkx_labels(G,pos=nx.spring_layout(G),labels=G.nodes())
#plt.show()
plt.savefig("cooccurrences_countries.png")