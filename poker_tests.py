from poker_class import Card, Deck, Player, PokerGame, PokerHandRanker
import unittest



class CardTestCase(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card('K','h')
        self.card2 = Card('A','c')
        self.card3 = Card('5','h')

    def tearDown(self):
        pass
    
    def test_get_card_value(self):
        self.assertEqual(self.card1.get_card_value(), 13)
        self.assertEqual(self.card2.get_card_value(), 14)
        self.assertEqual(self.card3.get_card_value(), 5)


class DeckTestCase(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def tearDown(self):
        del self.deck

    def test_all_cards(self):
        self.assertEqual(len(self.deck.cards), 52)
    
    def test_deal(self):
        cards = self.deck.deal(5)
        self.assertEqual(len(cards), 5)
        self.assertEqual(len(self.deck.cards), 47)

    def test_shuffle_reset(self):
        cards = self.deck.deal(12)
        self.assertEqual(len(self.deck.cards), 40)
        self.deck.shuffle()
        self.assertEqual(len(self.deck.cards), 52)



class PokerHandRankerTestCase(unittest.TestCase):
    
    def setUp(self):
        self.cards1 = PokerHandRanker([Card('K','d'), Card('9','c'), Card('9','h'),
                                       Card('4','d'), Card('3','d'), Card('9','d'), Card('J','d')])
        
        self.cards2 = PokerHandRanker([Card('5','s'),Card('4','c'),Card('5','h'),
                                       Card('4','s'),Card('3','h'),Card('10','h'),Card('J','d')])

        
        self.cards3 = PokerHandRanker([Card('2','h'), Card('4','c'), Card('5','s'),
                                       Card('J','d'), Card('6','h'), Card('A','d'), Card('Q','d')])
        
        self.cards4 = PokerHandRanker([Card('K','h'), Card('K','c'), Card('9','d'),
                                       Card('K','d'), Card('K','s'), Card('9','h'), Card('J','d')])

    
    def test_get_high_card(self):
        self.assertEqual(self.cards1.get_high_card(), 'Kd')
        self.assertEqual(self.cards2.get_high_card(), 'Jd')
        self.assertEqual(self.cards3.get_high_card(), 'Ad')

    def test_has_pair(self):
        self.assertTrue(self.cards1.has_pair())
        self.assertTrue(self.cards2.has_pair())
        self.assertFalse(self.cards3.has_pair())

    def test_has_two_pair(self):
        self.assertFalse(self.cards1.has_two_pair())
        self.assertTrue(self.cards2.has_two_pair())
        self.assertFalse(self.cards3.has_two_pair())

    def test_has_3ok(self):
        self.assertTrue(self.cards1.has_3ok())
        self.assertFalse(self.cards2.has_3ok())
        self.assertFalse(self.cards3.has_3ok())

    def test_has_full_house(self):
        self.assertFalse(self.cards1.has_full_house())
        self.assertFalse(self.cards2.has_full_house())
        self.assertFalse(self.cards3.has_full_house())
        self.assertTrue(self.cards4.has_full_house())

    def test_has_flush(self):
        self.assertTrue(self.cards1.has_flush())
        self.assertFalse(self.cards2.has_flush())
        self.assertFalse(self.cards3.has_flush())

unittest.main()
