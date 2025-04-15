"""

print("hola" == "Hola")

usuario_ingresado = input("Ingresa tu usuario: ")
contraseña_ingresada = input("Ingresa tu contraseña: ")

usuario_db = "checho123"
contraseña_db = "pupi456"

print( usuario_ingresado == usuario_db ) and ( contraseña_ingresada == contraseña_db )

"""
# rol_ingresado = input("Ingresa el rol que tenés: ")

# rol1 = "Administrador"
# rol2 = "Moderador"

# print( rol_ingresado == rol1 or rol_ingresado == rol2)

# num = 10

# if num == 5:
#     print("El número ingresado es correcto")
#     print(num*2)
#     print(num/2)
#     print(num**2)
   
#     print("Éstas son un conjunto de operaciones en donde opera al num con el 2")
# else:
#     print("El número es incorrecto")

usuario_ingresado = input("Ingresa tu usuario: ")
contraseña_ingresado = input("Ingresa tu contraseña: ")

usuario_db = "chech123"
contraseña_db = "pupi456"

if ((usuario_ingresado == usuario_db and contraseña_ingresado == contraseña_db)):
    print("Bienvenido, ingresaste correctamente")

else:
    print("Alguno de tus datos es incorrecto")
    if usuario_ingresado == usuario_db:
        print("Hola, ", usuario_ingresado, ", la contraseña que ingresaste es incorrecta")
    else:
        print("Esa cuenta no existe")