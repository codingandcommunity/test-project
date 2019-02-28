import unittest
from deck import shuffle
class MyTest(unittest.TestCase):
	def setUp(self):
		pass
	#Checks to see if two cards are shuffled by making sure they are not the exact same at least once out of 30 tries
	def test_TwoCards(self):
		deck = ["A", "B"]
		notDifferent = True
		i = 0
		while(notDifferent and i<30):
			if(shuffle(deck) != ["A", "B"]):
				notDifferent = False
			i += 1
		self.assertEquals(notDifferent,False)
		#Checks to see if the deck items are altered 
		deck.sort()
		self.assertEquals(deck, ["A","B"])
	#Checks to see if three cards are shuffled by making sure they are not the exact same at least once out of 40 tries
	def test_ThreeCards(self):
		deck = ["A", "B", "C"]
		notDifferent = True
		i = 0
		while(notDifferent and i<40):
			if(shuffle(deck) != ["A", "B", "C"]):
				notDifferent = False
			i += 1
		self.assertEquals(notDifferent,False)
		#Checks to see if the deck items are altered 
		deck.sort()
		self.assertEquals(deck, ["A","B","C"])

		

if __name__ == '__main__':
	unittest.main()