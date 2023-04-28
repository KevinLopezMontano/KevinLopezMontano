
pacientes = {}

def mostrar_menu():
    print("1. Añadir paciente")
    print("2. Buscar paciente")
    print("3. Eliminar paciente")
    print("4. Ver lista de pacientes")
    print("5. Salir")

while True:
   
    mostrar_menu()

    
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        nombre = input("Ingrese el nombre del paciente: ")
        codigo = input("Ingrese el código del paciente: ")
        pacientes[codigo] = nombre
        print("Paciente añadido correctamente.")

    elif opcion == "2":
        codigo = input("Ingrese el código del paciente: ")
        if codigo in pacientes:
            print("Nombre del paciente: ", pacientes[codigo])
        else:
            print("No se encontró ningún paciente con ese código.")

    elif opcion == "3":
        codigo = input("Ingrese el código del paciente: ")
        if codigo in pacientes:
            del pacientes[codigo]
            print("Paciente eliminado correctamente.")
        else:
            print("No se encontró ningún paciente con ese código.")
            
    elif opcion == "4":
        if pacientes:
            print("Lista de pacientes:")
            for codigo, nombre in pacientes.items():
                print(codigo, "-", nombre)
        else:
            print("No hay pacientes registrados.")

    elif opcion == "5":
        print("¡Hasta pronto!")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.") 
