# def prueba(num1, num2, *args, **kwargs):
#     print(f'El primer valor es {num1}')
#     print(f'El segundo valor es {num2}')
#     for arg in args:
#         print(f'arg = {arg}')
#
#     for clave, valor in kwargs.items():
#         print(f"{clave} = {valor}")
#         # total += valor
#     # print(type(kwargs))
#
#
# args = [50, 80, 20,40]
# kwargs = {'x': 'uno', 'y': 'dos', 'z': '10', 'a': 'Hola', 'b': 'tres'}
# print(prueba(2, 15, *args, **kwargs))


# def cantidad_atributos(**kwargs):
#     cantidad = 0
#     for clave in kwargs.items():
#         cantidad += 1
#     return cantidad
#
#
# kwargs = {'x': 'uno', 'y': 'dos', 'z': '10', 'a': 'Hola', 'b': 'tres'}
#
# print(cantidad_atributos(**kwargs))

def describir_persona(nombre,**kwargs):
    print(f'Características de {nombre}')
    for key, value in kwargs.items():
        print(f'{key}: {value}')


kwargs = {'ojo': 'azules', 'pelo': 'rubio', 'comprexion': 'delgado'}
print(describir_persona('Diego', **kwargs))

