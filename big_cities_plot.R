moskva <- c(0,7,3,6,15,24,7,17,16,54,51,56,57,37,39,22,12,16,40,129,297,147,147)
rim <- c(1,2,8,16,13,14,8,17,16,31,34,41,33,24,17,9,5,24,39,107,114,49,15)
parizh <- c(3,1,1,2,3,4,5,4,8,13,17,14,20,15,16,9,4,6,37,77,124,70,38)
sankt.peterburg <- c(0,1,0,0,0,0,2,2,4,14,14,9,12,13,20,11,5,6,10,71,100,63,85)
berlin <- c(0,0,0,2,3,1,1,2,1,0,0,1,2,3,5,3,0,1,2,22,35,9,47)
kiev <- c(0,0,1,0,1,2,0,2,4,7,11,7,3,6,9,8,2,1,7,18,16,17,20)
stambul <- c(0,1,1,0,5,6,4,4,2,2,14,10,3,7,8,3,1,2,5,37,16,3,3)
afiny <- c(0,2,2,3,4,6,3,8,12,17,15,1,6,8,5,2,1,2,9,8,9,5,1)
london <- c(1,0,0,0,1,1,2,1,2,3,4,1,6,1,5,3,0,2,2,17,25,10,6)
decades <- c(1720,1730,1740,1750,1760,1770,1780,1790,1800,1810,1820,1830,1840,1850,1860,1870,1880,1890,1900,1910,1920,1930,1940)

length(decades)

png(file="/home/boris/Work/Cloud/poetic/geo/Geo_entities/cities_in_dynamics_plot_small.png", width=800, height=600)

plot(moskva, col="red", type = "b", lwd = 1, lty = 1, pch = 19, xlab = "Decades", ylab = "Number", xaxt="n")
axis(1, at=seq(1:23), labels=decades)
lines(rim, type = "b", col="black", lwd = 2, lty = 2, pch = 20)
lines(parizh, type = "b", col="blue", lwd = 2,  lty = 1)
lines(sankt.peterburg, type = "b", col="green", lwd = 2, lty = 4, pch = 18)
lines(berlin, type = "b", col="grey", lwd = 2, lty = 1, pch = 17)
lines(kiev, type = "b", col="yellow", lwd = 2, lty = 1, pch = 6)
lines(stambul, type = "b", col="purple", lwd = 2, lty = 2, pch = 5)
lines(afiny, type = "b", col="orange", lwd = 2, lty = 3, pch = 1)

legend("topleft", col=c("red","black","blue","green","grey","yellow","purple","orange"), lwd=c(1,2,2,2,2,2,2,2), lty=c(1,2,1,4,1,1,2,3), pch=c(19,20,1,18,17,6,5,1), legend=c("Moscow", "Rome", "Paris", "Saint Petersburg", "Berlin", "Kiev", "Istanbul", "Athene"))

dev.off()

