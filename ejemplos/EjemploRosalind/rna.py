# lee una cadena de DNA.
# retorna una cadena de RNA.

cadena = raw_input()

respuesta = ""

for i in cadena:
    if(i == "T"):
        respuesta += "U"
    else:
        respuesta = respuesta + i

print respuesta

# print(cadena.)
