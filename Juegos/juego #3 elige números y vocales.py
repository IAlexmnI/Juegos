puntos = 100
juego = True

while juego:
    num = int(input("Dime un número del 1 al 5: "))
    vocal = input("Dime una vocal: ")

    if 0 >= num or num > 5:
        if vocal != "a" and vocal != "e" and vocal != "i" and vocal != "o" and vocal != "u":
            puntos -= 5
            print(puntos, "-5")
        else:
            puntos -= 2
            print(puntos, "-2")
        
    elif vocal != "a" and vocal != "e" and vocal != "i" and vocal != "o" and vocal != "u":
        puntos -= 2
        print(puntos, "-2")
        

    else: 
        print("GG, has ganado con", puntos, "puntos")
        juego = False 
