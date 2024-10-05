### Faça um programa que percorra duas listas e gere uma terceira com os elementos das duas primeiras.

x=0
lista1=[]
lista2=[]
listafinal=lista1+lista2

while x!=10:
    if x<5:
        lista1.append(int(input("Escreva a 1º lista:")))
        x+=1

    if x>=5 and x<10:
        lista2.append(int(input("Escreva a 2º lista:")))
        x+=1

listafinal.extend(lista1+lista2)
print(listafinal)
