# coding: utf-8

import codecs
import urllib2
import urllib
import re

fw = codecs.open('cities_latlon3.csv', 'w', 'utf-8')
fw.write(u'"","City","lon","lat"\n')

i = 0

f = codecs.open('cities.csv', 'r', 'utf-8')
for line in f:
    i += 1
    line = line.strip()
    city, freq = line.split()
    print str(i) + '. ' + city
    if i < 371:
        continue
    city_web = city.capitalize()
    if '-' in city_web:
        parts = city_web.split('-')
        for indx, part in enumerate(parts):
            parts[indx] = part.capitalize()
            if part == u'на':
                parts[indx] = u'на'
        city_web = '-'.join(parts)
    url = u'https://ru.wikipedia.org/wiki/' + city_web
    page = urllib.urlopen(url.encode("UTF-8")).read()
    res = re.search(u'href="//(tools.+?)">', page)
    link = res.group(1)
    link = link.replace('&amp;', '&')
    link = 'https://' + link 
    p = urllib2.urlopen(link)
    page = p.read().decode('utf-8')
    p.close()
    
    resl = re.search(u'span class="latitude" title="Широта">(.+?)</span>', page)
    lat = resl.group(1)
    
    resl = re.search(u'span class="longitude" title="Долгота">(.+?)</span>', page)
    lon = resl.group(1)
    
    latlon = lon + ',' + lat

    print (latlon)

    string = u'"' + unicode(i) + u'","' + city + u'",' + latlon + '\n'
    fw.write(string)

f.close()
fw.close()
