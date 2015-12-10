#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  
# source('prepared_data/countries.R')

import codecs, json
from math import log10


def extractor():
    f = codecs.open('../countries.json', 'r', 'utf-8')
    data = json.load(f)
    countries = data['all']
    f.close()
    f = codecs.open('eng_rus_countries.json', 'r', 'utf-8')
    mtch = json.load(f)
    f.close()
    eng_polygon_names = []
    f = codecs.open('countries_eng.txt', 'r', 'utf-8')
    for country in f:
        if country.strip() in mtch:
            if mtch[country.strip()] in countries:
                eng_polygon_names.append(str(log10(countries[mtch[country.strip()]]) + 1))
            else:
                eng_polygon_names.append('0')
        else:
            eng_polygon_names.append('0')
    f.close()
    f = codecs.open('../prepared_data/countries.R', 'w', 'utf-8')
    f.write('library(maps)\n')
    f.write('library(mapproj)\n')
    f.write('library(latticeExtra)\n')
    f.write('worldmap <- map("world", plot = FALSE, fill = FALSE,  projection = "azequalarea")\n')
    f.write('country = worldmap$names\n')
    f.write('var.countries <- c(' + ','.join(eng_polygon_names) + ')\n')
    f.write('worldt <- data.frame (country, var.countries)\n')
    f.write('print(mapplot(country ~ var.countries, worldt, map = map("world", plot = FALSE, fill = TRUE), colramp = colorRampPalette(c("black", "yellow")), main = "Countries frequency in Russian poetry"))\n')
    f.write('dev.copy(png,"maps_countries/countries_all.png", width=1800, height=1200)\n')
    f.write('dev.off()\n')
    f.close()


def main():
    extractor()
    return 0

if __name__ == '__main__':
	main()

#robjects.r('dec_years_seq <- c("' + dec_years_seq + '")')
#log10(x) + 1

# for word in sorted(rhyme, key=rhyme.get, reverse=True):
#    val = rhyme[word]
