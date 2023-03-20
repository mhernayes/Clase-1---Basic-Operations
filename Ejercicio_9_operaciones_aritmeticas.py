#funcion 1
def operacion_1():
    #realizar el calculo 1
    print("Vamos a realizar la siguiente operacióin matematica")
    resultado_1 = ((3+2)/(2*5))**2
    #imprimir el resultado 1
    print(resultado_1)

def operacion_2(_variable):
    #realizar el calculo 2
    resultado_2 = (_variable * (_variable + 1 )) / 2
    #imprimir el resultado
    print(resultado_2)


#solicitar por la pantalla que se ingrese el valor de X

variable = int(input("Ingrese el valor de x: "))

#llamar a la funcion 1
operacion_1()

#llamar a la funcion 2

operacion_2(variable)

