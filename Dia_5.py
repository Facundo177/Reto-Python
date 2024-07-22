""" 

# Funciones
# Datos de entrada para una función = Argumentos -> Parámetros

def suma (number1, number2):
    result = number1 + number2
    return result, 10, 20


result, *_ = suma(50, 67)
print(result)



def set_scores():
    scores = []
    for option in range(0, 5):
        score = int( input('Ingresa una calificación: ') )
        scores.append(score)
    return scores


def average(numbers):
    return sum(numbers) / len(numbers)


def show_message(average):
    match average:
        case 10:
            print('Muchas felicidades, aprobaste la materia.')
        case 9 | 8:
            print('Aprobaste la materia.')
        case 7:
            print('Aprobaste la materia, pero necesitas practicar más.')
        case _:
            print('Lo sentimos, no aprobaste la materia.')


scores = set_scores()
avg = average(scores)
show_message(avg)

# show_message(average(set_scores()))

"""





id_ultimo_registro = 0
usuarios = {}


def new_user():
    global id_ultimo_registro
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


def show_user(id_usuario):
    print(f"\nUsuario {id_usuario}:\n", usuarios.get(id_usuario))


def edit_user(id_usuario):
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


def delete_user(id_usuario):
    usuarios.pop(id_usuario)
    print("\nUsuario eliminado")


def list_users():
    print("\nUsuarios registrados:", tuple(usuarios.keys()))


# Menú inicial
while True:
    print(""" 
Elige la opción que deseas realizar:
    1) Registrar nuevos usuarios
    2) Listar usuarios
    3) Ver la información de un usuario
    4) Editar un usuario
    5) Eliminar usuario
    6) Cerrar programa""")
    while True:
        opcion_elegida_del_menu = int(input("\nEscribe aquí el número: "))
        
        if 1 <= opcion_elegida_del_menu <= 6:
            break
        else:
            print("\nOpción no existente")
    
    match opcion_elegida_del_menu: 
        case 1:
            cantidad_usuarios_nuevos = int(input("\n¿Cuántos nuevos usuarios se desean registrar?: "))
            for numero in range(1, cantidad_usuarios_nuevos+1):
                new_user()
        case 2:
            list_users()
        case 3:
            id_usuario = int(input("\n¿Cuál usuario desea consultar?: "))
            show_user(id_usuario)
        case 4:
            id_usuario = int(input("\n¿Cuál usuario desea editar?: "))
            edit_user(id_usuario)
        case 5:
            id_usuario = int(input("\n¿Cuál usuario desea eliminar?: "))
            delete_user(id_usuario)
        case 6:
            break

