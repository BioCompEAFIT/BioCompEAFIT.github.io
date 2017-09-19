import sys

# tail function implementation

def readfile():
    resultado = "Lectura Exitosa!"
    nombrearchivo = ""

    try:
        nombrearchivo = sys.argv[1]
    except IndexError:
        resultado = "No ingreso el nombre de entrada "

    try:
        archivo = open(nombrearchivo,'r')
        for line in archivo.readlines()[-10:-1]:
            print line.rstrip()
    except IOError:
        resultado = "nombre de archivo incorrecto"
    return resultado

print(readfile())
