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
        a = 0 
        b = 0
        i = 0
        while(i<1000):
            if(d.shuffle(deck) != ["A", "B"]):
                a = a + 1
                notDifferent = False
            else:
                b = b + 1 
            i += 1
        self.assertEquals(notDifferent,False)
        print("a: " +str(a)+ "    b: " + str(b))
        #Checks to see if the deck items are altered 
        deck.sort()
        self.assertEquals(deck, ["A","B"])
    #Checks to see if three cards are shuffled by making sure they are not the exact same at least once out of 40 tries
    #Prove that all combinations are equal
    def test_ThreeCards(self):
        deck = ["A", "B", "C"]
        notDifferent = True
        i = 0
        a = 0
        b = 0
        c = 0
        while(i<1000):
            if(d.shuffle(deck) != ["A", "B", "C"]):
                notDifferent = False
                a = a + 1
            if(d.shuffle(deck) == ["B", "A", "C"]):
            	b = b +1
            if(d.shuffle(deck) == ["C", "A", "B"]):
                c = c+1
            i += 1
        print("a: " +str(a)+ "    b: " + str(b)+ "    c:"+str(c))
        self.assertEquals(notDifferent,False)
        #Checks to see if the deck items are altered 
        deck.sort()
        self.assertEquals(deck, ["A","B","C"])

        

if __name__ == '__main__':
    unittest.main()