import random

import csv

class Carta:
    def __init__(self, atk, df, vel):
        self.atk = atk
        self.df = df
        self.vel = vel
        
    def __repr__(self):
        return f"Carta(atk={self.atk}, df={self.df}, vel={self.vel})"
    
def d6():
    return random.randint(1, 6)

def deck(pilha):
    escolha = input("Digite 1 para o player 1 ou 2 para o player 2 ou 0 para sair: ")

    deck_p1 = ['4, 10, 7',
 '1, 6, 3',
 '6, 5, 8',
 '2, 12, 9',
 '3, 8, 2',
 '5, 7, 4',
 '6, 11, 6',
 '1, 3, 10',
 '2, 4, 5',
 '3, 9, 1']
    
    with open("jogador_1.csv", "w", newline="", encoding="utf-8") as file:
        campos = ["Ataque", "Defesa", "Velocidade"]
        writer = csv.writer(file)
        writer.writerow(campos)
        for s in deck_p1:
            a, d, v = (x.strip() for x in s.split(","))  # tira espaços
            writer.writerow([a, d, v])  # lista de colunas
    
        
    deck_p2 = ['4, 12, 7',
 '6, 8, 10',
 '5, 6, 2',
 '1, 7, 9',
 '2, 11, 8',
 '4, 5, 4',
 '3, 12, 6',
 '5, 10, 1',
 '6, 9, 3',
 '2, 8, 5']

    with open("jogador_2.csv", "w", newline="", encoding="utf-8") as file:
        campos = ["Ataque", "Defesa", "Velocidade"]
        writer = csv.writer(file)
        writer.writerow(campos)
        for s in deck_p1:
            a, d, v = (x.strip() for x in s.split(","))  # tira espaços
            writer.writerow([a, d, v])  # lista de colunas


    if escolha == "1":
        print("--------- Cartas do Player 1 ---------")
        for i, num in enumerate(deck_p1):
            valores = num.split(",")
            ataque = int(valores[0])
            defesa = int(valores[1])
            velocidade = int(valores[2])
            carta = Carta(atk = ataque, df = defesa, vel = velocidade)
            pilha.append(carta)
            print(f"atk = {pilha[i].atk}\tdf = {pilha[i].df}\tvel = {pilha[i].vel}")
    else: 
        if escolha == "2":
            print("--------- Cartas do Player 2 ---------")
            for i, num in enumerate(deck_p2):
                valores = num.split(",")
                ataque = int(valores[0])
                defesa = int(valores[1])
                velocidade = int(valores[2])
                carta = Carta(atk = ataque, df = defesa, vel = velocidade)
                pilha.append(carta)
                print(f"atk = {pilha[i].atk}\tdf = {pilha[i].df}\tvel = {pilha[i].vel}")
        else:
            if escolha == "0":
                print("Saido")
            else:
                print("Tente novamente!")


def rodada(mao_p1, mao_p2, num_rodada):

    if not mao_p1 or not mao_p2:
        return "fim"
    
    carta_p1 = mao_p1[0]
    carta_p2 = mao_p2[0]

            
    vel_p1 = carta_p1.vel + d6()
    vel_p2 = carta_p2.vel + d6()

    print(f"\n[Rodada {num_rodada}]")
    print(f"P1: vel base {carta_p1.vel} + d6 = {vel_p1} | P2: vel base {carta_p2.vel} + d6 = {vel_p2}")

    while vel_p1 == vel_p2:
        print("Velocidades iguais — re-rolando...")
        vel_p1 = carta_p1.vel + d6()
        vel_p2 = carta_p2.vel + d6()
        print(f"Re-rolagem: P1={vel_p1} | P2={vel_p2}")

    if vel_p1 > vel_p2:
        ordem = [("P1", carta_p1, carta_p2), ("P2", carta_p2, carta_p1)]
    else:
        ordem = [("P2", carta_p2, carta_p1), ("P1", carta_p1, carta_p2)]

    for principal_atacante, atacante, defensor in ordem:
        
        if defensor.df < 0:
            continue

        dano = atacante.atk + d6()
        defensor.df = max(0, defensor.df - dano)
        print(f"{principal_atacante} ataca com {dano}. Defesa do oponente = {defensor.df}")

        if defensor.df <= 0:
            if principal_atacante == "P1":   
                print("Carta do Player 2 caiu! Saindo da fila.")
                mao_p2.pop(0)
                return "p2_caiu"
            else:
                print("Carta do Player 1 caiu! Saindo da fila.")
                mao_p1.pop(0)
                return "p1_caiu"

    return "continua"

def repor_carta(mao, pilha):

    if not pilha:
        return False
    else:
        mao.append(pilha.pop(0))
        return True



def jogo():

    pilha_de_cartas_1 = []
    pilha_de_cartas_2 = []

    deck(pilha_de_cartas_1)

    deck(pilha_de_cartas_2)

    mao_p1 = []
    mao_p2 = []

    if 10 == len(pilha_de_cartas_1):
        mao_p1 = pilha_de_cartas_1[:4]


    if 10 == len(pilha_de_cartas_2):
        mao_p2 = pilha_de_cartas_2[:4]

    print("\nínicio do Jogo")

    if 4 == len(mao_p1) and 4 == len(mao_p2):
        rodada_num = 1
        while mao_p1 and mao_p2:
            estado = rodada(mao_p1, mao_p2, rodada_num)
            rodada_num += 1

            if estado == "p1_caiu":
                print("Uma carta do Player 1 caiu nesta rodada!")
                if not repor_carta(mao_p1, pilha_de_cartas_1):
                    print("P1 não tem mais cartas na pilha para repor.")

            elif estado == "p2_caiu":
                print("Uma carta do Player 2 caiu nesta rodada!")
                if not repor_carta(mao_p2, pilha_de_cartas_2):
                    print("P2 não tem mais cartas na pilha para repor.")
            elif estado == "continua":
                print("As duas cartas sobreviveram e continuam na fila.")
            
        if not mao_p1 and not mao_p2:
            print("\nEmpate geral (as duas mãos ficaram vazias)!")

        else:
            if not mao_p1:
                print("\nO ganhador foi o Player 2")
            else:
                print("\nO ganhador foi o Player 1")
            
    else:
        print("Alguma mão com cartas faltando. Tente novamente!")

jogo()