def deletrear(palabra):
    lista_palabras = list(palabra.lower())
    lista_palabras = list(dict.fromkeys(lista_palabras))
    lista_palabras.sort()
    return lista_palabras


print(deletrear("entretenido"))
