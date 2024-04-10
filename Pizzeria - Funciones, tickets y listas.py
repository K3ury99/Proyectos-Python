# Pizzeria KORTEX
print("""
██╗  ██╗ ██████╗ ██████╗ ████████╗███████╗██╗  ██╗
██║ ██╔╝██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝╚██╗██╔╝
█████╔╝ ██║   ██║██████╔╝   ██║   █████╗   ╚███╔╝ 
██╔═██╗ ██║   ██║██╔══██╗   ██║   ██╔══╝   ██╔██╗ 
██║  ██╗╚██████╔╝██║  ██║   ██║   ███████╗██╔╝ ██╗
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
""")


# Usuarios
cola = []

# Precios de las pizzas
precio_pizza_margarita = 850
precio_pizza_pepperoni = 950
precio_pizza_hawaiana = 1250
precio_pizza_pollobbq = 1350
precio_pizza_cuatroquesos = 1700

# Inicio
while cola != None:
    
    # Menu
    print("\nMenú de Pizzas:")
    print("1. Margarita - $", precio_pizza_margarita)
    print("2. Pepperoni - $", precio_pizza_pepperoni)
    print("3. Hawaiana - $", precio_pizza_hawaiana)
    print("4. Pollo BBQ - $", precio_pizza_pollobbq)
    print("5. Cuatro Quesos - $", precio_pizza_cuatroquesos)

    # Personas
    cola.append(input("\nBienvenido, Ingrese su nombre: "))

    # Dinero disponible
    dinero_usuario = float(input("\nIngrese la cantidad de dinero disponible: $"))

    # Elegir la pizza
    opcion_pizza = int(input("\nSeleccione el número de la pizza que desea (1-5): "))
    if opcion_pizza == 1:
        pizza_elegida = "Margarita"
        precio_total = precio_pizza_margarita
    elif opcion_pizza == 2:
        pizza_elegida = "Pepperoni"
        precio_total = precio_pizza_pepperoni
    elif opcion_pizza == 3:
        pizza_elegida = "Hawaiana"
        precio_total = precio_pizza_hawaiana
    elif opcion_pizza == 4:
        pizza_elegida = "Pollo BBQ"
        precio_total = precio_pizza_pollobbq
    elif opcion_pizza == 5:
        pizza_elegida = "Cuatro Quesos"
        precio_total = precio_pizza_cuatroquesos
    else:
        print("Opción no válida. Por favor, elija una pizza válida.")
        continue

    print(f"\nHa elegido la pizza {pizza_elegida}. El total hasta ahora es: ${precio_total:.2f}")

    # Añadir ingredientes extras
    ingredientes_extras = []
    precio_extra_queso = 25
    precio_extra_jamon = 30
    precio_extra_pina = 50
    precio_extra_pollo = 60
    precio_extra_champinones = 75

    # Añadir Impuestos, totales y cambio
    itbis = dinero_usuario * 0.18 
    propinas = dinero_usuario * 0.10
    precio_final = precio_total + itbis + propinas
    cambio_total = dinero_usuario - precio_final

    
    while True:
        agregar_ingrediente = input("\n¿Desea agregar un ingrediente extra? (si/no): ").lower()
        
        if agregar_ingrediente == "si":
            print("Ingredientes Extras:")
            print("1. Queso - $", precio_extra_queso)
            print("2. Jamón - $", precio_extra_jamon)
            print("3. Piña - $", precio_extra_pina)
            print("4. Pollo - $", precio_extra_pollo)
            print("5. Champiñones - $", precio_extra_champinones)

            opcion_ingrediente = int(input("Seleccione el número del ingrediente que desea (1-5): "))
            if opcion_ingrediente == 1:
                ingredientes_extras.append("Queso")
                precio_total += precio_extra_queso
            elif opcion_ingrediente == 2:
                ingredientes_extras.append("Jamón")
                precio_total += precio_extra_jamon
            elif opcion_ingrediente == 3:
                ingredientes_extras.append("Piña")
                precio_total += precio_extra_pina
            elif opcion_ingrediente == 4:
                ingredientes_extras.append("Pollo")
                precio_total += precio_extra_pollo
            elif opcion_ingrediente == 5:
                ingredientes_extras.append("Champiñones")
                precio_total += precio_extra_champinones
            else:
                print("Opción no válida. Por favor, elija un ingrediente válido.")
        elif agregar_ingrediente == "no":
            break
        else:
            print("Por favor, responda con 'si' o 'no'.")
        
    
    
    # Ticket
    print(f'''
    ----------------------------------------------------------
                    FACTURA DE LA PIZZERIA.
    ----------------------------------------------------------
        Gracias por venir señor/a: {cola[-1]}
        Pizza solicitada: {pizza_elegida}
        Ingrendientes adicionales: {ingredientes_extras[:]}
    ----------------------------------------------------------
                    IMPUESTOS INCLUIDOS
    ----------------------------------------------------------
        ITBIS: ${itbis:.2f}
        PROPINAS: ${propinas:.2f}
    ----------------------------------------------------------
        TOTAL: ${precio_final:.2f}
        CAMBIO: ${cambio_total:.2f}
    ----------------------------------------------------------
                    GRACIAS POR VISITARNOS!
    ----------------------------------------------------------
    ''')

    print('¿Desea continuar?')
    continuar = input('(Si) / (No) ---> ').lower()
    if continuar != 'si':
        print('Gracias por preferirinos!')
        break

