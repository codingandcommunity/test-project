import unittest
import sys
sys.path.insert(0,"..")
from deck import deal

class MyTest(unittest.TestCase):
    def setUp(self):
        pass
    #Deals one card to an empty deck 
    def test_to_empty(self):
        deck1 = ["A"]
        deck2 = list()
        deal(deck1,deck2)
        self.assertEquals(deck1,[])
        self.assertEquals(deck2,["A"])
    #Deals one card to an deck with one card 
    def test_one_to_one(self):
        deck1 = ["B"]
        deck2 = ["A"]
        deal(deck1,deck2)
        self.assertEquals(deck1,[])
        self.assertEquals(deck2,["A","B"])
    #Deals two cards to a deck with one card 
    def test_two_to_one(self):
        deck1 = ["B","C"]
        deck2 = ["A"]
        deal(deck1,deck2)
        deal(deck1,deck2)
        self.assertEquals(deck1,[])
        self.assertEquals(deck2,["A","B","C"])
    #Deals two cards to an empty deck 
    def test_two_to_empty(self):
        deck1 = ["A","B"]
        deck2 = list()
        deal(deck1,deck2)
        deal(deck1,deck2)
        self.assertEquals(deck1,[])
        self.assertEquals(deck2,["A","B"])
    #Deals from two decks into a third
    def test_three_decks(self):
        deck1 = ["A","C"]
        deck2 = ["B"]
        deck3 = list()
        deal(deck1,deck3)
        deal(deck2,deck3)
        deal(deck1,deck3)
        self.assertEquals(deck1,[])
        self.assertEquals(deck2,[])
        self.assertEquals(deck3,["A","B","C"])
    #Deals an entire deck to another 
    def test_full_deck(self):
        freshDeck = ["AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS",
        "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH",
        "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC",
        "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
        deck = ["AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS",
        "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH",
        "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC",
        "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
        deck2 = list()
        for i in range(len(deck)):
            deal(deck,deck2)
        self.assertEquals(freshDeck,deck2)
        self.assertEquals(deck,[])
    
if __name__ == '__main__':
	unittest.main()