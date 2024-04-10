# - Crear un diccionario.
usuarios = {
    'id': [],
    'Nombre': [],
    'Celular': [],
    }
# - Constante tamano del diccionario.
tamano = 3

# - Leemos los datos a ingresar por teclado
for i in range (tamano):
    print('======== Iniciando ==========')
    print('Por favor ingrese los datos de la persona', i+1)
    print('=============================')
    id = input('IDs: ')
    nombre = input('Nombres: ')
    celular = input('No. Celular: ')

# - Agregar los datos al diccionario
    usuarios['id'].append(id)
    usuarios['Nombre'].append(nombre)
    usuarios['Celular'].append(celular)

# - Mostrar datos
for i in range (tamano):
    print('============== imprimiendo los datos de la persona: ', i+1,'================')
    print('ID: ', usuarios['id'][i])
    print('Nombre: ', usuarios['Nombre'][i])
    print('Celular: ', usuarios['Celular'][i])
print('================= Finalizado ===================')
