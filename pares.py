###  devem ser copiados para a P, se forem pares;ou para a I, se forem ímpares.

P=[]
I=[]
V = [9, 8, 7, 12, 0, 13, 21]

for numero in V:
    if (numero % 2)==0:
        P.append(numero)
    else:
        I.append(numero)
print(P)
print (I)
