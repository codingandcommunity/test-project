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
        for r in range(6):
            print( str(combos[r]) + "<1400")
        self.assertEquals(inRange, True)
        #Checks to see if the deck items are altered 
        deck.sort()
        self.assertEquals(deck, ["A","B","C"])

        

if __name__ == '__main__':
    unittest.main()
    
    
    
    
    
    
    
    
    
    
    