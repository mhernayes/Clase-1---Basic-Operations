'''
TARJETA DE CRÉDITO:
Crea un script que reciba como input un número de tarjeta de crédito e imprima por pantalla todos
los caracteres en forma de asterisco salvo los últimos cuatro. Si por ejemplo el número de tarjeta
es 1234 2345 3456 5678, el output deberá ser **** **** **** 5678.
'''

#Importación de la librería para buscar usando patrones
import re
#Patron que valida las tarjetas de crédito
pattern = '^[0-9]{16}|[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}|[0-9]{4} [0-9]{4} [0-9]{4} [0-9]{4}$'

cc = input("Nº de CC: ")

result = re.match(pattern, cc)
if result:
    init = len(cc)-4
    end = len(cc)
    print("**** **** **** " + cc[init:end])
else:
    print(cc + " -> " + "Nº de tarjeta no válido")        