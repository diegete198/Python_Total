from random import *

nombre = input("Por favor dime tu nombre: ")
numero_user = 0
print(f'Bueno, {nombre}, he pensado un número entre 1 y 100. \n'
      f'Tienes solo 8 intentos para adivinar. ')
intentos = 0
numero_ganador = randint(1, 100)

while intentos < 8:
    numero_user = int(input(f'Cuál crees que es el número: '))
    intentos += 1
    if numero_user < 0 or numero_user > 100:
        print(f'El numero {numero_user} que ha escogido no es valido')
        if intentos != 8:
            print(f"Vuelve a intentarlo, te quedan {8-intentos} intentos ")
        continue
    elif numero_user < numero_ganador:
        print(f'Su respuesta es incorrecta, ha elegido un número menor al número secreto')
        if intentos != 8:
            print(f"Vuelve a intentarlo, te quedan {8-intentos} intentos ")
        continue
    elif numero_user > numero_ganador:
        print(f'Su respuesta es incorrecta, ha elegido un número mayor al número secreto')
        if intentos != 8:
            print(f"Vuelve a intentarlo, te quedan {8-intentos} intentos ")
        continue
    else:
        print(f"Felicidades {nombre}! Has adivinado en {intentos} intentos el concurso")
        break
else:
    print(f"Lo siento se te han agotado los intentos, el numero secreto era {numero_ganador}")
