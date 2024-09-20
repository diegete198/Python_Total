from random import choice

no_vida = 7
guion = ''
palabra_al_azar = choice(["Melon", "Manzana", "Sandia", "Guanabana", "Papaya"])
cantidad_letra = len(palabra_al_azar)

print("Bienvenido al juego del ahorcado a continuacion se selecionara una palabra al azar \n"
      " y tendra 7 vidas para descubirla: ")
print(palabra_al_azar)

while cantidad_letra > 0:
    guion += '_ '
    cantidad_letra -= 1

print(f"Esta es la longitud de la palabra elegida: \n"
      f" {guion}")


def validar_letra(letra_a_validar):
    if isinstance(letra_a_validar, str) is True:
        return True
    else:
        print("No ingresaste una letra y perdiste una vida")
        return False


def chequear_letra(palabra_ganadora, letra_seleccionada):
    no_veces_existe_letra = 0
    if letra_seleccionada not in palabra_ganadora:
        print("Esa letra no existe dentro de la palabra")
        return False
    else:
        no_veces_existe_letra = palabra_ganadora.find(letra_seleccionada)
        print(no_veces_existe_letra)
        return True


while no_vida > 0:

    letra = input("Ingrese una letra: ")

    if validar_letra(letra) is False:
        no_vida -= 1
        print(f"Te quedan {no_vida} vidas en el juego")

    if chequear_letra(palabra_al_azar, letra) is False:
        no_vida -= 1
        print(f"Te quedan {no_vida} vidas en el juego")

    if no_vida == 0:
        print("Has perdido el juego")
