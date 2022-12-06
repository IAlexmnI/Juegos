from time import time
from random import randint, choice

inicio = time()
puntos = 0
signos = ["+", "*"]

input("Para empezar, pulsa Enter")
inicio = time()

while True:   
    n1 = randint(1, 9)
    n2 = randint(1,9)
    op = choice(signos)

    if op == "+":
        res = n1 + n2
        n1, n2 = str(n1), str(n2)
        answer = int(input(n1 + " " + op + " " + n2 + " " + "= "))

    elif op == "*":
        res = n1 * n2
        n1, n2 = str(n1), str(n2)
        answer = int(input(n1 + " " + op + " " + n2 + " " + "= "))
        

    if res == answer:
        puntos += 1
        print("Bien hecho, puntos:", puntos)
        print()
        
    else:
        print("Fallaste, puntos:", puntos)
        print()

    final = time()
    if final - inicio >= 10:
        print("Juego terminado, terminaste con", puntos, "puntos")
        break
        
    
    
    
