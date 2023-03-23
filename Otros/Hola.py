mi_str = "estas usando python"
mi_nombre = input("¿Cuál es tu nombre? ")
mi_nombre = mi_nombre.replace(".","")
mi_nombre = mi_nombre.lower().title()

nombre_y_str = "Hola " + mi_nombre + ", " + mi_str

print (nombre_y_str)