#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  eng_rus_match.py
#  

import codecs
import re
import sys
import json

def main():
    eng_polygon_names = []
    f = codecs.open('countries_eng.txt', 'r', 'utf-8')
    for country in f:
        eng_polygon_names.append(country.strip())
    f.close()
    
    eng_country_names = {}
    f = codecs.open('../prepared_data/countries_all_abs_eng.csv', 'r', 'utf-8')
    for country in f:
        res = re.search('"(.+?)".+? "(.+?)"', country)
        indx = res.group(1)
        country = res.group(2)
        eng_country_names[indx] = country
    f.close()
    
    rus_country_names = {}
    f = codecs.open('../prepared_data/countries_all_abs.csv', 'r', 'utf-8')
    for country in f:
        res = re.search('"(.*?)","(.+?)"', country)
        indx = res.group(1)
        country = res.group(2)
        rus_country_names[indx] = country
    f.close()
    
    mtch = {}
    nmtch = []
    for indx in eng_country_names:
        if eng_country_names[indx] in eng_polygon_names:
            mtch[eng_country_names[indx]] = rus_country_names[indx]

    
    f = codecs.open('eng_rus_countries.json', 'w', 'utf-8')
    json.dump(mtch, f, ensure_ascii = False, indent = 4)
    f.close()
    return 0

if __name__ == '__main__':
	main()

