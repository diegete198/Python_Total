# palabra = 'Python'
# lista = [letra for letra in palabra]
# print(lista)
#
# lista_num = [n for n in range(0,21,2)]
# print(lista_num)\

# lista_num = [n for n in range(0,21,2) if n * 2 > 10]
# print(lista_num)

# lista_num = [n if n * 2 > 10 else 'no' for n in range(0,21,2)]
# print(lista_num)

pies = [10,20,30,40,50.60]
metros = [p * 3.281 for p in pies]
print(metros)
