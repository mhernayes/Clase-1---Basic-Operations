import time

#llamar a la funcion saludo
def saludo(nombre):
    #imprimir el saludo
    print(      "Bievenidos a la calculadora de ahorros {}".format(nombre))
    #se devuelve la variable nombre
    return nombre

def datos():
    #solicitar salario, horas y gastos
    salario = int(input("Ingrese su salario en USD/hora:\n"))   
    horas = int(input("Ingrese la cantidad de horas trabajas en la semana:\n"))
    gastos = int(input("Ingrese los gastos semanales:\n"))
    #se devuelven las variables salario, horas y gastos
    return salario, horas, gastos
    
def calculos(salario, horas, gastos):
    salario_semanal = salario * horas
    salario_anual = salario_semanal * 52    
    gasto_anual = gastos * 52
    ahorros_anual = salario_anual - gasto_anual
    #se devuevlen las variables salario_anual y ahorro_anual
    return salario_anual, ahorros_anual

def resultados(nombre, ahorros_anual, salario_anual):
    print("{}, usted tiene una ganacia de {} USD anuales".format(nombre,salario_anual))
    print("Usted ahorrará por año {}".format(ahorros_anual))

#pedir el nombre de la persona
nombre = input("Por favor ingrese su nombre:\n ")

#llamar a la funcion saludo
nombre = saludo(nombre)

#llamar a la funcion datos. La variable salario, horas y gastos se igualan a la función que las reconozca
salario, horas, gastos = datos()

#llamar a la funcion calculos. La variable salario_anual y ahorro_anual se igualan a la función las reconozca
salario_anual, ahorro_anual = calculos(salario, horas, gastos)

#llamar a la función resultados. Se le pasa como parámetros nombre, ahorro_anual y salario_anual
resultados(nombre, ahorro_anual, salario_anual)





