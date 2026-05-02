import os

file_path = os.path.dirname(os.path.abspath(__file__))
c_patients = os.path.join(file_path, "patients")
c_his = os.path.join(file_path, "his")
path_salida = os.path.join(c_his, "hce.txt")
os.makedirs(c_his, exist_ok=True)

def analizar_archivo(ruta, id_paciente):
    with open(ruta, "r", encoding="utf-8") as arc:
        for linea in arc:
            linea = linea.strip().lstrip("¬")  
            if linea.startswith("3O|"):
                partes = linea.split("|")

                fecha_nacimiento = partes[3].split("-")[3]  
                fecha_nacimiento = f"{fecha_nacimiento[:4]}-{fecha_nacimiento[4:6]}-{fecha_nacimiento[6:]}"
                nombre_completo = partes[4].split("^")[1]
                partes_nombre = nombre_completo.strip().split(" ", 1)
                nombre   = partes_nombre[0]
                apellido = partes_nombre[1]
                edad   = partes[7]
                eps    = partes[6]
                genero = partes[-1].strip()  

                return f"|{id_paciente}|{nombre}|{apellido}|{edad}|{genero}|{fecha_nacimiento}|{eps}|\n"

####
archivos = []
for i in os.listdir(c_patients) :
    if i.endswith(".txt"):
        archivos.append(os.path.join(c_patients, i))

with open(path_salida, "w", encoding="utf-8") as salida:
    salida.write("|Id|Nombre|Apellido|Edad|Género|FechaNacimiento|EPS\n")

    i = 1
    for archivo in archivos:
        linea = analizar_archivo(archivo, i)
        if linea:
            salida.write(linea)
            print(f"Archivo procesado exitosamente: {os.path.basename(archivo)}")
            i += 1
        else:
            print(f"No se encontró información en el archivo: {os.path.basename(archivo)}")

print(f"\nArchivo guardado en: {path_salida}")
