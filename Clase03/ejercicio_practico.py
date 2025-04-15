comienzo = "Ingrese su "
nombre = input(comienzo+"nombre: ")
apellido = input(comienzo+"apellido: ")
edad = int(input(comienzo+"edad: "))
correo_electronico = input(comienzo+"correo electrónico: ")

if nombre == "":
    print("ERROR, el nombre está vacío")
else:
    print(nombre)
    
if apellido == "":
    print("ERROR, el apellido está vacío")
else:  
    print(apellido)

if not (edad > 18):
    print("ERROR, menor de 18 años")
else:
    print(edad)

if correo_electronico == "":
    print("ERROR, el correo electrónico está vacío")
else:
    print(correo_electronico)