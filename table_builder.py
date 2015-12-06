#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  table_builder.py
#  
# относительное число текстов с городами, с крупными городами

#dependency: pip install transliterate

import codecs, json
#import rpy2.robjects as robjects
from math import log10
from transliterate import translit, get_available_language_codes

thead = '"","City","Freq","lon","lat"\n'

def extractor(type_entity, cities_latlon, countries_latlon):
    f = codecs.open('../' + type_entity +'.json', 'r', 'utf-8')
    data = json.load(f)
    f.close()
    all_time = data['all']
    
    big_cities = []
    
    f = codecs.open('../prepared_data/' + type_entity + '_all_abs.csv', 'w', 'utf-8')
    f.write(thead)
    i = 1
    for item in sorted(all_time, key=all_time.get, reverse=True):
        if item in cities_latlon:
            latlon_val = cities_latlon[item]
        elif item in countries_latlon:
            latlon_val = countries_latlon[item]
        else:
            latlon_val = 'NA,NA'
        f.write('"' + str(i) + '","' + item + '",' + str(all_time[item]) + ',' + latlon_val + '\n')
        if type_entity == 'cities' and i < 11:
            big_cities.append(item)
        i += 1
    f.close()
    
    f = codecs.open('../prepared_data/' + type_entity + '_all_log.csv', 'w', 'utf-8')
    f.write(thead)
    i = 1
    for item in sorted(all_time, key=all_time.get, reverse=True):
        if item in cities_latlon:
            latlon_val = cities_latlon[item]
        elif item in countries_latlon:
            latlon_val = countries_latlon[item]
        else:
            latlon_val = 'NA,NA'
        f.write('"' + str(i) + '","' + item + '",' + str(log10(int(all_time[item])) + 1) + ',' + latlon_val + '\n')
        i += 1
    f.close()
    
    separated_data(data, type_entity, cities_latlon, countries_latlon)
    
    if type_entity == 'cities':
        big_cities_detalized(big_cities, data['decades'])
            
def big_cities_detalized(big_cities, data):
    f = codecs.open('../prepared_data/big_cities_abs.R', 'w', 'utf-8')
    for city in big_cities:
        city_decade = []
        for decade in sorted(data):
            if city in data[decade]:
                city_decade.append(str(data[decade][city]))
            else:
                city_decade.append('0')
        city_name = translit(city, 'ru', reversed=True)
        f.write(city_name + ' <- c(' + ','.join(city_decade) + ')\n')
    f.close()
    
def separated_data(data, type_entity, cities_latlon, countries_latlon):
    ents = ['centuries', 'decades', 'authors']
    for key in ents:
        dic = data[key]
        for cert in dic:
            order = dic[cert]
            #cert = cert.replace(' ', '')
            f = codecs.open('../prepared_data/' + type_entity + '_' + key + '_abs/' + cert + '.csv', 'w', 'utf-8')
            f.write(thead)
            i = 1
            for item in sorted(order, key=order.get, reverse=True):
                if item in cities_latlon:
                    latlon_val = cities_latlon[item]
                elif item in countries_latlon:
                    latlon_val = countries_latlon[item]
                else:
                    latlon_val = 'NA,NA'
                f.write('"' + str(i) + '","' + item + '",' + str(order[item]) + ',' + latlon_val + '\n')
                i += 1
            f.close()
            
            f = codecs.open('../prepared_data/' + type_entity + '_' + key + '_log/' + cert + '.csv', 'w', 'utf-8')
            f.write(thead)
            i = 1
            for item in sorted(order, key=order.get, reverse=True):
                if item in cities_latlon:
                    latlon_val = cities_latlon[item]
                elif item in countries_latlon:
                    latlon_val = countries_latlon[item]
                else:
                    latlon_val = 'NA,NA'
                f.write('"' + str(i) + '","' + item + '",' + str(log10(int(order[item])) + 1) + ',' + latlon_val + '\n')
                i += 1
            f.close()

    
    
    
def latlon(fname):
    cities_latlon = {}
    f = codecs.open(fname, 'r', 'utf-8')
    for ln in f:
        if ',' in ln:
            cells = ln.split(',')
            city = cells[1].strip('"')
            latlon = cells[2] + ',' + cells[3].strip()
            cities_latlon[city] = latlon
    f.close()
    return cities_latlon

def main():
    types = ['cities', 'countries']
    cities_latlon = latlon('cities_latlon.csv')
    countries_latlon = latlon('countries_latlon.csv')
    for tp in types:
        extractor(tp, cities_latlon, countries_latlon)
    return 0

if __name__ == '__main__':
	main()

#robjects.r('dec_years_seq <- c("' + dec_years_seq + '")')
#log10(x) + 1

# for word in sorted(rhyme, key=rhyme.get, reverse=True):
#    val = rhyme[word]
