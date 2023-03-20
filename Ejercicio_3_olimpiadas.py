#olimpiadas
#ingresar los valores de los 3 participantes de las olimpiadas
#.split(" ") es para sacar un caracter un string

tiempo_1 = input("Ingrese el tiempo de Hannah Neise (xx:xx:xx): ")
tiempo_2 = input("Ingrese el tiempo de Jackie Narracott (xx:xx:xx): ")
tiempo_3 = input("Ingrese el tiempo de Kimberley Bos (xx:xx:xx): ")

#convertimos en numeros los caracteres ingresados
#calculamos el tiempo en segundos
seg_1 = int(tiempo_1[0:2]) * 60 + int(tiempo_1[3:5]) + int(tiempo_1[6:8]) / 60
print(seg_1)

seg_2 = int(tiempo_2[0:2]) * 60 + int(tiempo_2[3:5]) + int(tiempo_2[6:8]) / 60
print(seg_2)

seg_3 = int(tiempo_3[0:2]) * 60 + int(tiempo_3[3:5]) + int(tiempo_3[6:8]) / 60
print(seg_3)

#calcular la velocidad media
vel_1 = 100 / seg_1
print("La velocidad media de Hannah Neise es : {} m/s".format(vel_1))

vel_2 = 100 / seg_2
print("La velocidad media de Jackie Narracott es : {} m/s".format(vel_2))

vel_3 = 100 / seg_3
print("La velocidad media de Kimberley Bos es : {} m/s".format(vel_3))