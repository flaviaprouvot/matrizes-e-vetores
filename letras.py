### faça um programa que leia um vetor de 10 caracteres minúsculos e diga quantas consoantes foram lidas

letras=[0,0,0,0,0,0,0,0,0,0]
x=0
vogais=0
consoantes=0
while vogais+consoantes!=10:
    letras[x]=str(input("Escreva uma letra minúscula:"))
    if (letras[x]=="a") or (letras[x]=="e") or (letras[x]=="i") or (letras[x]=="o") or(letras[x]=="u"):
        vogais+=1
        print(vogais)
    else:
        consoantes+=1
        print (consoantes)
print ("Foram lidas", consoantes, "consoantes")
