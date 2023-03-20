#funcion ocultar caracteres
def ocultar_caracteres(_numero_tarjeta):
    #calcular la longitud del string
    long = len(_numero_tarjeta)
    print("*" * (long-4) + _numero_tarjeta[long-4:long])
    
    

#ingresar los numeros de la tarjeta de credito
numero_tarjeta = (input("¿Por favor ingrese los 16 números de la tarjeta de credito? "))

#llamar a la funcion
ocultar_caracteres(numero_tarjeta)

'''
#ingresar los numeros de la tarjeta de credito
numero_tarjeta = (input("¿Por favor ingrese los 16 números de la tarjeta de credito? "))

print("**** **** ****", numero_tarjeta[12:16])
'''