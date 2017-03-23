cadena = raw_input()

aes = 0
ces = 0
ges = 0
tes = 0

longitud = len(cadena)

cont = 0

#while(cont < longitud):
#    print cadena[cont]
#    cont = cont + 1

for i in cadena:
    if(i == "A"):
        aes += 1
    elif(i == "C"):
        ces += 1
    elif(i == "G"):
        ges += 1
    elif(i == "T"):
        tes += 1
    print i


print(str(aes) + " " + str(ces)+ " "+ str(ges)+ " "+ str(tes))
