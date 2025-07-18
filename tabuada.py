#! /usr/bin/env python

#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Iterable (percorriveis)
numeros = list(range(1, 11) )



# para cada numero na lista numeros:
for n1 in numeros:
    print("{:^18}".format(f"Tabuada do {n1}"))
    print()
    bloco = ""
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
    print("#" * 18)





