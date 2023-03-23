'''
RESTAURANTE:
En un restaurante el menú consta de las siguientes opciones:
Ensalada mixta ———————— 12 EU
Sopa de pescado ——————— 10 EU
Dorada al horno ———————— 18 EU
Arroz al curry ————————— 14 EU
Lasaña de carne ——————— 15 EU
Brownie de chocolate ————— 8 EU
Helado ——————————— 6 EU
Refrescos —————————— 5,5 EU
Café ———————————— 3,5 EU
Escribe un script que lea la cantidad de cada alimento consumido y que calcule e imprima el total
de la cuenta'''

listAlimentos = ["Ensalada mixta (12€)", "Sopa de pescado (10€)", "Dorada el horno (18€)", "Arroz al curry (14€)", 
"Lasaña de carne (15€)", "Brownie de chocolate (8€)", "Helado (6€)", "Refrescos (5,5€)", "Café (3,5€)"]
total = 0
suma = 0

for alimento in listAlimentos:
    
    unidades = input("Escribe el número de unidades de " + alimento + ": ")    
    unidades = int(unidades)

    if alimento == "Ensalada mixta (12€)":
        suma = 12*unidades
    elif alimento == "Sopa de pescado (10€)":
        suma = 10*unidades
    elif alimento == "Dorada el horno (18€)":
        suma = 18*unidades
    elif alimento == "Arroz al curry (14€)":
        suma = 14*unidades
    elif alimento == "Lasaña de carne (15€)":
        suma = 15*unidades
    elif alimento == "Brownie de chocolate (8€)":
        suma = 8*unidades
    elif alimento == "Helado (6€)":
        suma = 6*unidades
    elif alimento == "Refrescos (5,5€)":
        suma = 5.5*unidades
    elif alimento == "Café (3,5€)":
        suma = 3.5*unidades           
            
    print("Total: " + str(total) + "+" + str(suma))
    total = total + suma

print("Total menú: " + str(total))