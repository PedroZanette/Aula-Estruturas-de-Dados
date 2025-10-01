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
    """Preenche a pilha de um jogador com 10 cartas aleatórias e imprime."""
    escolha = input("Digite 1 para o player 1 ou 2 para o player 2 ou 0 para sair: ")

    if escolha == "1":
        print("--------- Cartas do Player 1 ---------")
    elif escolha == "2":
        print("--------- Cartas do Player 2 ---------")
    elif escolha == "0":
        print("Saindo")
        return
    else:
        print("Tente novamente!")
        return

    pilha.clear()
    for i in range(10):
        carta = Carta(
            atk=random.randint(1, 6),
            df =random.randint(3, 12),
            vel=random.randint(1, 10),
        )
        pilha.append(carta)
        print(f"atk = {carta.atk}\tdf = {carta.df}\tvel = {carta.vel}")

def repor_carta(mao, pilha):
    """Repõe 1 carta do topo da pilha para o fim da mão (fila rotativa)."""
    if not pilha:
        return False
    mao.append(pilha.pop(0))
    return True

def limpar_topo(mao, pilha, label):
    """
    Remove TODAS as cartas com df <= 0 do topo da mão e tenta repor da pilha.
    Retorna True se removeu algo (para permitir reavaliar condições de fim).
    """
    removeu = False
    while mao and mao[0].df <= 0:
        print(f"Carta do {label} com DF=0 removida do topo. Saindo da fila.")
        mao.pop(0)
        removeu = True
        if not repor_carta(mao, pilha):
            print(f"{label} não tem mais cartas na pilha para repor.")
    return removeu

def rodada(mao_p1, mao_p2, num_rodada):
    """
    Executa UMA rodada e retorna:
      'p1_caiu' | 'p2_caiu' | 'continua'
    (A remoção do card caído é feita aqui; a reposição fica para o driver.)
    """
    if not mao_p1 or not mao_p2:
        # Quem decide fim de jogo é o driver recursivo; aqui só sinalizamos que
        # não há como rodar batalha — mas para manter o driver simples, retornamos
        # 'continua' e ele checa as mãos na entrada da próxima chamada.
        return "continua"

    c1 = mao_p1[0]
    c2 = mao_p2[0]

    vel_p1 = c1.vel + d6()
    vel_p2 = c2.vel + d6()

    print(f"\n[Rodada {num_rodada}]")
    print(f"P1: vel base {c1.vel} + d6 = {vel_p1} | P2: vel base {c2.vel} + d6 = {vel_p2}")

    while vel_p1 == vel_p2:
        print("Velocidades iguais — re-rolando...")
        vel_p1 = c1.vel + d6()
        vel_p2 = c2.vel + d6()
        print(f"Re-rolagem: P1={vel_p1} | P2={vel_p2}")

    if vel_p1 > vel_p2:
        ordem = [("P1", c1, c2), ("P2", c2, c1)]
    else:
        ordem = [("P2", c2, c1), ("P1", c1, c2)]

    # estado padrão
    estado = "continua"

    for tag_atacante, atacante, defensor in ordem:
        # se por algum motivo o defensor está 0, não age mais
        if defensor.df <= 0:
            continue

        dano = atacante.atk + d6()
        defensor.df = max(0, defensor.df - dano)
        print(f"{tag_atacante} ataca com {dano}. Defesa do oponente = {defensor.df}")

        if defensor.df <= 0:
            if tag_atacante == "P1":
                print("Carta do Player 2 caiu! Saindo da fila.")
                mao_p2.pop(0)
                estado = "p2_caiu"
            else:
                print("Carta do Player 1 caiu! Saindo da fila.")
                mao_p1.pop(0)
                estado = "p1_caiu"
            break  # cai alguém → encerra a rodada

    return estado

def jogo_recursivo(mao_p1, mao_p2, pilha1, pilha2, rodada_num):
    """Driver recursivo que substitui o while."""
    # limpar cartas mortas do topo (evita travar se df==0)
    mudou = False
    mudou |= limpar_topo(mao_p1, pilha1, "Player 1")
    mudou |= limpar_topo(mao_p2, pilha2, "Player 2")

    # condições de parada (fim de jogo) — SEMPRE depois de limpar topo
    if not mao_p1 and not mao_p2:
        print("\nEmpate geral (as duas mãos ficaram vazias)!")
        return "empate"
    if not mao_p1:
        print("\nO ganhador foi o Player 2")
        return "p2"
    if not mao_p2:
        print("\nO ganhador foi o Player 1")
        return "p1"

    # executa UMA rodada
    estado = rodada(mao_p1, mao_p2, rodada_num)

    # reposição conforme resultado
    if estado == "p1_caiu":
        print("Uma carta do Player 1 caiu nesta rodada!")
        if not repor_carta(mao_p1, pilha1):
            print("P1 não tem mais cartas na pilha para repor.")
    elif estado == "p2_caiu":
        print("Uma carta do Player 2 caiu nesta rodada!")
        if not repor_carta(mao_p2, pilha2):
            print("P2 não tem mais cartas na pilha para repor.")
    else:
        print("As duas cartas sobreviveram e continuam na fila.")

    # passo recursivo
    return jogo_recursivo(mao_p1, mao_p2, pilha1, pilha2, rodada_num + 1)

def jogo():
    pilha_de_cartas_1 = []
    pilha_de_cartas_2 = []

    sorteio(pilha_de_cartas_1)
    sorteio(pilha_de_cartas_2)

    if len(pilha_de_cartas_1) == 10:
        mao_p1 = pilha_de_cartas_1[:4]
    else:
        mao_p1 = []

    if len(pilha_de_cartas_2) == 10:
        mao_p2 = pilha_de_cartas_2[:4]
    else:
        mao_p2 = []

    print("\nínicio do Jogo")

    if len(mao_p1) == 4 and len(mao_p2) == 4:
        jogo_recursivo(mao_p1, mao_p2, pilha_de_cartas_1, pilha_de_cartas_2, rodada_num=1)
    else:
        print("Alguma mão com cartas faltando. Tente novamente!")

# --- executa ---
jogo()
