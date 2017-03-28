archivo = open("entrada.txt")

for line in archivo:
    a = int(line.strip())
    print a+1
