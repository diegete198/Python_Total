# mi_list = ['Diego', 'Armando', 'Aldo Samuel', 'Cristina']
#
# for element in mi_list:
#     num_letra = mi_list.index(element) + 1
#     print(f"{num_letra}: Hola {element}")


# list= ["Diego", 'Armando', "Pablo", 'Angel', "Alfredo"]
#
# for nombre in list:
#     if nombre.startswith('O'):
#         print(nombre)
#     else:
#         print("Nombre que no comienza con A")

# numeros = [1,2,3,4,5,6]
# mi_valor = 0
#
# for numero in numeros:
#     mi_valor = mi_valor + numero
#
#     print(mi_valor)

# palabra = 'Python es genial'
#
# for letra in palabra:
#     print(letra)

# for numero1,numero2, numero3 in [[1,2,3], [4,5,6], [7,8,9]]:
#     print(numero1)
#     print(numero2)
#     print(numero3)


# dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}
#
# for item1, item2 in dic.items():
#     print(item1,item2)
#

lista_numeros = [1,5,8]
suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
    if numero//2 == 0:
        print('es par')
        suma_pares = suma_pares + numero
    else:
        suma_impares = suma_impares + numero

print(suma_impares, suma_pares)
