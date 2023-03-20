#convertir euros a dolares
euros = float(input("Ingrese la cantidad de euros "))
dolares_brutos = (euros * 1.2)
print("Los dolares brutos son: ", dolares_brutos)

#agregarle una comision
dolares_netos = dolares_brutos * 0.9
print("Usted recibirá: {}".format(dolares_netos))
comision = dolares_brutos - dolares_netos
print("La comisión de la casa de cambios es del 10% y es de: {}". format(comision))

