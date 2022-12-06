import random
import time

juego = True
puntos = 0

print("------------------------------------")
print("""*****JUEGO DE MEMORIZAR COLORES*****""")
print("------------------------------------")
print()
print("""Tienes 3 segundos para memorizar 4 colores.
Al terminar el tiempo para memorizar, deberás introducir
los 4 colores en el orden en el que estaban""")
print()
input("¡PULSA ENTER PARA INICIAR!")

while juego:
    colores = ["rojo", "naranja", "amarillo", "verde", "azul", "celeste", "morado", "blanco", "negro", "cafe", "rosa"]

    print("Preparados...")
    time.sleep(1)
    print("Listos...")
    time.sleep(1)
    print("¡YA!")
    time.sleep(0.5)
    print()


    colores = random.sample(colores, 4)
    
    for i in range(len(colores)):
        print(colores[i], end = "  ")
    time.sleep(3)

    for i in range(35):
        print("**********************************************")
    
    color1 = input("Dime el primer color: ")
    if color1 == colores[0]:
        
        color2 = input("Dime el segundo color: ")
        if color2 == colores[1]:
            
            color3 = input("Dime el tercer color: ")
            if color3 == colores[2]:

                color4 = input("Dime el cuarto color: ")
                if color4 == colores[3]:
                    puntos += 1
                    print()
                    print("Has ganado", puntos,"puntos")
                    time.sleep(1)
                    print()
                    print("Ahora vamos de nuevo")
                    time.sleep(1)
                    print()

                else:
                    print("Has perdido con", puntos, "puntos")
                    juego = False
            else:
                print("Has perdido con", puntos, "puntos")
                juego = False
        else:
            print("Has perdido con", puntos, "puntos")
            juego = False
    else:
        print("Has perdido con", puntos, "puntos")
        juego = False
            


