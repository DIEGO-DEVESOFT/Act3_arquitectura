from funciones import registrar_usuario, mostrar_registros

def iniciar():
    print("=== Sistema de Registro de Usuarios ===")
    
    while True:
        nombre = input("Ingresa tu nombre: ")
        apellidos = input("Ingresa tus apellidos: ")
        ciudad = input("Ingresa tu ciudad: ")
        edad = input("Ingresa tu edad: ")
        cedula = input("Ingresa tu cédula: ")
        
        registrar_usuario(nombre, apellidos, ciudad, edad, cedula)
        print("Registro completado con éxito.")

        continuar = input("¿Deseas registrar otra persona? (s/n): ").lower()
        if continuar != 's':
            print("\nLista de usuarios registrados:")
            mostrar_registros()
            print("Saliendo del sistema de registro.")
            break

if __name__ == "__main__":
    iniciar()
