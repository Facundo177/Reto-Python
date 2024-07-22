""" 
# Desempaquetado de tuplas

settings = ('localhost', 3306, 'root', 'password', 'database')

# host, port, _, _, _ = settings
host, port, *_ = settings

print (host, port)

host, *_, password, database = settings

print (host, password, database)



tuples = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

for _tuple in tuples:
    for number in _tuple:
        print(number)


for numberl, number2, number3 in tuples:
    print(number1, number2, number3)





# Llave != String - Llaves = Objetos inmutables (String, Enteros, Flotantes, Bool, Tuplas)
user = {
    'name': 'Cody',
    'age': 10,
    'email': 'info@codigofacilito.com',
    'active': True
}

print( user['active'] )

value = user.get("name")    # Evita errores

# keys, values, items

print(tuple(user.items()))

for key, value in tuple(user.items()):
    print(key + ":", value)

"""






id_ultimo_registro = 0
usuarios = {}

# Menú inicial
while True:
    
    while True:
        opcion_elegida_del_menu = int(input(""" 
Elige la opción que deseas realizar:
    1) Registrar nuevos usuarios
    2) Listar usuarios
    3) Ver la información de un usuario
    4) Editar un usuario
    5) Cerrar programa
        
Escribe aquí el número: """))
        
        if 1 <= opcion_elegida_del_menu <= 5:
            break
        else:
            print("\nOpción no existente")
    
    if opcion_elegida_del_menu == 1: 
        cantidad_usuarios_nuevos = int(input("¿Cuántos nuevos usuarios se desean registrar?: "))
        
        for numero in range(1, cantidad_usuarios_nuevos+1):
            id_ultimo_registro += 1
            print("\nUsuario", id_ultimo_registro)

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
            
            usuario = {
                "nombre": nombres,
                "apellido": apellidos,
                "numero_de_telefono": numero_telefono,
                "correo": correo
            }
            
            usuarios[id_ultimo_registro] = usuario.copy()
            
    elif opcion_elegida_del_menu == 2:
        print("\nUsuarios registrados:", tuple(usuarios.keys()))
    elif opcion_elegida_del_menu == 3:
        id_usuario = int(input("¿Cuál usuario desea consultar?: "))
        print(f"\nUsuario {id_usuario}:\n", usuarios.get(id_usuario))
    elif opcion_elegida_del_menu == 4:
        id_usuario = int(input("¿Cuál usuario desea editar?: "))
        
        print("\nUsuario", id_usuario)
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
        
        usuario = {
            "nombre": nombres,
            "apellido": apellidos,
            "numero_de_telefono": numero_telefono,
            "correo": correo
        }
        
        usuarios[id_usuario] = usuario.copy()
        
        print("\nUsuario editado correctamente") 
        
    else:
        break
