precios_cafe = [('Capuchino', 3.5), ('Expresso', .9), ('Moka', 1.8)]

#for elemento in precios_cafe:
#     print(elemento)

def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_caro = ''

    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_caro = cafe
        else:
            pass
    return (cafe_caro, precio_mayor)

# print(cafe_mas_caro(precios_cafe))
cafe, precio = cafe_mas_caro(precios_cafe)
