# if 10 > 19:
#     print("Es correcto")
# else:
#     print("No es correcto")
#

# mascota = 'Hamsters'
# if mascota == 'Gato':
#     print('Tienes un gato')
# elif mascota == 'Perro':
#     print("Tienes un perro")
# else:
#     print('No se que animal tienes')

# edad = 18
# calificacion = 5
# if edad >= 18:
#     print('Eres mayor de edad')
#     if calificacion >= 7:
#         print('Aprobado')
#     else:
#         print("No aprobado")
# else:
#     print('Eres menor de edad')

# num1 = int(input("Ingresa un número:"))
# num2 = int(input("Ingresa otro número:"))
#
# if num1 > num2:
#     print(f"{num1} es mayor que {num2}")
# elif num1 == num2:
#     print(f"{num1} y {num2} son iguales")
# else:
#     print(f"{num2} es mayor que {num1}")


edad = 18
tiene_licencia = True

if edad >= 18 and tiene_licencia is True:
    print("Puedes conducir")
elif edad >= 18 and tiene_licencia is False:
    print("No puedes conducir. Necesitas contar con una licencia")
else:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")

