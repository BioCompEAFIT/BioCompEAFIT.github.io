# lee una cadena de DNA.
# retorna una cadena de RNA.

cadena = raw_input("Por favor ingrese una cadena en DNA")

respuesta = ""

for i in cadena:
    if(i == "T"):
        respuesta += "U"
    else:
        respuesta = respuesta + i

print respuesta

# print(cadena.)
