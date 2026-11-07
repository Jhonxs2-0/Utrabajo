estudiantes = []

def ingresar_estudiante():
    nombre = input("Nombre del estudiante: ")
    
    nota = float(input("Nota del estudiante (1 a 5): "))
    while nota < 1 or nota > 5:
        print("La nota debe estar entre 1 y 5.")
        nota = float(input("Ingresa la nota nuevamente: "))
    
    if nota >= 3.0:
        estado = "Aprobado"
    else:
        estado = "Reprobado"
        
    estudiante = {
        "nombre": nombre,
        "nota": nota,
        "estado": estado
    }
    
    estudiantes.append(estudiante)
    print("Estudiante guardado.")

def mostrar_estudiante():
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        for est in estudiantes:
            print("Nombre:", est["nombre"], "- Nota:", est["nota"], "- Estado:", est["estado"])

def estadistica_estudiantil():
    if len(estudiantes) == 0:
        print("No hay datos para mostrar.")
    else:
        total = len(estudiantes)
        suma = 0
        aprobados = 0
        reprobados = 0
        mayor = estudiantes[0]["nota"]
        menor = estudiantes[0]["nota"]

        for est in estudiantes:
            suma += est["nota"]
            
            if est["nota"] > mayor:
                mayor = est["nota"]
            if est["nota"] < menor:
                menor = est["nota"]
                
            if est["estado"] == "Aprobado":
                aprobados += 1
            else:
                reprobados += 1

        promedio = suma / total

        print("Total estudiantes:", total)
        print("Promedio:", promedio)
        print("Nota mayor:", mayor)
        print("Nota menor:", menor)
        print("Aprobados:", aprobados)
        print("Reprobados:", reprobados)

while True:
    print("\n1. Ingresar estudiante")
    print("2. Mostrar estudiante")
    print("3. Estadística estudiantil")
    print("4. Salir")
    
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        ingresar_estudiante()
    elif opcion == "2":
        mostrar_estudiante()
    elif opcion == "3":
        estadistica_estudiantil()
    elif opcion == "4":
        print("Fin del programa.")
        break
    else:
        print("Opcion no valida.")