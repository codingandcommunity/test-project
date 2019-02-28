import unittest
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
if __name__ == '__main__':
	unittest.main()