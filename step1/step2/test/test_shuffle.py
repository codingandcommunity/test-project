import unittest
import sys
import random
sys.path.insert(0,"..")
import deck as d
class MyTest(unittest.TestCase):
    def setUp(self):
        pass
    #Checks to see if two cards are shuffled by making sure they are not the exact same at least once out of 30 tries
    def test_TwoCards(self):
        deck = ["A", "B"]
        notDifferent = True
        i = 0
        while(notDifferent and i<1000):
            if(d.shuffle(deck) != ["A", "B"]):
                notDifferent = False
            i += 1
        self.assertEquals(notDifferent,False)
        #Checks to see if the deck items are altered 
        deck.sort()
        self.assertEquals(deck, ["A","B"])
    #Prove that all combinations are equal
    def test_ThreeCards(self):
        deck = ["A", "B", "C"]
        inRange = True
        i = 0
        combos = list()
        for k in range(6):
            combos.append(0)
        while(i<1000):
            deck  = d.shuffle(deck)
            if(deck == ["A", "B", "C"]):
                combos[0] = combos[0] + 1
            elif(deck == ["A", "C", "B"]):
                combos[1] = combos[1] + 1
            elif(deck == ["B", "A", "C"]):
                combos[2] = combos[2] + 1
            elif(deck == ["B", "C", "A"]):
                combos[3] = combos[3] + 1
            elif(deck == ["C", "B", "A"]):
                combos[4] = combos[4] + 1
            elif(deck == ["C", "A", "B"]):
                combos[5] = combos[5] + 1
            i += 1
        for j in range(6):
        	if(combos[j]<50 or combos[j]>282):
        	    inRange = False
        self.assertEquals(inRange, True)
        #Checks to see if the deck items are altered 
        deck.sort()
        self.assertEquals(deck, ["A","B","C"])
    def test_Full_deck(self):
        deck = ["AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS",
        "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH",
        "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC",
        "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
        freshDeck = ["AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS",
        "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH",
        "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC",
        "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
        notDifferent = True
        i = 0 
        while(notDifferent and i<10):
            if(d.shuffle(deck) != freshDeck):
                notDifferent = False
            i += 1
        self.assertEquals(notDifferent,False)
        

if __name__ == '__main__':
    unittest.main()
    
    
    
    
    
    
    
    
    
    
    