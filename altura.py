###  Faça um programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa à ordem lida.


y=0
idades=[]
alturas=[]
while y!=5:
    idades.append(int(input("Escreva sua idade:")))
    alturas.append(float(input("Escreva sua altura:")))
    y=y+1
idades.reverse()
alturas.reverse()
print (idades)
print(alturas)
