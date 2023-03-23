'''En la competición de skeleton de las olimpiadas de invierno hay tres finalistas. El cronómetro mide
los siguientes tiempos:
Hannah Neise: 8 minutos 3 segundos y 10 centésimas
Jackie Narracott: 12 minutos 7 segundos y 8 centésimas
Kimberley Bos: 9 minutos 14 segundos y 3 centésimas
1. Crea un script que pida los tiempos por pantalla para cada uno de los finalistas
2. Convierte los tiempos de minutos-segundos-centésimas a segundos
3. Sabiendo que la pista es de 100 metros calcula la velocidad media de cada uno de ellos en
metros por segundo.
4. Imprime los resultados por pantalla'''

# Convierte string de tiempo "minutos-segundos-centésimas" a segundos
def getSeconds(finalista):
    finalista_time = str(finalista).split('-')
    minutes = int(finalista_time[0])
    seconds = int(finalista_time[1])
    hundredths = float(finalista_time[2])
    total_seconds = (minutes*60)+seconds+(hundredths/100)
    return total_seconds


finalista1 = input("Tiempo del primer finalista (minutos-segundos-centésimas): ")
finalista2 = input("Tiempo del segundo finalista(minutos-segundos-centésimas): ")
finalista3 = input("Tiempo del tercer finalista(minutos-segundos-centésimas): ")

print ("*** FINALISTA 1 ***\nSegundos: " + str(getSeconds(finalista1)))
print ("Velocidad media: " + str(getSeconds(finalista1)/100) + " m/s")
print ("*** FINALISTA 2 ***\nSegundos finalista 2: " + str(getSeconds(finalista2)))
print ("Velocidad media: " + str(getSeconds(finalista2)/100) + " m/s")
print ("*** FINALISTA 3 ***\nSegundos finalista 3: " + str(getSeconds(finalista3)))
print ("Velocidad media: " + str(getSeconds(finalista3)/100) + " m/s")







