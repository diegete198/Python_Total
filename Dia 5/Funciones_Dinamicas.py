# def chequear_3_cifras(numero):
#     return  numero in range(100,1000)
#
# suma = 586 + 403
#
# resultado = chequear_3_cifras(suma)
# print(resultado)

def chequear_3_digitos(lista):

    listacifras = []

    for n in lista:
        if n in range(100,1000):
            listacifras.append(n)
        else:
            pass
    return listacifras

resultado = chequear_3_digitos([554,77,188])
print(resultado)

