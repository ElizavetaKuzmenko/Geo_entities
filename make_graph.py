# coding: utf-8

import json, codecs, itertools

PATH_DATA = u'/home/liza/Документы/geo/'
output_f = codecs.open('cooccurrences_countries.gexf', 'w')
output_f.write('<?xml version="1.0" encoding="UTF-8"?>\n<gexf xmlns="http://www.gexf.net/1.2draft" xmlns:xsi="' +\
               'http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.gexf.net/1.2draft ' +\
               'http://www.gexf.net/1.2draft/gexf.xsd" version="1.2">\n<meta lastmodifieddate="2016-06-25">' +\
               '\n<creator>Liza</creator>\n<description>A cooccurrences graph</description>\n</meta>')
output_f.write('<graph defaultedgetype="undirected" label="co-occurrences graph for cities and countries" mode="static">')
output_f.write('<attributes class="edge" mode="static">\n' +
               '<attribute id="0" title="author" type="string"/>\n' +\
               '<attribute id="1" title="century" type="string"/>\n</attributes>\n<nodes>')
cities_id = {}
countries_id = {}
edges_id = {}
ci_id = 0
co_id = 0
ed_id = 0
d = []
cities = []
countries = []

with open(PATH_DATA + u'file_base.json', 'r') as f:
    data = json.loads(f.read())
    n = 0
    for piece in data:
        cities_together = data[piece]['cities']
        if len(cities_together) < 2:
            continue
        cities.extend(cities_together)

        countries_together = data[piece]['countries']
        if len(countries_together) < 2:
            continue
        countries.extend(countries_together)

        author = data[piece]['author']
        century = data[piece]['century']
        d.append([countries_together, author, century])

print(len(countries), len(d))

#for city in set(cities):
#    if city not in cities_id:
#        cities_id[city] = ci_id
#        ci_id += 1
#    s = '<node id="%s" label="%s">\n<attvalues/>\n</node>' % (str(cities_id[city]), city)
#    output_f.write(s.encode('utf-8'))
#output_f.write('</nodes>\n<edges>')

for country in set(countries):
    if country not in countries_id:
        countries_id[country] = co_id
        co_id += 1
    s = '<node id="%s" label="%s">\n<attvalues/>\n</node>' % (country, country) # str(countries_id[country]))
    output_f.write(s.encode('utf-8'))
output_f.write('</nodes>\n<edges>')

for piece in d:
    #print(piece)
    for pair in itertools.combinations(piece[0],2):
        #if (pair[0], pair[1]) in edges_id:
        #    e_id = edges_id[(pair[0], pair[1])]
        #elif (pair[1], pair[0]) in edges_id:
        #    e_id = edges_id[(pair[1], pair[0])]
        #else:
        #    edges_id[(pair[0], pair[1])] = ed_id
        #    e_id = ed_id
        #    ed_id += 1
        #print pair[0], pair[1]
        s = '<edge id="%s" source="%s" target="%s">' % (str(ed_id), pair[0], pair[1]) #str(countries_id[pair[0]]), str(countries_id[pair[1]]))
        s += '<attvalues>\n<attvalue for="0" value="%s"/>\n<attvalue for="1" value="%s"/>\n</attvalues>\n</edge>' \
             % (piece[1], piece[2])
        ed_id += 1
        output_f.write(s.encode('utf-8'))


output_f.write('</edges>\n</graph>\n</gexf>')
