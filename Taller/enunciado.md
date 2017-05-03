# Bipología Computacional
## Evaluación Modulo Python


### **_Fecha de Entrega_**: 2017-04-14

## Punto 1 (50%)

## Descripción del problema:

Los 20 aminoacidos de mayor ocurrencia son abreviados usando 20 letras del alfabeto (todas menos B, J, O, U, X, Z).

Las cadenas de proteinas son construidas a partir de esos 20 simbolos. El termino cadena genetica incorporara cadenas de proteninas con cadenas de DNA y RNA.La [tabla de RNA Codones](codontable.txt) dicta los detalles correspondientes a los codones especificos en el alfabeto de aminoacidos.

+ [Entrada](prot.txt): Una cadena de RNA correspondiente a una cadena de mRNA (de longitud máxima de 10 kbp)
+ [Salida](out1.out): La cadena resultante que representa la proteina codificada

### _sugerencia_:

Del archivo de la tabla de codones cree un diccionario cuya clave sea el codon y cuyo valor el aminoacido.
De la entrada leer la linea y tomar cada codones (3 caracteres), buscar el aminoacido correspondiente en el diccionario, crear una cadena  resultante a partir de los aminoacidos leidos.

## Punto 2 (50%)

## Descripción del problema:

En un alfabeto ponderado, a cada símbolo se le asigna un número real positivo llamado peso. Una cadena formada a partir de un alfabeto ponderado se denomina cadena ponderada y su peso es igual a la suma de los pesos de sus símbolos.

El peso estándar asignado a cada miembro del alfabeto de aminoácidos de 20 símbolos es la masa monoisotópica del aminoácido correspondiente.

+ [Entrada](prtm.in): Una cadena de proteínas de longitud de 1000 aa como máximo.
+ [Salida](p2.out): El peso total de. Consulte la [tabla de masa monoisotópica](masstable.txt).

### _sugerencia_:

Del archivo de la tabla de masas cree un diccionario cuya clave sea el simbolo y cuyo valor la masa.
De la entrada leer la linea y tomar cada simbolo, buscarlo en el diccionario, retornar la suma de los pesos

### Recursos

https://docs.python.org/2/library/string.html
https://docs.python.org/2/tutorial/datastructures.html
https://docs.python.org/2/tutorial/inputoutput.html
https://docs.python.org/2/library/functions.html#range
https://docs.python.org/2/library/functions.html#round
