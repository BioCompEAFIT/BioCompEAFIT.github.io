
ruta = "/home/horus/Dropbox/9_Programming/BioComp/BioCompEAFIT.github.io/Clase3/IO/entrada1.txt"

miarchivo = open(ruta,'r')

resultado = open("salida.txt",'w')

def cuentaNT(cadena):
    return ("%d %d %d %d" % (cadena.count("A"),cadena.count("C"),cadena.count("G"),cadena.count("T")
))


for linea in miarchivo.readlines():
    if len(linea) > 1:
        resultado.write(cuentaNT(linea.rstrip().rstrip())+"\n")
