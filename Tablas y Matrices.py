
# Tablas y Matrices
nombre_tabla = [[],[]]
print(type(nombre_tabla))

# sub-lista (0) sub-lista (1)
tabla1 = [['Juan','Pedro','Abner'],[20,30,60]]

print('Vizualizando el primer elemento de la primera sub-lista')
print(tabla1[1][1])

# Recorrer la lista interactivamente por nombre de elementos
print('\n')
print('Recorriendo la fila completa y sub-lista')
for fila in tabla1:
    for columna in fila:
        print(columna)

# Recorrer la lista interactivamente por el indice de elementos
print('\n')
print('Recorriendo la fila completa y sub-lista por indice')
fila = 0
while fila < len(tabla1):
    columna = 0
    while columna < len(tabla1[fila]):
        print(tabla1[fila][columna])
        columna += 1
    fila += 1
    
# Recorrer la lista completa interactivamente por nombre con while.
print('\n')
print('Recorriendo la lista completa y sus parejas')
for i in range (len(tabla1)):
    for j in range (len(tabla1)):
        k = i + 1
        if k == 2:
            break
        print(f'Mi nombre es: {tabla1[i][j]} y mi edad es: {tabla1[k][j]}')


#====================================================
# Ejercicio practico de Tabla
#====================================================
# Creamos una tabla vacia
usuarios = [[],[]]
tamano = 2 #cantidad de usuarios

# Agregar datos desde el teclado a las tablas
for i in range (tamano):
    print('========================================')
    print('Ingresando los datos del usuario...', i+1)
    print('========================================')
    print('\n')
    nombre = input('Digite el nombre del usuario: ')
    cedula = input('Digite la cedula del usuario: ')

    # Agregar el nombre en la primera lista y la cedula en la segunda lista
    usuarios[0].append(nombre)
    
    usuarios[1].append(cedula)

# Vizualizando los datos de los usuarios
for i in range (tamano):
    print('\n')
    print('========================================')
    print('Vizualizando los datos del usuario: ', i+1)
    print('========================================')
    print('El nombre del usuario es: ', usuarios[0][i])
    print('La cedula del usuario es: ', usuarios[1][i])
print('\n\n')
print(f'Fin del ejercicio practico, cantidad de usuarios procesados: {len(usuarios[0])}')



















