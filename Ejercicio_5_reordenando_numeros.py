#definir la función
def funcion_reordenar(_numero):
    _numero = str(_numero)    #transformar el numero a un string para poder recorrelo y elimnar el "-" en caso de que hubiera
    long = len(_numero)  #calculamos el largo del string
    for i in range(0,long): #usamos ese largo para recorrer el string con un "for"
        if _numero[i] == "-":   #si el numero es negativo saltamos el "-"
            pass
        else:
            print(_numero[i])   #imprimimos el string

def funcion_inversa(_numero): 
    if _numero < -999:    #si el numero es negativo eliminamos el signo "-""
        _numero = _numero * -1
        print('Saltearemos el signo "-"')
    _numero = str(_numero)    #transformar el numero a un string para poder imprimirlo al revés
    print(_numero[::-1])   #imprimimos el string de forma inversa

#establecer las condiciones del numero ingresado
numero = int(input("Ingrese un numero de 4 dígitos: "))

if numero < 999 and numero > -999:  #el numero debe ser de 4 digitos positivo o negativo
    print("El número ingresado no es de 4 dígitos, por favor ingrese a un numero de 4 dígitos ")
    
else:
    print("El numero ingresado es correcto")
    print("Ahora reordenaremos el numero:") #mostramos mensaje de la operacion a realizar 
    funcion_reordenar(numero)   #llamar a la funcion
    print("Ahora imprimiremos el número ingresado al revés")
    funcion_inversa(numero)
