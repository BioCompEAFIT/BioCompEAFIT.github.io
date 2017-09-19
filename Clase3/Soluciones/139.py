def leerTarjeta(nombre):
    mi_tarjeta = {"B":[],"I":[],"N":[],"G":[],"O":[]}
    archivo = open(nombre,'r')
    lineas = archivo.readlines()
    for i in range(1,6):
        nums = [int(x) for x in lineas[i].split()]
        mi_tarjeta["B"].append(nums[0])
        mi_tarjeta["I"].append(nums[1])
        mi_tarjeta["N"].append(nums[2])
        mi_tarjeta["G"].append(nums[3])
        mi_tarjeta["O"].append(nums[4])
    print mi_tarjeta
    return mi_tarjeta

def checkBingo(tarjeta,llamados):
    for k,v in tarjeta.items():
        if k not in llamados or v != llamados[k]:
            c = {k:v}
        # else:
        #     c = {k:0}
    return c

t1 = leerTarjeta("Bingo/T1.txt")
c1 = leerTarjeta("Bingo/c1.txt")

print checkBingo(t1,c1)
