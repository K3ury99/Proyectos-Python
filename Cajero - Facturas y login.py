# Saldo inicial.
saldo = 0

# Datos de usuario.
usuarios = ["keury", "Bernardo"]
cedulas = ["369", "123"]
cuentas = ["456", "123"]

# Factura / Historial de operaciones.
historial_operaciones = []

# Autenticacion de la persona.
while True:
    print("""
    ------------------------------------------------------------
    | $$  /$$/                      | $$                        
    | $$ /$$/   /$$$$$$   /$$$$$$  /$$$$$$    /$$$$$$  /$$   /$$
    | $$$$$/   /$$__  $$ /$$__  $$|_  $$_/   /$$__  $$|  $$ /$$/
    | $$  $$  | $$  \ $$| $$  \__/  | $$    | $$$$$$$$ \  $$$$/ 
    | $$\  $$ | $$  | $$| $$        | $$ /$$| $$_____/  >$$  $$ 
    | $$ \  $$|  $$$$$$/| $$        |  $$$$/|  $$$$$$$ /$$/\  $$
    |__/  \__/ \______/ |__/         \___/   \_______/|__/  \__/
    ------------------------------------------------------------
    """)

    usuario = input("Ingrese su usuario: ")
    cedula = input("Ingrese su cedula: ")
    cuenta = input("Ingrese su cuenta: ")

    if usuario in usuarios and cedula in cedulas and cuenta in cuentas:
        print("""
        -------------------------------------------------------
        Autenticación exitosa. Bienvenido al cajero automático.
        -------------------------------------------------------
        """)
        break
    else:
        print("Error de autenticación. Por favor, inténtelo nuevamente.")

# Operaciones del cajero automático.
while True:
    print("\n1. Consultar Saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir/Cerrar")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        print(f"""
        ----------------------
        Saldo actual: ${saldo}
        ----------------------
        """)
        historial_operaciones.append(f"| Consulto el saldo actual: ${saldo}")
    elif opcion == "2":
        cantidad = float(input("Ingrese la cantidad a depositar: "))
        if cantidad > 0:
            saldo += cantidad
            print(f"""
            ----------------------------------------
            Depósito exitoso. Saldo actual: ${saldo}
            ----------------------------------------
            """)
            historial_operaciones.append(f"| Depósito la Cantidad: ${cantidad}")
        else:
            print("Error: La cantidad debe ser mayor que cero.")
    elif opcion == "3":
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        if cantidad > 0 and cantidad <= saldo:
            saldo -= cantidad
            print(f"""
            --------------------------------------
            Retiro exitoso. Saldo actual: ${saldo}
            --------------------------------------
            """)
            historial_operaciones.append(f"| Retiro la Cantidad: ${cantidad}")
        elif cantidad <= 0:
            print("Error: La cantidad debe ser mayor que cero.")
        else:
            print("Error: Fondos insuficientes.")
    elif opcion == "4":
        print(f"""
 -------------------------------------------------
|                 FACTURA DE OPERACIONES            
 -------------------------------------------------
| ID Factura: 369369369369369369369                 
| Nombre: {usuario}                                
| Cedula: {cedula}                                 
| Cuenta: {cuenta}                                 
 -------------------------------------------------
 Historial de transacciones realizadas:
        """),
        for factura in historial_operaciones:
            print(factura),
            
        print("""
          /$$$$$$                               /$$                     /$$
         /$$__  $$                             |__/                    | $$
        | $$  \__/  /$$$$$$  /$$$$$$   /$$$$$$$ /$$  /$$$$$$   /$$$$$$$| $$
        | $$ /$$$$ /$$__  $$|____  $$ /$$_____/| $$ |____  $$ /$$_____/| $$
        | $$|_  $$| $$  \__/ /$$$$$$$| $$      | $$  /$$$$$$$|  $$$$$$ |__/
        | $$  \ $$| $$      /$$__  $$| $$      | $$ /$$__  $$ \____  $$    
        |  $$$$$$/| $$     |  $$$$$$$|  $$$$$$$| $$|  $$$$$$$ /$$$$$$$/ /$$
         \______/ |__/      \_______/ \_______/|__/ \_______/|_______/ |__/
        """)
        break
