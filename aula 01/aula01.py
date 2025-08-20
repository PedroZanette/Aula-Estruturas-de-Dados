import random

notas = [7.5, 8.0, 6.5]
notas_ordenadas = []
notas_ordenadas2 = []

# notas.append(9.0)

print(f"A lista contem {len(notas)} elementos")

# iteração
for valor in notas:
    print(valor)

#for indice in range(4):  # ou in range(len(notas))
#    print(notas[indice])

nota = 0

while nota != -1:
    nota = float(input("Digite -1 para sair: "))

    if nota != -1:
        notas.append(nota)

print(f"\nTodas as notas : {notas}")

for nota in notas: 
    if nota >= 7.0:
        
        notas_ordenadas.append(nota)
        
        notas_ordenadas = sorted(notas_ordenadas)
        
print("\nNotas acima ou na média")
for nota in notas_ordenadas:
    print(nota)