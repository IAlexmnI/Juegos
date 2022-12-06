#Juego #1 Python

print("Juego para adivinar el número preselecionado")

pedir = int(input("Dame un número del 1 al 10: "))
num = 2
contador = 1

while pedir != num:
    print()
    print("Has jugado", contador, "veces")
    contador += 1
    pedir = int(input("Dame otro: "))
  
else:
    print("¡Ganaste y te tomó", contador, "intentos!")
