#almacenar en un string 'estas usando python' y mostrarlo por pantalla
cadena_1 = "estas usando Python"
print(cadena_1)

#pedir por pantalla el nombre usuario y luego mostrar un mensaje
nombre_usario = input("ingrese el nombre de Usuario. ")
mensaje = "¡Hola, " + nombre_usario + ", estas usando Python"
'''print(mensaje)

#colocar el mensaje en mayuscula
mensaje = mensaje.upper()
print(mensaje)

#colocar el mensaje en minuscula
mensaje = mensaje.lower()
print(mensaje)

#colocar el mensaje en formato titulo
mensaje = mensaje.title()
print(mensaje)
'''
#borrar los puntos que puedan existir en el nombre
mensaje = mensaje.replace(".","")
mensaje = mensaje.title()
print(mensaje)