from pylab import plot, show

nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3]
plot(nyc_temp, marker = 'o')
show()

# Para visualizar los años, con matplotlib podemos visualizar en el eje x datos de tipo float y en el eje y datos de tipo integer y viceversa.
years = range(2000, 2013)  
plot(years, nyc_temp, marker = 'o')
show()

