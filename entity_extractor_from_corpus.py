#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 2015-11-01

import json, codecs, re, os


st = codecs.open('stoplist', 'r', 'utf-8')
stp = st.read()
stopwords = stp.split('\n')
st.close()

stoplist = [u'чад', u'панама', u'того']
stoplist.extend(stopwords)

def entity_clean_up(ent):
    clean = []
    for e in ent:
        if ' ' not in e:
            e = e.strip()
            e = e.lower()
            if e in stoplist:
                continue
            clean.append(e)
    #return set(clean)
    return clean

def fileparse(f, cities, countries):
    found_cities = []
    found_countries = []
    for line in f:
        if '<meta content="' in line:
            if 'name="created"' in line or 'name="date"' in line:
                res = re.search(u'<meta content="(.+?)"', line)
                if res:
                    raw_date = res.group(1)
                    resd = re.search(u'([0-9]{4})', raw_date)
                    if resd:
                        date = resd.group(1)
                    elif '19??' in raw_date:
                        date = '19??'
                    elif '18??' in raw_date:
                        date = '18??'
            if 'name="author"' in line:
                res = re.search(u'<meta content="(.+?)"', line)
                if res:
                    author = res.group(1)
        if u'<line meter="' in line:
            lemmas = re.findall(u'\{(.+?)\}', line)
            for lemma in lemmas:
                if lemma in cities:
                    found_cities.append(lemma)
                if lemma in countries:
                    found_countries.append(lemma)
                    
    return (date, author, list(set(found_cities)), list(set(found_countries)))
                        

def date_extr(year):
    if '?' in year:
        if '19' in year:
            return 'XX', 0
        elif '18' in year:
            return 'XIX', 0
    else:
        decade = year[:-1] + '0'
    if year.startswith('17'):
        century = 'XVIII'
    elif year.startswith('18'):
        century = 'XIX'
    elif year.startswith('19'):
        century = 'XX'
    elif year.startswith('20'):
        century = 'XXI'
    return century, decade
        

