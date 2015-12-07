#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  maps_maker.py
#  

import os
import codecs
import rpy2.robjects as robjects

location = u'africa'
zoom = '3'

def mapmaker(flname, root, location, zoom):
    robjects.r('library(ggmap)')
    robjects.r('library(ggplot2)')
    robjects.r('setwd("' + os.getcwd() + '")')
    robjects.r('eu.data <- read.csv("' + root + os.sep + flname + '")')
    robjects.r('eu <- get_map(location = "' + location + '", zoom=' + zoom + ', maptype="roadmap", color="bw", language="en-US")')
    robjects.r('eu.map <- ggmap(eu)')
    beginpath, endpath = root.split('prepared_data')
    path = beginpath + 'maps' + endpath + '/'
    if os.path.exists(path) == False:
        os.mkdir(path)
    mapname = flname.replace('.csv', '')
    print path + mapname
    robjects.r('eu.map.o <- eu.map + geom_point(data = eu.data, aes(x = lon, y = lat, color = Freq, size = Freq))')
    robjects.r('eu.map.o <- eu.map.o + scale_color_gradient(low = "brown", high = "yellow")')
    robjects.r('eu.map.o <- eu.map.o + ggtitle("' + mapname + '\n") + theme(legend.position = "right")')
    robjects.r('print(eu.map.o)')
    robjects.r('ggsave("' + path + mapname + '.png", width=8, height=8)')
    robjects.r('dev.off()')
    
        
    

def main():
    for root, dirs, files in os.walk('../prepared_data'):
        for flname in files:
            if 'authors' in root or 'countries' in root:
                continue
            if '0.csv' == flname:
                continue
            if flname.endswith('.csv'):
                try:
                    mapmaker(flname, root, location, zoom)
                except:
                    print 'problem: ' + root + os.sep + flname
    return 0

if __name__ == '__main__':
	main()

#robjects.r('')