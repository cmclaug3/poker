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

    VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    SUITS = ['h', 'd', 's', 'c']

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

    def play_one_round(self):
        print(self.deck)
        round_community_cards = self.deck.deal(5)
        for player in self.players:
            player.hand = self.deck.deal(2)
            player.hand += round_community_cards
            self.final_dict[player] = player.hand
            
        print(self.deck)
        print(self.final_dict)
        
    def round_rankings(self, final_dict):
        pass



class PokerHandRanker(object):

    RANKING = ('Royal Flush', 'Straight Flush', 'Four of Kind', 'Full House',
         'Flush', 'Straight', 'Three of Kind', 'Two Pair', 'Pair', 'High Card')
    
    def __init__(self, cards):
        self.cards = cards
        self.value_count = dict(Counter([i.value for i in self.cards]))
        self.suit_count = dict(Counter([i.suit for i in self.cards]))

    def get_high_card(self):
        tester = 0
        for card in self.cards:
            if card.get_card_value() > tester:
                winner = card
                tester = winner.get_card_value()
        return str(winner)




# Figure out how to attach "TIEBREAKER/(card)" needs...

    
    def has_pair(self):
        values = [i.value for i in self.cards]
        if len(set(values)) == len(values):
            return False
        return True
        

    def has_two_pair(self):
        value_list = [s for v, s in self.value_count.items()]
        if value_list.count(2) == 2:
            return True
        return False
                    
    def has_3ok(self): #####
        for k, v in self.value_count.items():
            if v >= 3:
                return 'True {}\'s'.format(k)
        return False



    def has_straight(self):
        return False



    def has_flush(self):
        suit_list = [s for v, s in self.suit_count.items()]
        if suit_list.count(5) == 1:
            return True
        return False

    def has_full_house(self):
        value_list = [s for v, s in self.value_count.items()]
        if value_list.count(2) >= 1 and value_list.count(3) == 1 or value_list.count(4) == 1:
            return True
        return False

    


    def has_4ok(self):
        return False

    def has_straight_flush(self):
        return False

    def has_royal_flush(self):
        return False




    def comparison_dict(self):
        return {'High Card': self.get_high_card(),
                    'Pair': self.has_pair(),
                    'Two Pair': self.has_two_pair(),
                    'Three of Kind': self.has_3ok(),
                    'Full House': self.has_full_house(),
                    'Flush': self.has_flush(),
                    'Straight': self.has_straight(),
                    'Four of Kind': self.has_4ok(),
                    'Straight Flush': self.has_straight_flush(),
                    'Royal Flush': self.has_royal_flush()}




    # Returns a list with highest play /
    # any card(s) value neccessary /
    # tiebreakers
    
    def get_result(self):
        for level in PokerHandRanker.RANKING:
            if self.comparison_dict()[level] == True:
                return level
        return self.get_high_card()



if __name__ == '__main__':
    our_game = PokerGame()
    our_game.add_player('corey')
    our_game.add_player('tyler')
    our_game.add_player('chelsea')
    our_game.add_player('mommy')
    print('START OF THE GAME')
    our_game.play_one_round()
    print()
    for player, cards in our_game.final_dict.items():
        print('{}\'s high card is {}, HAVE PAIR? {}, HAVE TWO PAIR? {}, HAVE 3OK? {}, VALUE COUNTER -->{}, SUIT COUNTER --> {}'.format(player.name,
                                                            PokerHandRanker(cards).get_high_card(),
                                                            PokerHandRanker(cards).has_pair(),
                                                            PokerHandRanker(cards).has_two_pair(),
                                                            PokerHandRanker(cards).has_3ok(),
                                                            PokerHandRanker(cards).value_count,
                                                            PokerHandRanker(cards).suit_count))

        