def main():
    js = open('all.json')
    geodict = json.load(js)
    js.close()
    cities = entity_clean_up(geodict[u'Населенные пункты'])
    countries = entity_clean_up(geodict[u'Государства'])
    
    cities.append(u'емен')
    countries = set(countries)
    
    cities.extend([u'петербург', u'петроград', u'ленинград'])
    cities.extend([u'царьград', u'константинополь'])
    cities.append(u'ревель')
    cities.append(u'дерпт')
    cities = set(cities)
    
    geopoetics = {
    'countries': {'all': {}, 'decades': {}, 'centuries': {}, 'authors': {}},
    'cities': {'all': {}, 'decades': {}, 'centuries': {}, 'authors': {}}
    }
    base = {}
    
    authors = []
    
    for root, dirs, files in os.walk('/home/boris/Work/poetic/lemmed_poetic_corpus'):
        for fl in files:
            print root + os.sep + fl
            f = codecs.open(root + os.sep + fl, 'r', 'utf-8')
            filedata = fileparse(f, cities, countries)
            authors.append(filedata[1])
            century, decade = date_extr(filedata[0])
            path = root.replace('/home/boris/Work/poetic/lemmed_poetic_corpus', '')
            path = path + os.sep + fl
            base[path] = {'decade': decade, 'century': century, 'cities': filedata[2], 'countries': filedata[3], 'author': filedata[1]}
            for city in filedata[2]:
                if city in [u'петербург', u'петроград', u'ленинград']:
                    city = u'санкт-петербург'
                if city in [u'царьград', u'константинополь']:
                    city = u'стамбул'
                if city == u'ревель':
                    city = u'таллин'
                if city == u'дерпт':
                    city = u'тарту'
                if city in geopoetics['cities']['all']:
                    geopoetics['cities']['all'][city] += 1
                else:
                    geopoetics['cities']['all'][city] = 1
                
                if decade in geopoetics['cities']['decades']:
                    if city in geopoetics['cities']['decades'][decade]:
                        geopoetics['cities']['decades'][decade][city] += 1
                    else:
                        geopoetics['cities']['decades'][decade][city] = 1
                else:
                    geopoetics['cities']['decades'][decade] = {city: 1}
                    
                if filedata[1] in geopoetics['cities']['authors']:
                    if city in geopoetics['cities']['authors'][filedata[1]]:
                        geopoetics['cities']['authors'][filedata[1]][city] += 1
                    else:
                        geopoetics['cities']['authors'][filedata[1]][city] = 1
                else:
                    geopoetics['cities']['authors'][filedata[1]] = {city: 1}
                    
                if century in geopoetics['cities']['centuries']:
                    if city in geopoetics['cities']['centuries'][century]:
                        geopoetics['cities']['centuries'][century][city] += 1
                    else:
                        geopoetics['cities']['centuries'][century][city] = 1
                else:
                    geopoetics['cities']['centuries'][century] = {city: 1}

            for country in filedata[3]:
                if country == u'емен':
                    country = u'йемен'
                if country in geopoetics['countries']['all']:
                    geopoetics['countries']['all'][country] += 1
                else:
                    geopoetics['countries']['all'][country] = 1
                
                if decade in geopoetics['countries']['decades']:
                    if country in geopoetics['countries']['decades'][decade]:
                        geopoetics['countries']['decades'][decade][country] += 1
                    else:
                        geopoetics['countries']['decades'][decade][country] = 1
                else:
                    geopoetics['countries']['decades'][decade] = {country: 1}
                    
                if filedata[1] in geopoetics['countries']['authors']:
                    if country in geopoetics['countries']['authors'][filedata[1]]:
                        geopoetics['countries']['authors'][filedata[1]][country] += 1
                    else:
                        geopoetics['countries']['authors'][filedata[1]][country] = 1
                else:
                    geopoetics['countries']['authors'][filedata[1]] = {country: 1}
                    
                if century in geopoetics['countries']['centuries']:
                    if country in geopoetics['countries']['centuries'][century]:
                        geopoetics['countries']['centuries'][century][country] += 1
                    else:
                        geopoetics['countries']['centuries'][century][country] = 1
                else:
                    geopoetics['countries']['centuries'][century] = {country: 1}
    
    countries_poet = geopoetics['countries']['all']
    cities_poet = geopoetics['cities']['all']
    
    fw = codecs.open('/home/boris/Work/poetic/geo/Geo_entities/countries.csv', 'w', 'utf-8')
    for word in sorted(countries_poet, key=countries_poet.get, reverse=True):
        fw.write(word + '\t' + str(countries_poet[word]) + '\n')
    fw.close()
    
    fw = codecs.open('/home/boris/Work/poetic/geo/Geo_entities/cities.csv', 'w', 'utf-8')
    for word in sorted(cities_poet, key=cities_poet.get, reverse=True):
        fw.write(word + '\t' + str(cities_poet[word]) + '\n')
    fw.close()
                
    fj = codecs.open('/home/boris/Work/poetic/geo/file_base.json', 'w', 'utf-8')
    json.dump(base, fj, sort_keys=True, indent=4, ensure_ascii=False)
    fj.close()
            
    fj = codecs.open('/home/boris/Work/poetic/geo/cities.json', 'w', 'utf-8')
    json.dump(geopoetics['cities'], fj, sort_keys=True, indent=4, ensure_ascii=False)
    fj.close()
    
    fj = codecs.open('/home/boris/Work/poetic/geo/countries.json', 'w', 'utf-8')
    json.dump(geopoetics['countries'], fj, sort_keys=True, indent=4, ensure_ascii=False)
    fj.close()
    
    authors = list(set(authors))
    authors.sort()
    fw = codecs.open('authors.csv', 'w', 'utf-8')
    author = '\n'.join(authors)
    fw.write(author)
    fw.close()
    
    
    return 0

if __name__ == '__main__':
    main()

