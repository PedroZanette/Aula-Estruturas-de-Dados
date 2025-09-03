from data_structures import *
from typing import List, Optional, Any
from random import randint, shuffle


class Game:

    def __init__(self, hand_size=5, player_amount=2, cards_amount=10):

        """ Game Rules
            - Quantidade de Cartas
            - Tamanho da Mão
            - Quantidade de Jogadores
        """

        self.hand_size = hand_size
        self.cards_amount = cards_amount
        self.player_amount = player_amount
        self.player_queue = Queue()
        self._create_players()
        self.finish_game = False

    def _create_players(self):
        for next_player in range(self.player_amount):
            player = Player(f'Player {next_player}', self.cards_amount, self.hand_size)
            player.deck.create_random_deck(player)
            player.draw_cards(4)
            self.player_queue.enqueue(player)

    def start(self):
        while not self.finish_game:
            self.update_round()

        player_1 = self.player_queue.dequeue()
        player_2 = self.player_queue.dequeue()
        if player_1.get_victory_points() > player_2.get_victory_points():
            print(f'Jogador: {player_1.name} foi o Vitorioso com {player_1.get_victory_points()} pontos contra {player_2.get_victory_points()} pontos')
        elif player_1.get_victory_points() < player_2.get_victory_points():
            print(f'Jogador: {player_2.name} foi o Vitorioso com {player_2.get_victory_points()} pontos contra {player_1.get_victory_points()} pontos')
        else:
            print(f'Jogo Empatado')

    def update_round(self):
        player_1 = self.player_queue.dequeue()
        player_2 = self.player_queue.peek()
        self.player_queue.enqueue(player_1)
        card_1 = player_1.get_next_card()
        card_2 = player_2.get_next_card()
        if card_1 and card_2:
            self.solve_battle(card_1, card_2)

        else:
            self.finish_game = True

    def solve_battle(self, card_1, card_2):
        attack_queue = self.create_attack_queue(card_1, card_2)
        while True:
            card_in_attack = attack_queue.dequeue()
            card_in_defense = attack_queue.peek()
            if card_in_attack.solve_attack(card_in_defense):
                print(f'{card_in_attack.owner.name} Destrui a carta de {card_in_defense.owner.name}')
                card_in_attack.owner.plus_victory()
                break
            attack_queue.enqueue(card_in_attack)

    @staticmethod
    def create_attack_queue(card_1, card_2):
        attack_queue = Queue()
        if card_1.speed > card_2.speed:
            attack_queue.enqueue(card_1)
            attack_queue.enqueue(card_2)
        elif card_1.speed < card_2.speed:
            attack_queue.enqueue(card_2)
            attack_queue.enqueue(card_1)
        else:
            cards = [card_1, card_2]
            shuffle(cards)
            for card in cards:
                attack_queue.enqueue(card)
        return attack_queue


class Player:
    def __init__(self, name, cards_amount, hand_size):
        self.name = name
        self.deck = Deck(cards_amount)
        self.hand = CircularQueue(hand_size)
        self._victory_points = 0

    def draw_cards(self, card_amount):
        for next_card in range(card_amount):
            if not self.hand.is_full():
                card = self.deck.stack_deck.pop()
                if card:
                    self.insert_hand_card(card)
                else:
                    print('Acabou as Cartas da Pilha')
            else:
                print('Mão Cheia')

    def insert_hand_card(self, card):
        if type(self.hand) == PriorityQueue:
            self.hand.enqueue(card, card.speed)
        elif type(self.hand) == CircularQueue:
            self.hand.enqueue(card)

    def get_next_card(self):
        if self.hand.is_empty():
            return None
        next_card = self.hand.dequeue()
        self.draw_cards(1)
        return next_card

    def plus_victory(self):
        self._victory_points += 1

    def get_victory_points(self):
        return self._victory_points


class Deck:
    def __init__(self, cards_amount):
        self.cards_amount = cards_amount
        self.stack_deck = Stack()

    def create_random_deck(self, owner):
        for next_card in range(self.cards_amount):
            self.stack_deck.push(Card(True, owner))


class Card:
    def __init__(self,
                 random_attributes,
                 owner,
                 attack=None,
                 defense=None,
                 speed=None):
        self.owner = owner
        self.attack = attack
        self.defense = defense
        self.speed = speed
        if random_attributes:
            self._create_random_attributes()

    def _create_random_attributes(self):
        self.attack = randint(1, 6)
        self.defense = randint(3, 12)
        self.speed = randint(1, 10)

    def solve_attack(self, defense_card):
        dice_result = self.roll_dices()
        print('-----Rolagem dos Dados-----')
        print(f'{self.owner.name} Atacando ---> {defense_card.owner.name}')
        print(f'Resultado da Rolagem de Dados -> {dice_result}')
        print(f'---Ataque:{self.attack} --> Poder de Ataque -> '
              f'{self.attack + dice_result} <-- Defesa: {defense_card.defense}')
        return self.attack + dice_result > defense_card.defense

    @staticmethod
    def roll_dices():
        return randint(1, 6) + randint(1, 6)



