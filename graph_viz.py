# coding:utf-8

import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_gexf('cooccurrences_countries.gexf')
nodes = set()
for (u, v, c) in G.edges(data='decade'):
    if c == '1820':
        nodes.add(u)
        nodes.add(v)
        #print('(%s, %s, %s)' % (u, v, c))
h = G.subgraph(nodes)

#betweenness = nx.betweenness_centrality(G)
#bil = betweenness.items()
#bil.sort(key=lambda x:x[1],reverse=True)
#print(bil[2][0])

#nx.draw(G, node_size=30)
#nx.draw_networkx_labels(G,pos=nx.spring_layout(G),labels=G.nodes())
#G = h
pos=nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color='grey', node_size=5)
nx.draw_networkx_edges(G, pos, width=0.6)
nx.draw_networkx_edges(G, pos, edge_color='#dd99ff')
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
#plt.axis('off')
#plt.title(u"Заголовок")
plt.show()
#plt.savefig("1820.png")