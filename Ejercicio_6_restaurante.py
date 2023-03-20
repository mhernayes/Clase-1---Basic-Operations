def menu():     #funcion menu
    menu = """"
    Bienvenidos al Restaurante CONQUERBLOCKS
    El menú es el siguiente:

    1 - Ensalada mixta ———————— 12 EU
    2 - Sopa de pescado ——————— 10 EU 
    3 - Dorada al horno ——————— 18 EU 
    4 - Arroz al curry ———————— 14 EU
    5 - Lasaña de carne ——————— 15 EU
    6 - Brownie de chocolate —— 8 EU
    7 - Helado ———————————————— 6 EU
    8 - Refrescos ————————————— 5,5 EU 
    9 - Café —————————————————— 3,5 EU
    """
    print(menu)

def suma_total():
    #seteamos el monto total en 0 para poder realizar el bucle
    total = 0

    #pedimos por pantalla si quiere ordenar
    pregunta = input("¿Desea ordenar? s/n ")

    #bucle para preguntar si quiere tomar algo más (con variable pregunta = s se repite)
    while pregunta == "s":  
        #solicitar ingresar la opcióin y las cantidades 
        pedido = input("Por favor ingrese que el número de lo que desea tomar/comer: ") 

        #nos quedamos con el precio de lo elegido  
        precio_pedido = precios.get(pedido) 
        #solicitamos la cantidades
        cantidades = int(input("Por favor ingrese las cantidades que desea: ")) 
        #calculamos el subtotal    
        sub_total = precio_pedido * cantidades 
        #calculamos el total     
        total = sub_total + total   
        #preguntamos si quiere ordenar algo mas para completar el bucle
        pregunta = input("¿Desea ordenar algo más? s/n ")

    #imprimimos el total
    print("Usted debe abonar un total de: {}".format(total))

#llamar a al funcion menu
menu()  

#definir la lista de precio con un diccionario
precios = {"1": 12, "2": 10, "3": 18, "4": 14, "5": 15, "6": 8, "7": 6, "8": 5.5, "9": 3.5}

#llamamos a la función para realizar el calculo
suma_total()

#imprimimos el total  
print("Gracias por venir. Adios!")