'''
a. Crea un script en el que el usuario introduzca un número de más de una cifra. El script debe
imprimir los componentes del número uno a uno por pantalla. Por ejemplo si el número introducido
es el 4532 por pantalla deberá imprimirse:
4
5
3
2
b. Crea un script que dado un numero entero de cuatro cifras calcula e imprima el número que
resulta de leer el número introducido de derecha a izquierda. Por ejemplo si el número introducido
es 4532, el output deberá ser 2354
'''

cifra = input("A. Escribe un entero de más de una cifra: ")
for valor in cifra:
    print(valor)


cifra2 = input("\n13B. Escribe un entero de 4 de una cifras: ")
while int(cifra2) < 1000 or int(cifra2) > 9999:
    cifra2 = input("El número tiene que contener 4 cifras, vuelve a intenarlo: ")

print(cifra2[::-1])