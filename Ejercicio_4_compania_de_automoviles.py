

#definir funcion de calculos de comisiones
def comisiones():
    #definir precios y comisiones
    rbm_serie_1 = 20000
    rbm_serie_plus = 35000
    rbm_todoterreno = 60000

    #definir comisiones
    com_rbm_serie_1 = rbm_serie_1 * 0.03
    com_rbm_serie_plus = rbm_serie_plus * 0.05
    com__rbm_todoterreno = rbm_todoterreno * 0.07

    #pedir por pantalla la cantidad de coches
    cant_rbm_serie_1 = int(input("Ingrese la cantidad de vehículos RBM Serie 1 vendidos en el último mes: "))
    cant_rbm_serie_plus = int(input("Ingrese la cantidad de vehículos RBM Serie Plus vendidos en el último mes: "))
    cant_rbm_serie_todoterreno = int(input("Ingrese la cantidad de vehículos RBM Serie Todoterreno vendidos en el último mes: "))

    #calcular las comisiones totales en Euros
    com_total_serie_1 = com_rbm_serie_1 * cant_rbm_serie_1
    com_total_serie_plus = com_rbm_serie_plus * cant_rbm_serie_plus
    com_total_serie_todoterreno = com__rbm_todoterreno * cant_rbm_serie_todoterreno

    #imprimir comisiones parciales
    print("La comisiones totales RBM Serie 1 son: {}".format(com_total_serie_1))
    print("La comisiones totales RBM Serie Plus son: {}".format(com_total_serie_plus))
    print("La comisiones totales RBM TodoTerreno son: {}".format(com_total_serie_todoterreno))

    #comisiones totales del mes
    com_total_mes = com_total_serie_1 + com_total_serie_plus + com_total_serie_todoterreno
    print("Las comisiones totales del mes son: {}".format(com_total_mes))


#llamar a la funcion
print("Bienvenidos a la compañia de Automóviles")
print("Calcularemos las comisiones por totales de acuerdo a los vehículos vendidos por cada modelo")
comisiones()


