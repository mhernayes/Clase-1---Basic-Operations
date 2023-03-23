'''Una casa de cambios necesita construir un programa que dada una cantidad de euros introducida
por el usuario de el resultante en dólares.
1. Crea un script que reciba una cantidad de euros del usuario e imprima por pantalla el
correspondiente en dólares (considera una tasa de cambio donde 1 EU = 1.2 $)
2. La casa de cambios se queda un 10% en concepto de ‘tasas de gestión’. Calcula el monto
recibido, el cambio en dólares, la cantidad que se queda la casa de cambios y la cantidad de
dólares restante que recibirá el usuario. Imprime el desglose por pantalla formateado de tal
forma que quede claro para el usuario.'''

euros = input("Introduce el monto en euros para obtener en cambio en $. (1€ = 1,2$) ")
dolares = float(euros) * 1.2
print ("Monto en dolares: " + str(dolares))
tasa_gestion = dolares * 0.10
total_dolares = dolares - tasa_gestion
print ("Tasas de gestion 10%: " + str(tasa_gestion))
print ("Disponible en dolares: " + str(total_dolares))

