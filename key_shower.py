#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  key_shower.py
#  
#12
#Государства
#Водные объекты
#Объекты флоры и фауны
#Улицы
#Гетто
#Месторождения
#Железнодорожные объекты
#Населенные пункты
#Вода и суша
#Пещеры
#Административные единицы
#Объекты рельефа

#  

import json

def main():
    js = open('/home/boris/Dropbox/geopoetics/all.json')
    geodict = json.load(js)
    js.close()
    print len(geodict)
    ks = geodict.keys()
    for k in ks:
        print k
    
    
    return 0

if __name__ == '__main__':
	main()

