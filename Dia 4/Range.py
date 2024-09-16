# for numero in range(1,100,10):
#     print(numero)

# lista = list(range(1,101))
# print(lista)

suma_numero = 0

for numero in range(1,16):
    suma_numero = suma_numero + (numero**2)
    print(f'La potencia de {numero} a la 2 potencia es igual a {suma_numero}')

print(f'Total es {int(suma_numero)}')