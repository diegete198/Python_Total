def repetidos(*args):
    valor = 0
    for arg in args:
        if valor == arg and valor == 0:
            return True
        else:
            valor = arg
            pass

    return False


# 6,0,5,1,0,3,0,1)
print(repetidos(6,1,5,1,0,3,2,1,0,5,1))
