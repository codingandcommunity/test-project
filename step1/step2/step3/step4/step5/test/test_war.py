import unittest
import sys
sys.path.insert(0,"..")
import deck as d
class MyTest(unittest.TestCase):
    def setUp(self):
        pass
    #Checks to see if all cards are equal to the counter part of another suit
    def test_is_equal(self):
        L1 = ["AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS"]
        L2 = ["AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH"]
        L3 = ["AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC"]
        L4 = ["AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
        for i in range(len(L1)):
            self.assertEquals(d.compare_card(L1[i],L2[i]),3)
            self.assertEquals(d.compare_card(L1[i],L3[i]),3)
            self.assertEquals(d.compare_card(L1[i],L4[i]),3)
if __name__ == '__main__':
	unittest.main()