# Saldo inicial
saldo = 0

# Datos de usuario
usuario_valido = "keury"
contrasena_valida = "369"

# Función de autenticación
def autenticar_usuario():
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
        contrasena = input("Ingrese su cedula: ")

        if usuario == usuario_valido and contrasena == contrasena_valida:
            print("""
            -------------------------------------------------------
            Autenticación exitosa. Bienvenido al cajero automático.
            -------------------------------------------------------
                    """)
            return True
        else:
            print("Error de autenticación. Por favor, inténtelo nuevamente.")

            

# Funciones de operaciones del cajero automático
# Consultar el saldo disponible
def consultar_saldo():
    global saldo
    print(f"""
        ----------------------
        Saldo actual: ${saldo}
        ----------------------
            """)
# Deposito
def depositar():
    global saldo
    cantidad = float(input("Ingrese la cantidad a depositar: "))
    if cantidad > 0:
        saldo += cantidad
        print(f"""
        ----------------------------------------
        Depósito exitoso. Saldo actual: ${saldo}
        ----------------------------------------
                """)
    else:
        print("Error: La cantidad debe ser mayor que cero.")
        
# Retiro
def retirar():
    global saldo
    cantidad = float(input("Ingrese la cantidad a retirar: "))
    if cantidad > 0 and cantidad <= saldo:
        saldo -= cantidad
        print(f"""
        --------------------------------------
        Retiro exitoso. Saldo actual: ${saldo}
        --------------------------------------
        """)
    elif cantidad <= 0:
        print("Error: La cantidad debe ser mayor que cero.")
    else:
        print("Error: Fondos insuficientes.")

# Autenticación del usuario
if autenticar_usuario():
    
    # Operaciones del cajero automático
    while True:
        print("\n1. Consultar Saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir/Cerrar")

        opcion = input("Seleccione una opción (1-4): ")
        
        match opcion:
            case "1":
                consultar_saldo()
            case "2":
                depositar()
            case "3":
                retirar()
            case "4":
                print("""
-------------------------------------------------------------------
  /$$$$$$                               /$$                     /$$
 /$$__  $$                             |__/                    | $$
| $$  \__/  /$$$$$$  /$$$$$$   /$$$$$$$ /$$  /$$$$$$   /$$$$$$$| $$
| $$ /$$$$ /$$__  $$|____  $$ /$$_____/| $$ |____  $$ /$$_____/| $$
| $$|_  $$| $$  \__/ /$$$$$$$| $$      | $$  /$$$$$$$|  $$$$$$ |__/
| $$  \ $$| $$      /$$__  $$| $$      | $$ /$$__  $$ \____  $$    
|  $$$$$$/| $$     |  $$$$$$$|  $$$$$$$| $$|  $$$$$$$ /$$$$$$$/ /$$
 \______/ |__/      \_______/ \_______/|__/ \_______/|_______/ |__/
-------------------------------------------------------------------
""") or exit()
                

        
