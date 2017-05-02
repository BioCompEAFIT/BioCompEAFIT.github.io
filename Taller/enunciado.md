# Evaluación Modulo Python Bipología Computacional

## Punto 1

## Descripción del problema:

Los 20 aminoacidos de mayor ocurrencia son abreviados usando 20 letras del alfabeto (todas menos B, J, O, U, X, Z).

Las cadenas de proteinas son construidas a partir de esos 20 simbolos. El termino cadena genetica incorporara cadenas de proteninas con cadenas de DNA y RNA.La tabla de RNA Codones dicta los detalles correspondientes a los codones especificos en el alfabeto de aminoacidos.

[Entrada](prot.txt): Una cadena de RNA correspondiente a una cadena de mRNA (de longitud máxima de 10 kbp)
[Salida](out1.out): La cadena resultante que representa la proteina codificada

### Recursos

https://docs.python.org/2/library/string.html
https://docs.python.org/2/tutorial/datastructures.html
https://docs.python.org/2/tutorial/inputoutput.html
https://docs.python.org/2/library/functions.html#range
https://docs.python.org/2/library/functions.html#round

## Punto 2

## Descripción del problema:

In a weighted alphabet, every symbol is assigned a positive real number called a weight. A string formed from a weighted alphabet is called a weighted string, and its weight is equal to the sum of the weights of its symbols.

The standard weight assigned to each member of the 20-symbol amino acid alphabet is the monoisotopic mass of the corresponding amino acid.

Given: A protein string  of length at most 1000 aa.

Return: The total weight of . Consult the monoisotopic mass table.



En un alfabeto ponderado, a cada símbolo se le asigna un número real positivo llamado peso. Una cadena formada a partir de un alfabeto ponderado se denomina cadena ponderada y su peso es igual a la suma de los pesos de sus símbolos.

El peso estándar asignado a cada miembro del alfabeto de aminoácidos de 20 símbolos es la masa monoisotópica del aminoácido correspondiente.

+ [Entrada](prtm.in): Una cadena de proteínas de longitud de 1000 aa como máximo.
+ [Salida](p2.out): El peso total de. Consulte la [tabla de masa monoisotópica](masstable.txt).
