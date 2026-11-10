inventario = [
    {
        "id": 1,
        "nombre": "Sensor Ultrasonico HC-SR04",
        "categoria": "Sensores",
        "stock": 10,
        "precio_unitario": 2.50
    },
    {
        "id": 2,
        "nombre": "Servomotor SG90",
        "categoria": "Actuadores",
        "stock": 25,
        "precio_unitario": 1.75
    },
    {
        "id": 3,
        "nombre": "Arduino Uno R3",
        "categoria": "Microcontroladores",
        "stock": 8,
        "precio_unitario": 12.0
    }
]


opcion = ""

while opcion != "4":
    print("\n--- MENU DE GESTION DEL LABORATORIO ---")
    print("1. Registrar componente")
    print("2. Consultar y filtrar")
    print("3. Actualizar stock")
    print("4. Salir")
    
    opcion = input("Elige una opcion (1-4): ")

    if opcion == "1":
        print("\n--- REGISTRAR COMPONENTE ---")
        nuevo_id = int(input("Ingresa el ID: "))
        
     
        id_repetido = False
        for item in inventario:
            if item["id"] == nuevo_id:
                id_repetido = True
                break
        
        if id_repetido:
            print("Error: Ya existe un componente con ese ID.")
        else:
            nombre = input("Nombre del componente: ")
            categoria = input("Categoria (Sensores / Actuadores / Microcontroladores): ")
            stock = int(input("Stock inicial: "))
            precio = float(input("Precio unitario: "))
            
            nuevo_componente = {
                "id": nuevo_id,
                "nombre": nombre,
                "categoria": categoria,
                "stock": stock,
                "precio_unitario": precio
            }
            inventario.append(nuevo_componente)
            print("Componente registrado con exito.")

   
    elif opcion == "2":
        print("\n--- CONSULTAR INVENTARIO ---")
        print("a. Ver todos los componentes")
        print("b. Filtrar por categoria")
        sub_opcion = input("Selecciona una opcion (a/b): ")
        
        if sub_opcion == "a":
            print("\n--- TODOS LOS COMPONENTES ---")
            for item in inventario:
                print(f"ID: {item['id']} | Nombre: {item['nombre']} | Categoria: {item['categoria']} | Stock: {item['stock']} | Precio: ${item['precio_unitario']}")
        
        elif sub_opcion == "b":
            cat_buscar = input("Ingresa la categoria a buscar: ")
            print(f"\n--- COMPONENTES DE LA CATEGORIA: {cat_buscar} ---")
            encontrados = False
            for item in inventario:
                if item["categoria"].lower() == cat_buscar.lower():
                    print(f"ID: {item['id']} | Nombre: {item['nombre']} | Stock: {item['stock']} | Precio: ${item['precio_unitario']}")
                    encontrados = True
            
            if not encontrados:
                print("No se encontraron componentes en esa categoria.")
        else:
            print("Opcion invalida.")

    
    elif opcion == "3":
        print("\n--- ACTUALIZAR STOCK ---")
        id_buscar = int(input("Ingresa el ID del componente a actualizar: "))
        
        encontrado = False
        for item in inventario:
            if item["id"] == id_buscar:
                encontrado = True
                print(f"Componente seleccionado: {item['nombre']}")
                print(f"Stock actual: {item['stock']}")
                
                cambio = int(input("Ingresa cantidad a sumar (+) o restar (-): "))
                
                
                if item["stock"] + cambio < 0:
                    print("Error: El stock no puede ser negativo.")
                else:
                    item["stock"] = item["stock"] + cambio
                    print(f"Stock actualizado. Nuevo stock: {item['stock']}")
                break
        
        if not encontrado:
            print("Error: No se encontro ningun componente con ese ID.")

    elif opcion == "4":
        print("Saliendo del programa...")
        
    else:
        print("Opcion no valida, intenta de nuevo.")