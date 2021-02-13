print("Hoja de trabajo 2")
print("Ejercicio 1")
contra = input("Ingrese una contraseña: ")
validar = input("Escriba de nuevo su contraseña: ")
if contra==validar:
    print("Las contraseñas coinciden.")
else:
    print("Las contraseñas no coinciden.")
print("Fin del ejercicio.")
print(" ")

print("Ejercicio 2")
nombre = input("Escribe tu nombre: ")
sexo = input("Escribe tu sexo: ")
if sexo == "Mujer" or sexo == "mujer":
        if nombre.lower() < "m":
            print("Usted se encuentra en el grupo A")
        else:
            print("Usted se encuentra en el grupo B")
else:
    if sexo == "Hombre" or sexo == "hombre":
        if nombre.lower() >"n":
            print("Usted se encuentra en el grupo A")
        else:
            print("Usted se encuentra en el grupo B")
print("Fin del ejercicio.")