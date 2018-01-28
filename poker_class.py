import random
import time
from collections import Counter



class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def get_card_value(self):
        try:
            return int(self.value)
        except Exception:
            if self.value == 'J': return 11
            elif self.value == 'Q': return 12
            elif self.value == 'K': return 13
            elif self.value == 'A': return 14

    def __repr__(self):
        return '{}{}'.format(self.value, self.suit)


class Deck(object):

    VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
    SUITS = ('h', 'd', 's', 'c')

    def __init__(self):
        self.cards = list()
        self.discard_pile = list()
        self._create_deck()
        self.shuffle()

    def __repr__(self):
        return '{} card deck here'.format(len(self.cards))

    def _create_deck(self):
        for value in Deck.VALUES:
            for suit in Deck.SUITS:
                self.cards.append(Card(value, suit))

    def shuffle(self, reset=True): 
        if reset == True:
            self.cards += self.discard_pile
            self.discard_pile = list()
            print('shuffling fresh deck')
        else:
            print('shuffling remaining')
        random.shuffle(self.cards)
        

    def deal(self, num_cards):
        patch = []
        for num in range(num_cards):
            pop = self.cards.pop()
            self.discard_pile.append(pop)
            patch.append(pop)
        return patch
        


class Player(object):
    
    def __init__(self, name):
        self.name = name
        self.hand = list()
        self.round_outcomes = dict()

    def __repr__(self):
        return self.name



class PokerGame(object):
    
    def __init__(self):
        self.players = list()
        self.deck = Deck()
        self.final_dict = dict()

    def add_player(self, player_name):
        self.players.append(Player(player_name))

    def remove_player(self, player_name):
        pass

    def simulate_round(self):
        community_cards = self.deck.deal(5)
        for player in self.players:
            player.hand = self.deck.deal(2)
            player.hand += community_cards
        print(PokerHandRanker().compare(self.players))




class PokerHandRanker(object):

    RANKING = ('Royal Flush', 'Straight Flush', 'Four of Kind', 'Full House',
         'Flush', 'Straight', 'Three of Kind', 'Two Pair', 'Pair', 'High Card')


    def _get_value_count(self, cards):
        return dict(Counter([i.value for i in cards]))


    def _get_suit_count(self, cards):
        return dict(Counter([i.suit for i in cards]))


    def get_high_card(self, cards):
        tester = 0
        for card in cards:
            if card.get_card_value() > tester:
                winner = card
                tester = winner.get_card_value()
        return winner

    
    def has_pair(self, cards):
        values = [i.value for i in cards]
        if len(set(values)) == len(values):
            return False
        for val, occurances in self._get_value_count(cards).items():
            if occurances == 2:
                return val
        

    def has_two_pair(self, cards):
        value_list = [s for v, s in self._get_value_count(cards).items()]
        vals = []
        if value_list.count(2) == 2:
            for x, y in self._get_value_count(cards).items():
                if y == 2:
                    vals.append(x)
            return vals
        return False

                   
    def has_3ok(self, cards): 
        for k, v in self._get_value_count(cards).items():
            if v >= 3:
                return k
        return False




    def has_straight(self, cards):
        return False




    def has_flush(self, cards):
        suit_list = [s for v, s in self._get_suit_count(cards).items()]
        if suit_list.count(5) == 1:
            for x, y in self._get_suit_count(cards).items():
                if y == 5:
                    flush_cards = [i for i in cards if i.suit == x]
                    sorted_flush_cards = sorted(flush_cards, key=lambda x: x.get_card_value(), reverse=True)
                    return [x, sorted_flush_cards[0]]
        return False


    def has_full_house(self, cards):
        value_list = [s for v, s in self._get_value_count(cards).items()]
        vals = []
        if value_list.count(2) >= 1 and value_list.count(3) == 1 or value_list.count(4) == 1:
            sorted_cards = sorted(cards, key=lambda x: x.get_card_value(), reverse=True)
            return [sorted_cards[0].value, sorted_cards[3].value]
        return False


    def has_4ok(self, cards):
        for k, v in self._get_value_count(cards).items():
            if v == 4:
                return k
        return False



    def has_straight_flush(self, cards):
        return False



    def has_royal_flush(self, cards):
        values = ['A','K','Q','J','10']
        suit_list = [s for v, s in self._get_suit_count(cards).items()]
        if suit_list.count(5) == 1:
            for x, y in self._get_suit_count(cards).items():
                if y == 5:
                    flush_cards = [i for i in cards if i.suit == x]
            for card in flush_cards:
                if card.value in values:
                    values.remove(card.value)
            if len(values) == 0:
                return [x, 'WOW!!']
        return False
            

    def comparison_dict(self, cards):
        
        return {'High Card': self.get_high_card(cards),
                    'Pair': self.has_pair(cards),
                    'Two Pair': self.has_two_pair(cards),
                    'Three of Kind': self.has_3ok(cards),
                    'Full House': self.has_full_house(cards),
                    'Flush': self.has_flush(cards),
                    'Straight': self.has_straight(cards),
                    'Four of Kind': self.has_4ok(cards),
                    'Straight Flush': self.has_straight_flush(cards),
                    'Royal Flush': self.has_royal_flush(cards)}




# Still need to add final ordering logic for delivery
    
    def compare(self, players_list):
        result = []
        for player in players_list: 
            for level in PokerHandRanker.RANKING:
                primary = self.comparison_dict(player.hand)[level]
                if primary != False:
                    result.append((player, level, primary))
                    break
        return result
                                  



if __name__ == '__main__':
    our_game = PokerGame()
    our_game.add_player('corey')
    our_game.add_player('tyler')
    our_game.add_player('chelsea')
    our_game.add_player('mom')
    print('Simulating three rounds')
    print()
    for count in range(3):
        our_game.simulate_round()
    

        
