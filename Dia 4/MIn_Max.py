# menor = min(58,96,34,667,121,11)
# maximo = max(58,96,34,667,121,11)
#
# print(menor)
# print(maximo)

# lista = [58,96,34,667,121,11]
# print(max(lista))
# print(min(lista))
# print(f'El mayor es {max(lista)} y el menor es {min(lista)}')

# nombre = ['Juan', 'Carlos', 'Armando', 'Zuleima']
# nombre1 = 'Carlos'
# print(min(nombre1.lower()))
# print(min(nombre), max(nombre))
#
# dic = {'C1': 45, 'C2': 11, 'C3': 1}
# print(min(dic.values()))


diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

edad_minima = min(diccionario_edades.values())
print(edad_minima)
ultimo_nombre = max(diccionario_edades.keys())
print(ultimo_nombre)