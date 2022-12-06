
print("""¡JUEGO MAYOR/MENOR! ¡Adivina número aleatorio
    del 1 al 100! ¡Tienes 7 intentos!""")
print()

import random
lol = random.randint(1, 100)
ganaste = False

frases_alto = ("Demasiado alto",
               "Tu número es mayor, prueba con uno más pequeño",
               "¡Te fuiste hasta las nubes, ve más bajito!",
               "Poniendo números más altos, no encontrarás la respuesta")
frases_bajo = ("Tu número es menor, prueba con uno más grande",
               "Vamos a subir que estamos muy bajito", "¡Sube más!",
               "Muy cerca del suelo ¡súbele!")
               
gg = ("¡GG! ¡Victoria magistral!", "¡Excelente! ¡Has ganado!",
      "¡Qué crack! ¡ganaste!",
      "¡No sabía que en este mundo habían adivinos así!")

perder = ("Rip", "Perdiste", "Tus inentos se agotaron",
          "Mejor suerte para la próxima")

for i in range(7):
    num = int(input("Dame un número del 1 al 100: "))
    print()
    if num > lol:
        if i == 6:
            break
        print(random.choice(frases_alto))

    if num < lol:
        if i == 6:
            break
        print(random.choice(frases_bajo))


    elif num == lol:
        print(random.choice(gg) + ", efectivamente, el número es", lol)
        ganaste = True
        break

if i == 6 and ganaste == False:
    print(random.choice(perder) + ", el número era", lol)

    
    

