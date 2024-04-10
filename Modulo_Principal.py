import datetime
import modulo_principal

print('La fecha de hoy es: ', datetime.datetime.now()) #Nos dice la fecha y hora actual.


# Funciones constantes.
def sumar (num1,num2):
    print(f'\nLa suma de {num1} y {num2} es: ', (num1+num2))

def restar (num1,num2):
    print(f'\nLa resta de {num1} y {num2} es: ', (num1-num2))

def multiplicar (num1,num2):
    print(f'\nLa multiplicacion de {num1} y {num2} es: ', (num1*num2))

def dividir (num1,num2):
    print(f'\nLa division de {num1} y {num2} es: ', (num1/num2))


# Menu

while True:
    print(
        f'''
        ================= Menú Principal =================
        1. - Visualizando la fecha actual
        2. - Sumar 2 números
        3. - Restar 2 números
        4. - Multiplicar 2 números
        5. - Dividir 2 números
        0. - Salir
        ==================================================
        ''')
    try:
        opcion = int(input('Ingrese una opción del menú: '))
    except ValueError:
        print('Opcion no válida. Por favor, ingrese una opción')
    else:
        if opcion == 1:
            print('La fecha actual es: ', datetime.datetime.now())
        elif opcion == 2:
            num1 = int(input('Ingrese el primer número: '))
            num2 = int(input('Ingrese el segundo número: '))
            modulo_principal.sumar(num1,num2)
        elif opcion == 3:
            num1 = int(input('Ingrese el primer número: '))
            num2 = int(input('Ingrese el segundo número: '))
            modulo_principal.restar(num1,num2)
        elif opcion == 4:
            num1 = int(input('Ingrese el primer número: '))
            num2 = int(input('Ingrese el segundo número: '))
            modulo_principal.multiplicar(num1,num2)
        elif opcion == 5:
            num1 = int(input('Ingrese el primer número: '))
            num2 = int(input('Ingrese el segundo número: '))
            modulo_principal.dividir(num1,num2)
        elif opcion == 0:
            break
        else:
            print('Opcion no válida. Por favor, ingrese una opción')










