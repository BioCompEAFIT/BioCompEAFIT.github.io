def bin2dec(strbin):
    tam = len(strbin)
    res = 0
    cont = 0
    while(cont < len(strbin)):
        res += (2**(tam - cont-1) * int(strbin[cont]))
        cont +=1
    return(res)

bin_num = raw_input("ingrese el numero binario a convertir: ")
while(bin_num!="0"):
    print(("el resultado es: {0} ").format((bin2dec(bin_num))))
    bin_num = raw_input("ingrese el numero binario a convertir: ")
