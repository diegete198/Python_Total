# serie = 'N-06'
#
# # if serie == 'N-01':
# #     print("Samsung")
# # elif serie == 'N-02':
# #     print('Nokia')
# # elif serie == 'N-03':
# #     print('Motorola')
# # else:
# #     print('No existe el producto')
#
#
# match serie:
#     case 'N-01':
#         print("Samsung")
#     case 'N-02':
#         print("Nokia")
#     case 'N-03':
#         print('Motorola')
#     case _:
#         print('No existe el producto')


cliente = {'nombre': 'Diego',
           'edad': '39',
           'ocupacion': 'Ingeniero'
           }

pelicula = {'titulo': 'Matrix',
            'ficha_tecnica': {'protagonista': 'Keanu Reaves',
                              'director': 'Lana y Lilly Wachoswki'}}

elemento = [cliente, pelicula, 'Libro']

for e in elemento:
    match e:
        case {'nombre': nombre, 'edad': edad, 'ocupacion': ocupacion}:
            print("Es un cliente")
            print(nombre,edad,ocupacion)
        case {'titulo': titulo, 'ficha_tecnica': {'protagonista': protagonista, 'director': director}}:
            print('Esto es una pelicula')
            print(titulo, protagonista, director)
        case _:
            print("No se que es esto")