# monedas = 5
#
# while monedas > 0:
#     print(f'Tengo {monedas} monedas')
#     monedas -= 1
# else: print("No tengo mas dinero")

#respuesta = 's'
#
# while respuesta == 's':
#     respuesta = input("Quieres seguir? (s/n)")
# else:
#     print('Graciass')

# resp = 's'
#
# while resp == 's':
#     pass
#
# print("Hola")


# nombre = input('Tu nombre:')
#
# for letra in nombre:
#     if letra == 'r':
#         continue
#     print(letra)

# numero = 50
#
# while numero > 0:
#     if numero % 5 == 0:
#         print(numero)
#         numero -= 1
#     else:
#         numero -= 1
#         continue

lista_numeros = [4, 5, 8, 7, 6, 9, 8, 2, 4, 5, 7, 1, 9, 5, 6, -1, -5, 6, -6, -4, -3]

for numero in lista_numeros:
    if numero < 0:
        break
    else:
        print(numero)
