def registrar_usuario(nombre, apellidos, ciudad, edad, cedula):
    with open('registro_usuarios.txt', 'a') as f:
        f.write(f"Nombre: {nombre}, Apellidos: {apellidos}, Ciudad: {ciudad}, Edad: {edad}, Cedula: {cedula}\n")
    print(f"Usuario {nombre} registrado correctamente.")

def mostrar_registros():
    try:
        with open('registro_usuarios.txt', 'r') as f:
            registros = f.readlines()
            if registros:
                for registro in registros:
                    print(registro.strip())
            else:
                print("No hay usuarios registrados.")
    except FileNotFoundError:
        print("No hay usuarios registrados.")
