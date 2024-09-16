# texto = input("Ingrese un texto para poder analizar: ").upper()
# letras = input("Ingrese tres letras que mas le gusten: ").upper()
#
# lista_texto = texto.split()
# lista_letra = list(letras)
# print(f"La letra {lista_letra[0]} aparece {texto.count(lista_letra[0])} veces, \n la letra {lista_letra[1]} aparece {texto.count(lista_letra[1])} veces \n y por ultimo la palabra {lista_letra[2]} aparece {texto.count(lista_letra[2])} veces en el parrafo")
# print(f"Tiene un total de {len(lista_texto)} palabras en la frase"  )
# print(f"La primera letra es {texto[0]} y la ultima es {texto[-1]}")
# print(f"Existe la palabra Python dentro del texto: {"Python" in texto}")


texto = input("Ingrese un texto para poder analizar: ").lower()
letras = [input("Ingresa la primera letra: "), input("Ingresa la segunda letra: "), input("Ingresa la tercera letra: ").lower()]

print("/n")
print("Cantidad de letras")
cantidad_letras = texto.count(letras[0])
cantidad_letras1 = texto.count(letras[1])
cantidad_letras2 = texto.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras} veces ")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras1} veces ")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras2} veces ")

print("/n")
print("Cantidad de palabras")
palabras = texto.split()
print(f"Hemos encontrado la cantidad de palabras {len(palabras)} en tu texto")

print("/n")
print("Letras de inicio y Fin")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"La letra inicial es '{letra_inicio}' y la letra final es '{letra_final}'")

print("/n")
print("Texto Invertido")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Si ordenamos un texto al reves va a decir '{texto_invertido}'")

print("/n")
print("Buscando la palabra Python")
buscar_python = "python" in texto
dic = {True: "si", False: "no"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")