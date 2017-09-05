# lee una cadena de DNA.
# retorna una cadena de RNA.

cadena1 = raw_input("Por favor ingrese una cadena en DNA\n")
#print(cadena)
cadena2 = raw_input("Por favor ingrese una cadena en DNA\n")



def DNA_to_RNA(cadena):
    respuesta = ""
    for i in cadena:
        if(i == "T"):
            respuesta += "U"
        else:
            respuesta = respuesta + i
    return respuesta

print(DNA_to_RNA(cadena1))
print(DNA_to_RNA(cadena2))

# print(cadena.)
