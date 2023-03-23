'''Una compañía de automóviles vende tres tipos de coche: RBM Serie 1, RMB Serie plus, RBM
todoterreno. Cada uno de estos coches tiene un precio de venta y el vendedor recibe una
comisión diferente por cada tipo de coche que ha vendido.
Suponga que los precios y las comisiones son:
RBM Serie 1:
precio: 20.000 EU, comisión: 3%
RMB Serie plus:
precio: 35.000 EU, comisión: 5%
RBM todoterreno:
precio: 60.000 EU, comisión: 7%
Crea un programa donde el usuario introduzca el numero de coches vendidos de cada tipo ese
mes y que le devuelva la cantidad en euros a comisionar ese mes'''


total_serie1 = int(input("Nº de ventas modelo RBM Serie 1: "))
total_seriePlus = int(input("Nº de ventas modelo RMB Serie plus: "))
total_todoterreno = int(input("Nº de ventas modelo RBM todoterreno: "))

comisiones_serie1 = 20000*total_serie1*0.03
comisiones_seriePlus = 35000*total_seriePlus*0.05
comisiones_todoterreno = 60000*total_todoterreno*0.07

print("Comisiones RBM Serie 1: " + str(comisiones_serie1))
print("Comisiones RBM Serie plus: " + str(comisiones_seriePlus))
print("Comisiones RBM Serie todoterreno: " + str(comisiones_todoterreno))
