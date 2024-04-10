# Encriptador de mensaje de texto

# propiedades
data: str
texto: str

# Funcion de encriptar
def encriptar(texto):
    textofinal = ' '
    print('\nEsta funcion encripta el siguiente texto: ', texto)
    for letra in texto:
        textofinal += letra + 'f'
    print('El dato encriptado es: ', textofinal)
    print('\n')

# Funcion de desencriptar
def desEncriptar(texto):
    textofinal = ' '
    print('\nEsta funcion desencripta el siguiente texto: ', texto)
    for letra in texto:
        if contador % 3 == 0:
            textofinal += letra
        contador += 1
    print('El dato desencriptado es: ', textofinal) 
    print('\n')

# Lector de archivos
def LeerArchivo():
    archivo = open('probando_texto.txt', 'r')
    texto = archivo.read()
    archivo.close()
    textoencriptado = encriptar(texto)
    print(textoencriptado)

# lector de archivos encriptados
def leer_archivo_encriptar():
    archivo = open('probando_texto.txt', 'r')
    texto = archivo.read()
    archivo.close()
    textoencriptado = encriptar(texto)

    archivo = open('probando_texto.txt', 'w')
    archivo.write(textoencriptado)
    archivo.close()

# Muestra el texto encriptado, desencriptado 
def lector_archivo_desencriptar():
    archivo = open('probando_texto.txt', 'r')
    texto = archivo.read()
    archivo.close()
    textoencriptado = desEncriptar(texto)
    print(textoencriptado)

    archivo = open('probando_texto.txt', 'w')
    archivo.write(textoencriptado)
    archivo.close()


# Inicio
while True:
    opcion = input('Desea encriptar el texto... (S/N)(x: salir)...: ').lower()
    data = input('Escriba el texto que desee encriptar: ').lower()
    # Muestra el resultado
    if opcion == 's':
        encriptar(data)
    elif opcion == 'x':
        print('La operacion ha terminado ')
        break
    else:
        desEncriptar(data)












