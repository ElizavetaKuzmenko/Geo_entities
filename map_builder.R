library(ggmap)
library(ggplot2)

# geocode('Москва', output = "latlon", messaging = FALSE)

eu.data <- read.csv('/home/boris/Work/geo/countries.csv')
eu <- get_map(location = 'europe', zoom=4, maptype="roadmap", color='bw', language='ru-RU')
eu.map <- ggmap(eu)
png(file='/home/boris/Work/geo/euromap.png', width=800, height=800)
eu.map.o <- eu.map + geom_point(data = eu.data, aes(x = lon, y = lat, color = Freq, size = Freq))
eu.map.o <- eu.map.o + scale_color_gradient(low = 'blue', high = 'red')
eu.map.o <- eu.map.o + ggtitle('Frequency of country names in Russian poetry\n') + theme(legend.position = 'right')
eu.map.o
dev.off()

library(ggmap)
library(ggplot2)
eu.data <- read.csv('/home/boris/Work/geo/poetic_cities2.csv')
eu <- get_map(location = 'europe', zoom=4, maptype="roadmap", color='bw', language='en-US')
eu.map <- ggmap(eu)
png(file='/home/boris/Work/geo/euromap3.png', width=800, height=800)
eu.map.o <- eu.map + geom_point(data = eu.data, aes(x = lon, y = lat, color = Freq, size = Freq))
eu.map.o <- eu.map.o + scale_color_gradient(low = 'blue', high = 'red')
eu.map.o <- eu.map.o + ggtitle('Frequency of city names in Russian poetry\n') + theme(legend.position = 'right')
eu.map.o
dev.off()

# http://habrahabr.ru/post/264153/
