import re #Caracteres especiales
import datetime #Fechas

# Funcion: Datos necesarios del cliente
def Datos_del_vehiculo():
    while True:
        nombre = input("Ingrese nombre del cliente: ")
        if nombre.strip() == '':
            print("Por favor, ingrese el nombre del cliente.")
            continue

        cedula = input("Ingrese su cédula: ")
        if cedula.strip() == '':
            print("Por favor, ingrese la cédula del cliente.")
            continue

        celular = input("Ingrese su número de celular: ")
        if celular.strip() == '':
            print("Por favor, ingrese el número de celular del cliente.")
            continue
        
        while True: # Esto hace que se necesite obligatoriamente '@' y '.' en el correo
            email = input("Ingrese su correo electrónico: ")
            if email.strip() == '':
                print("Por favor, ingrese el correo electrónico del cliente.")
                continue
            elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                print("El correo electrónico ingresado no es válido. Use '@gmail.com'")
                continue
            else:
                break

        marca = input("Ingrese la marca de su vehículo: ")
        if marca.strip() == '':
            print("Por favor, ingrese la marca del vehículo.")
            continue

        modelo = input("Ingrese el modelo de su vehículo: ")
        if modelo.strip() == '':
            print("Por favor, ingrese el modelo del vehículo.")
            continue

        año = input("Ingrese el año de su vehículo: ")
        if año.strip() == '':
            print("Por favor, ingrese el año del vehículo.")
            continue
        break
    # Devuelve los valores
    return {
        "nombre": nombre,
        "cedula": cedula,
        "celular": celular,
        "email": email,
        "marca": marca,
        "modelo": modelo,
        "año": año
    }

# Comienza a realizar las operaciones
def realizar_operaciones():
    operaciones_realizadas = []
    precios = {
        1: 1500,
        2: 2000,
        3: 2500,
        4: 1000,
        5: 4500,
        6: 750,
        7: 2000,
        8: 5000,
        9: 3200
    }

    while True: # Mostrando opciones a solicitar
        print("\n--- Menú ---")
        print("1. Cambio de Aceite del motor: $1500")
        print("2. Cambio de Filtro: $2000")
        print("3. Cambio de Aceite y Filtro: $2500")
        print("4. Compra y Cambio de Batería: $1000")
        print("5. Compra de Neumáticos: $4500")
        print("6. Cambio de Neumático: $750")
        print("7. Reparación Menor: $2000")
        print("8. Reparación Mayor: $5000")
        print("9. Pintura de Vehículo: $3200")
        print("0. Salir del sistema")

        try:
            opcion = int(input("Ingrese la opción deseada: "))
            if opcion == 0:
                break
            elif opcion not in range(1, 10):
                print("Opción no válida. Por favor, elija una opción del menú.")
                continue

            operaciones_realizadas.append(opcion)
            print("Operación realizada.")
        except ValueError:
            print("Error: Ingrese un número válido.")
    return operaciones_realizadas, precios

# Guardando los valores introducidos
def Guardar_datos(cliente, operaciones, precios):
    print("\nDatos del cliente:")
    print("Nombre:", cliente["nombre"])
    print("Cédula:", cliente["cedula"])
    print("Celular:", cliente["celular"])
    print("Email:", cliente["email"])
    print("Marca:", cliente["marca"])
    print("Modelo:", cliente["modelo"])
    print("Año:", cliente["año"])
    print("\nOperación solicitada:")
    for operacion in operaciones:
        print("Selección ---> ", operacion)
    total_pagar = sum(precios[op] for op in operaciones)
    print("\nTotal de operaciones realizadas:", len(operaciones))
    print("Total a pagar: $", total_pagar)

# Exportar datos a TXT y editando el texto exportado para crear una especie de factura
def exportacion_TXT(cliente, operaciones, precios):
    with open("Resultados_ultimo_parcial.txt", "a", encoding="utf-8") as archivo:
        archivo.write("""
    ██╗  ██╗ ██████╗ ██████╗ ████████╗███████╗██╗  ██╗
    ██║ ██╔╝██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝╚██╗██╔╝
    █████╔╝ ██║   ██║██████╔╝   ██║   █████╗   ╚███╔╝ 
    ██╔═██╗ ██║   ██║██╔══██╗   ██║   ██╔══╝   ██╔██╗ 
    ██║  ██╗╚██████╔╝██║  ██║   ██║   ███████╗██╔╝ ██╗
    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
        """)
        archivo.write(f"""\n
        -------------------------------------------
                    DATOS DEL CLIENTE 
                    FECHA: {datetime.date.today()}
        -------------------------------------------
        \n""")
        archivo.write(f"        Nombre: {cliente['nombre']}\n")
        archivo.write(f"        Cedula: {cliente['cedula']}\n")
        archivo.write(f"        Celular: {cliente['celular']}\n")
        archivo.write(f"        Email: {cliente['email']}\n")
        archivo.write(f"        Marca: {cliente['marca']}\n")
        archivo.write(f"        Modelo: {cliente['modelo']}\n")
        archivo.write(f"        Año: {cliente['año']}\n\n")
        archivo.write("""
        -------------------------------------------
                    OPERACIONES REALIZADAS
        -------------------------------------------
        """)
        for operacion in operaciones:
            archivo.write(f"\n              ---> {operacion}\n")
        total_pagar = sum(precios[op] for op in operaciones)
        archivo.write(f"""
        -------------------------------------------
                TOTAL DE OPERACIONES REALIZADAS:
                ---> {len(operaciones)}
        -------------------------------------------
        """)
        archivo.write(f"""
        -------------------------------------------
                    TOTAL A PAGAR:
                    ---> ${total_pagar}
        -------------------------------------------
        """)

# Inicio de todas las funciones declaradas y repeticion, pudiendo agregar tantos clientes como se requiera y almacenandolos en un TXT.
while True:
    print("""
    ██╗  ██╗ ██████╗ ██████╗ ████████╗███████╗██╗  ██╗
    ██║ ██╔╝██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝╚██╗██╔╝
    █████╔╝ ██║   ██║██████╔╝   ██║   █████╗   ╚███╔╝ 
    ██╔═██╗ ██║   ██║██╔══██╗   ██║   ██╔══╝   ██╔██╗ 
    ██║  ██╗╚██████╔╝██║  ██║   ██║   ███████╗██╔╝ ██╗
    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
    """)

    datos_cliente_vehiculo = Datos_del_vehiculo()

    operaciones_realizadas, precios_servicios = realizar_operaciones()

    Guardar_datos(datos_cliente_vehiculo, operaciones_realizadas, precios_servicios)

    exportacion_TXT(datos_cliente_vehiculo, operaciones_realizadas, precios_servicios)

    continuar = input("¿Desea continuar con otro cliente? (Si/No): ")
    if continuar.lower() != 'si':
        break

# CREDITOS: KEURY RAMIREZ, MATRICULA: 2023-1101