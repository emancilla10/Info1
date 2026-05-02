import os

file_path = os.path.dirname(os.path.abspath(__file__))
path_salida = os.path.join(file_path, "salida.txt")

def ingresar_paciente():
    print("\nIngrese la información del paciente")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")

    try:
        with open(path_salida, "r") as arc:
            lineas = arc.readlines()
            id_paciente = len([l for l in lineas if l.strip()]) + 1
    except FileNotFoundError:
        id_paciente = 1

    with open(path_salida, "a") as arc:
        arc.write(f"{id_paciente}|{nombre}|{apellido}|{edad}|\n")
    print("Paciente guardado.")
    
def ver_informacion():
    try:
        with open(path_salida, "r") as arc:
            print("\nInformación pacientes:")
            print(arc.read())
    except FileNotFoundError:
        print("\nEl archivo no existe aún.")

while True:
    print("\nMENÚ")
    print("1. Ingresar información de paciente")
    print("2. Ver información en archivo")
    print("3. Salir")
    
    opcion = input("Seleccione una opción (1-3): ").strip()
    
    if opcion == "1":
        ingresar_paciente()
    elif opcion == "2":
        ver_informacion()
    elif opcion == "3":
        print(f"\nArchivo guardado en: {path_salida}")
        print("Saliendo...")
        break
    else:
        print("Opción inválida. Seleccione 1, 2 o 3.")
