# def multiplicar(numero1, numero2):
#     total = numero2 * numero1
#     return total
#
# # print(multiplicar(1,2))
# resultado = multiplicar(10,5)
# print(resultado)


def inverti_palabra(palabra):
    palabras = list(palabra)
    palabras.reverse()
    texto_invertido = ''.join(palabras).upper()
    return texto_invertido


palabra = "Mesa"

resultado = inverti_palabra(palabra)
print(resultado)
