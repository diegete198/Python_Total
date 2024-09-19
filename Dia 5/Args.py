# def suma(*args):
#     return sum(args)
#
#
# print(suma(5, 6, 7, 1))


# def suma_obsoletos(*args):
#     suma = 0
#     for arg in args:
#         suma += abs(arg)
#
#     return suma
#
#
# print(suma_obsoletos(1, 2, -3,-6))


def numeros_persona(nombre, *args):
    suma = sum(args)
    return f'{nombre}, la suma de tus numero es {suma}'
