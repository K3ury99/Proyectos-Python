# Mensaje de seleccion
while True:
    print(
    """
    ============== Menu de Operaciones ==============
    1.Suma
    2.Resta
    3.Multiplicación
    4.División
    5.Division Exacta
    6.Potencia
    7.Modulo
    0.Cerrar
    ==================== Fin menu ===================
    """)

    # Variables
    operacion = (int(input('Seleccione la operación a realizar:')))
    # Operaciones
    if operacion ==0:
        print('Gracias por utilizar nuestros sistema')
        break
    else:
        num1 = (int(input('Introduzca el primer numero.')))
        num2 = (int(input('Introduzca el segundo numero.')))


    # Inicio
        match operacion:
            case 1:
                print('El resultado de la suma es', num1+num2)
            case 2:
                print('El resultado de la resta es', num1-num2)
            case 3:
                if (num1 != 0):
                    print('El resultado de la Multiplicación es', num1*num2)  
                else:
                    print('No se puede Multiplicar Por cero')     
            case 4:
                if (num1 != 0):
                    print('El resultado de la división es', num1/num2)
                else:
                    print('No se puede dividir entre cero')
            case 5:
                print('El resultado de la Division Exacta es', num1//num2)
            case 6:
                print('El resultado de la Potencia es', num1**num2)
            case 7:
                if (num1==0 and num2==0):
                    print('El resultado de la Modulo es', num1%num2)
                else:
                    print('Error calculo')
            case 0:
                break
            case _:
                print('La operacion elegida es invalida')





