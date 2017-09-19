miarchivo = open("entrada2.txt",'r')

for linea in miarchivo.readlines():
    print linea.rstrip()
