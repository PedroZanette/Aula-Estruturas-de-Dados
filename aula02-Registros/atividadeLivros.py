from dataclasses import dataclass


@dataclass 
class Livro:
    titulo: str
    autor: str
    ano: int
    preco: float

def addLivro():

    escolha = input("Digite 1 para digitar os 5 livros ou digite 2 para usar pré definido: ")

    livros = []

    if escolha == "1":
        for i in range(5):
            titulo = input(f"Digite o titulo do {i+1}° livro: ")
            autor = input(f"Digite o autor do {i+1}° livro: ")
            ano = input(f"Digite o ano do {i+1}° livro: ")
            preco = input(f"Digite o preço do {i+1}° livro: ")
            print("\n")

            livro = Livro(titulo, autor, ano, preco)
            livros.append(livro)
    else:
        if escolha == "2":
            livros.append(Livro("1984", "George Orwell", 1949, 39.90))
            livros.append(Livro("Klara e o Sol", "Kazuo Ishiguro", 2021, 57.80))
            livros.append(Livro("O Verão em que Tudo Mudou", "Thalita Rebouças", 2023, 42.90))
            livros.append(Livro("A Revolução dos Bichos", "George Orwell", 1945, 34.20))
            livros.append(Livro("Capitães da Areia", "Jorge Amado", 1937, 27.30))
        else :
            print("digite um número valido")
            return False

    return livros



def recente(livros):
    recentes = []
    for livro in livros:
        if livro.ano > 2020:
            recentes.append(livro)
    return recentes

def caro(livros):
    caro = []
    mais_caro = 0
    livro_caro = ""
    media = 0
    preco = 0

    for livro in livros:
        preco = livro.preco
        media += preco
        if mais_caro <= livro.preco:
            mais_caro = livro.preco
            livro_caro = livro.titulo

    media = media/5
    
    print(f"A média de valores dos livros é {media:.2f}, o mais caro é {livro_caro} custando R${mais_caro}")

    for livro in livros:
        if livro.preco > media:
            caro.append(livro)
            
    print("\nOs livros mais caros que a média é/são:")
    for livro in caro:
        print(livro)




def main():
    
    livros = addLivro()

    print("\nDemonstração dos dados/livros")
    for livro in livros:
        print(livro)

    print("\n")

    recent = recente(livros)

    print(f"Os livros recentes de menos que 5 anos:")
    for livro in recent:
        print(livro)

    print("\n")

    caro(livros)


main()
