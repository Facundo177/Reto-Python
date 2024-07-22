# El switch de python es match
""" 
match color:
    case "red":
        print("Rojo")
    case "yellow":
        print("Amarillo")
    case "green":
        print("Verde")
    case _:
        print("default")
"""





cantidad_usuarios_nuevos = int(input("¿Cuántos nuevos usuarios se desean registrar?: "))

for numero in range(1, cantidad_usuarios_nuevos+1):
    print("\nUsuario", numero)

    while True:
        nombres = input("Ingrese su/s nombre/s: ")
        if len(nombres) >= 5 and len(nombres) <= 50:
            break
        else:
            print("Debe estar entre 5 y 50 caracteres.")
    
    while True:
        apellidos = input("Ingrese su/s apellido/s: ")
        if len(apellidos) >= 5 and len(apellidos) <= 50:
            break
        else:
            print("Debe estar entre 5 y 50 caracteres.")
        
    while True:
        numero_telefono = input("Ingrese su número de teléfono: ")
        if len(numero_telefono) == 10:
            break
        else:
            print("Su longitud debe ser de 10 números.") 
        
    while True:
        correo = input("Ingrese su correo electrónico: ")
        if len(correo) >= 5 and len(correo) <= 50:
            break
        else:
            print("Debe estar entre 5 y 50 caracteres.")

    print("\nBienvenido", nombres, apellidos + ", en breve recibirás un correo a", correo) 
