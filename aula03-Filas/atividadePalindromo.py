def verifica_palindromo():
    palavra = str(input("Digite uma palavra para verificar se é palindroma: "))
    
    lista = list(palavra)

    lista_invertida = lista[::-1]

    resultado = "".join(lista_invertida)

    if resultado == palavra:
        print(f"A palavra {palavra} é palindroma")
    else:
        print(f"A palavra {palavra} não é palindroma")

verifica_palindromo()

