# Listas = Estructura de datos.
# append, insert, extend, remove, count, index
# Índices

""" 

courses = ['Python', 'Django', 'Flask', 'Ruby', 'Ruby on Rails', 'Rust', 'C#']
new_courses = ['Java9', 'Docker', 'Unix']

courses.extend( new_courses )

courses.remove('Python')
courses.remove('Flask')
courses.remove('C#')

print( 'Laravel' in courses )
print( courses.count('Laravel') >= 1)

print( courses.index('Laravel') )
print (courses)

if value in courses:
    print('El índice es: ' + str(courses.index(value)))
else:
    print('Lo sentimos, el valor no existe dentro del listado.')

for course in courses:
    print(course)

for index, course in enumerate(courses):
    print('El valor para el índice', index, 'es', course)


message = 'Hola mundo'
new_message = 'P' + message[1:]
print( new_message )

"""




cantidad_usuarios_nuevos = int(input("¿Cuántos nuevos usuarios se desean registrar?: "))
ids_usuarios = []

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
    ids_usuarios.append(numero)

print("\nUsuarios registrados:", ids_usuarios)
