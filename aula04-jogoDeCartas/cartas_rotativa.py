import random

class Carta:
    def __init__(self, atk, df, vel):
        self.atk = atk
        self.df = df
        self.vel = vel
        
    def __repr__(self):
        return f"Carta(atk={self.atk}, df={self.df}, vel={self.vel})"
    
def d6():
    return random.randint(1, 6)

def sorteio(pilha):
    escolha = input("Digite 1 para o player 1 ou 2 para o player 2 ou 0 para sair: ")

    if escolha == "1":
        print("--------- Cartas do Player 1 ---------")
        for i in range(10):
            carta = Carta(atk = random.randint(1, 6), df = random.randint(3, 12), vel = random.randint(1, 10))
            pilha.append(carta)
            print(f"atk = {pilha[i].atk}\tdf = {pilha[i].df}\tvel = {pilha[i].vel}")
    else: 
        if escolha == "2":
            print("--------- Cartas do Player 2 ---------")
            for i in range(10):
                carta = Carta(atk = random.randint(1, 6), df = random.randint(3, 12), vel = random.randint(1, 10))
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

    sorteio(pilha_de_cartas_1)

    sorteio(pilha_de_cartas_2)

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