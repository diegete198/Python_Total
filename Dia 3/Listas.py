mi_lista = ["a", "b", "c", "d"]
mi_lista2 = ["e", "f", "g", "h"]
mi_lista3 = mi_lista2 + mi_lista
# otra_lista = ["hola", 55, 22.99]
# resultado = mi_lista[0:]

# mi_lista3[0] = "alfa"
mi_lista3.append("z")
eliminado = mi_lista3.pop(0)
mi_lista3.pop(0)
# mi_lista3.sort()
mi_lista3.reverse()

print(mi_lista3)
print(eliminado)