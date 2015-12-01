#!/usr/local/python/python2.7/bin/python2.7
# coding: utf-8

import codecs
import rpy2.robjects as robjects

robjects.r('library(ggmap)')

fw = codecs.open('/home/boris/Work/geo/poetic_cities.csv', 'w', 'utf-8')
fw.write(u'"","City","Freq","lon","lat"\n')

i = 0

f = codecs.open('/home/boris/Work/geo/cities.csv', 'r', 'utf-8')
for line in f:
    i += 1
    line = line.strip()
    city, freq = line.split()
    robjects.r('l = geocode("' + city + '", output = "latlon", messaging = FALSE)')
    robjects.r('a = as.vector(t(l))')
    latlon = robjects.r('a')
    print (latlon)
    latlon2 = str(latlon)
    fw.write(u'"' + unicode(i) + u'","' + city + u'",' + freq + u',' + latlon2)
    #fw.write(latlon2 + u'\n')
    #if i == 5:
        #break

f.close()
fw.close()

# print robjects.r('c <- c(1, 2, 3)')
