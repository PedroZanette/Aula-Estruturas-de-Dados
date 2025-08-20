from dataclasses import dataclass

test = []

@dataclass 
class Aluno:
    nome: str
    idade: int
    media: float

aluno = Aluno("Felipe", 45, 9.2)

print(aluno)

#
aluno.nota = 8.7

teste = type(aluno.nome)

teste = str(teste)

test = teste.split(' ')

teste = test[1]

teste = teste.replace(">", '' )
teste = teste.replace("'", '' )

if teste == 'str':
    print("Deu certo só correr pro abraço")

class Aluno1:
    def __init__(self,nome,idade,media):
        self.nome = nome
        self.idade = idade
        self.media = media
    def aprovado(self):
        return self.media >= 7.0