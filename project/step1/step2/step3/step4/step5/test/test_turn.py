import unittest
import sys
sys.path.insert(0,"..")
import deck as d
def hi(L1, L2):
    L1.append(L2.pop())
class MyTest(unittest.TestCase):
    def setUp(self):
        pass
    #Checks to see if all cards are equal to the counter part of another suit
    def test_one_is_greater_test(self):
        L1 = ["8S"]
        L2 = ["AH"]
        d.turn(L1,L2)
        self.assertEquals(L1,["8S", "AH"])
        self.assertEquals(L2,[])
    def test_two_is_greater_test(self):
        L1 = ["AH"]
        L2 = ["8S"]
        d.turn(L1,L2)
        self.assertEquals(L1,[])
        self.assertEquals(L2,["AH", "8S"])
    def test_
if __name__ == '__main__':
	unittest.main()