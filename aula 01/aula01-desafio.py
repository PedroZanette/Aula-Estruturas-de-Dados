import random

notas = []

nota = 0 
contador = 0

decisao = input("Para digitar as notas digite 1 se quiser aleatório digite 2: ")

if decisao == "1":

    while nota != -1:
        contador += 1
        nota = float(input(f"Digite a {contador}° nota ou -1 para sair: "))
        
        if nota != -1:
            notas.append(nota)

else:
    if decisao == "2":

        while contador != 20:
            contador += 1
            nota = random.uniform(0, 10)
            
            notas.append(nota)
    
    else:
        print("Resposta inválida tente novamente depois de 1000 anos")

def media():
    nota = 0
    ajuda = 0
    resultado = 0

    for nota in notas:
        ajuda += nota
        resultado = ajuda/contador

    print(f"A média é {resultado:.2f}\n")

def maiorMenor():
    nota_maior = 0

    nota_menor = 99999999999

    for nota in notas:
        if nota > nota_maior:
            nota_maior = nota
        
        if nota < nota_menor:
            nota_menor = nota
    
    print(f"A nota maior é {nota_maior:.2f}\n")

    print(f"A nota menor é {nota_menor:.2f}\n")


def main():
    print("\n")
    media()
    maiorMenor()

main()