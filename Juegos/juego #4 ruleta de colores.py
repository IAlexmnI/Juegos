print("*****************************************************")
print("                 La ruleta de colores                ")
print("*****************************************************")
print()


print("Adivina los 4 colores sin repetir ninguno")
print("Consigue puntos hasta que falles")
print()

colores = ("rojo", "verde", "morado", "blanco")
puntos = 0
repetido = []

juego = True
color = input("Dime un color: ")
color = color.lower()

while juego:
    if color in colores:
        puntos += 1
        
        if puntos < 4 and color not in repetido:
            print()
            print("Has acertado un color, tienes estos puntos:", puntos)
            repetido += [color]
            color = input("Dime otro color: ")
            color = color.lower()

        elif color in repetido:
            print()
            print("Perdiste con", puntos, "puntos por repetir color")
            juego = False
        else:
            print()
            print("¡Has ganado con todos los puntos!")
            juego = False

    else:
        print()
        print("Has perdido con", puntos, "puntos")
        juego = False


