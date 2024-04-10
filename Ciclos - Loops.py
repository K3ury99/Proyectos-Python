# Estructuras repetitivas
# Ciclos / Loops
# Son: While, for

# while
cont = 2
while cont <= 100:
    print(f'El valor del contador del While es: {cont}')
    cont += 1

# for
for i in range (1,100):
    print(f'El valor del For es: {i}')
print(range)

# Listas
lista = list(range(1,100,2))
print(lista)

# Variables
aux, factorial, resultado, numero = 0,0,0,0

# Factorial
factorial = int(input('Digite un numero'))
aux = factorial
while factorial >1:
    numero = aux * (factorial -1)
    resultado = numero
    aux = numero
    factorial -= 1
print(f'El factorial es: {numero}')


# Arreglos
colores = ['Azul', 'Amarillo', 'Blanco','Negro']
colorcito = input('Digite un colorcito ')
for k in colores:
    if k == colorcito:
        print(f'Tengo el color: {k}')
        continue
    else:
        print('No tengo ese colorcito {colorcito}')
    print(k)


# Listas
lista = ['amarillo', 'a2', 45, 34.56, True, [1,2,3]]
lista_numeros = list((1,2,3,4,5))
listica =[]
colores = ['Azul', 'Amarillo', 'Blanco','Negro']

resultado_lista = list(range(100))
#print(resultado_lista)
print(colores[2])
print(colores.index('Negro'))
print(colores)

colores[1] = 'Blanco'
colores.append('Blanco')
colores.extend(['violeta','purpura'])
colores.pop()
colores.remove()





