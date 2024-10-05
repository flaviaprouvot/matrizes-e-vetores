###  Faça um programa que peça as 4 notas de 10 alunos, calcule e armazene em um vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

medias=[0,0,0,0,0,0,0,0,0,0]
notas=[0,0,0,0]
add=0
a,b=0,0

while a<10:
    for b in range(4):
        notas[b]=float(input("Digite suas notas:"))
        add+=notas[b]
        b+=1
    medias[a]=add/4
    add=0
    print(medias[a])
    a+=1

print ("Notas que passaram:")
for item in medias:
    if item>=7:
        print (item)
