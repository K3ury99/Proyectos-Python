import os

#open('nombre_archivo', 'modo' -> 'x = crear', 'a = agregar', 'r = leer', 'w = escribir', 't = modo texto')
# creando el archivo
'''
archivo_nuevo = open('keury_Prueba_ITLA.txt', 'x')
print(f'El archivo plano {archivo_nuevo}, ha sido creado existosamente')
print('\n')
file = open('keury_Prueba_ITLA.txt', 'r')
print(file.read())
file.close()
'''

# Agregando info en el archivo
print('Agregando informacion en el archivo plano...')
file = open('keury_Prueba_ITLA.txt', 'a')
file.write('\nKeury Alberto Ramirez Capellan')
file.close()

# Leyendo el Archivo
print(f'Leyendo el archio {file}')
print('\n')
file = open('keury_Prueba_ITLA.txt','r')
print(file.read())
file.close()

# Leyendo el archivo linea a linea
'''
print(f'Leyendo el archivo {file} linea a linea')
file = open('keury_Prueba_ITLA.txt', 'r')
print(file.readline())
file.close()
'''

# Iterando el archivo plano linea a linea
'''
print('Iterando el archivo plano linea a linea')
f = open('keury_Prueba_ITLA.txt', 'r')
for registro in f:
    if registro.startswith('Pepito'):
        print(f'El nombre actual es: {registro}')
    else:
        print(f'El nombre especificado no existe en: {registro}')
'''

# Eliminando archivos
'''
os.remove('keury_Prueba_ITLA.txt')
'''

# Manejar archivos con gestor
try:
    with open('keury_Prueba_ITLA.txt', 'r+'):
        print(file.readline())
except FileNotFoundError:
    print('El archivo no existe')
finally:
    print('Ejecucion finalizada')


