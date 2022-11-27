from pylab import plot, show, title, xlabel, ylabel, legend

# Predicciones de tiempo de León, Nueva York y Berlin para el 19 Agosto 2021 de 12 AM a 12 PM
leon_temp = [15, 14, 13, 11, 11, 10, 9, 9, 9, 13, 15, 18, 20]
nyc_temp = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 26, 27, 28]
berlin_temp = [17, 17, 17, 17, 17, 16, 16, 16, 16, 17, 17, 17, 18]

times = ['0:00 AM', '1:00 AM', '2:00 AM', '3:00 AM', '4:00 AM', '5:00 AM', '6:00 AM', '7:00 AM', '8:00 AM', '9:00 AM', '10:00 AM', '11:00 AM', '12:00 PM']

plot(times, leon_temp)
plot(times, nyc_temp)
plot(times, berlin_temp)
legend(['León','New York', 'Berlin'])
title('Temperaturas del 19  de agosto de 2021')
xlabel('Horas')
ylabel('Temperatura')   
show()

