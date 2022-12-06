import random

posibles = ("piedra", "papel", "tijeras")
juego = True
ganar = "¡Has ganado! GG"
perder = "Has perdido, RIP"
empatar = "Has empatado"

while juego:
    seguir = ""
    mano = (input("¿Piedra, Papel o Tijeras?: "))
    print()
    respuesta = random.choice(posibles)
    
    if mano == "piedra":
        if respuesta == "tijeras":
            print(ganar)
            
        elif respuesta == "papel":
            print(perder)

        else:
            print(empatar)

    elif mano == "papel":
        if respuesta == "piedra":
            print(ganar)
            
        elif respuesta == "tijeras":
            print(perder)

        else:
            print(empatar)

    elif mano == "tijeras":
        if respuesta == "papel":
            print(ganar)
            
        elif respuesta == "piedra":
            print(perder)

        else:
            print(empatar)

    else:
        print("No los has escrito correctamente")

    while seguir != "s" and seguir != "n":
        print()
        seguir = input("¿Quieres seguir jugando? (s/n): ")
        print()
        if seguir == "n":
            juego = False
        elif seguir == "s":
            ""
        else:
            print("No se te ha entendido, intenta de nuevo")
        
print()
print("¡Gracias por jugar!")                   
