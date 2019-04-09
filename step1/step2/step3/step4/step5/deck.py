import random

def shuffle(deck):
    ### STEP 1
    for i in range(100):
        j = random.randint(0, len(deck)-1)
        k = random.randint(0, len(deck)-1)
        temp = deck[j]
        deck[j] = deck[k]
        deck[k] = temp
    return deck
    ### END STEP 1
    
def deal(deck1,deck2):
    ### STEP 2
	deck2.append(deck1.pop(0))
    ### END STEP 2 
    
def switch(argument):
    switcher = {
        "A": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13
        }
    if argument[:-1] in switcher.keys():
        return switcher.get(argument[:-1])
    else:
        return "Invalid card!"
    
def compare_card(p1Card, p2Card):
    ### STEP 3
    if switch(p1Card) > switch(p2Card):
        return 1
    elif switch(p1Card) < switch(p2Card):
        return 2
    elif switch(p1Card) == switch(p2Card):
        return 3    
    ### END STEP 3
    
def print_table(hand1card, hand2card):
    if hand1card[-1] == "C":
        suit = "\u2663"
    elif hand1card[-1] == "S":
        suit = "\u2660"
    elif hand1card[-1] == "D":
        suit = "\u2666"
    elif hand1card[-1] == "H":
        suit = "\u2665"
        
    if hand2card[-1] == "C":
        suit2 = "\u2663"
    elif hand2card[-1] == "S":
        suit2 = "\u2660"
    elif hand2card[-1] == "D":
        suit2 = "\u2666"
    elif hand2card[-1] == "H":
        suit2 = "\u2665"
        
    if len(hand1card[:-1]) == 1 and len(hand2card[:-1]) == 1:
        topstring = ("| {}       |         | {}       |").format(hand1card[:-1], hand2card[:-1])
    elif len(hand1card[:-1]) == 2 and len(hand2card[:-1]) == 1:
        topstring = ("| {}      |         | {}       |").format(hand1card[:-1], hand2card[:-1])
    elif len(hand1card[:-1]) == 1 and len(hand2card[:-1]) == 2:
        topstring = ("| {}       |         | {}      |").format(hand1card[:-1], hand2card[:-1])
    elif len(hand1card[:-1]) == 2 and len(hand2card[:-1]) == 2:
        topstring = ("| {}      |         | {}      |").format(hand1card[:-1], hand2card[:-1])
        
    if len(hand1card[:-1]) == 1 and len(hand2card[:-1]) == 1:
        botstring = ("|       {} |         |       {} |").format(hand1card[:-1], hand2card[:-1])
    elif len(hand1card[:-1]) == 2 and len(hand2card[:-1]) == 1:
        botstring = ("|      {} |         |       {} |").format(hand1card[:-1], hand2card[:-1])
    elif len(hand1card[:-1]) == 1 and len(hand2card[:-1]) == 2:
        botstring = ("|        {}|         |      {} |").format(hand1card[:-1], hand2card[:-1])
    elif len(hand1card[:-1]) == 2 and len(hand2card[:-1]) == 2:
        botstring = ("|      {} |         |      {} |").format(hand1card[:-1], hand2card[:-1])
        
    d = "\u2500"
    print("\u250C",d,d,d,d,"\u2510"+"         "+"\u250C",d,d,d,d,"\u2510")
    print(topstring)
    print("|         |         |         |")
    print("|    {}    |   VS.   |    {}    |".format(suit, suit2))
    print("|         |         |         |")
    print(botstring)
    print("\u2514",d,d,d,d,"\u2518"+"         "+"\u2514",d,d,d,d,"\u2518")
    
def turn(p1hand, p2hand):
    ### STEP 4
    p1 = players[0]
    p2 = players[1]
    result = compare_card(players[0][0], players[1][0])
    table = [] ###Current cards in play
    deal(p1, table)
    deal(p2, table)
    print_table(table[-2], table[-1])
    
    if result == 1:
        deal(table, p1)
        deal(table, p1)
        ###print("p1" + str(p1))
        ###print("p2" + str(p2))
        return 1
    elif result == 2:
        deal(table, p2)
        deal(table, p2)
        ###print("p1" + str(p1))
        ###print("p2" + str(p2))
        return 2
    elif result == 3:

        while True:
            p1size = len(players[0])
            p2size = len(players[1])

            if (p1size == 0 and p2size == 0):
                print("Neither player has enough cards!")
                return 4

            ###Throw down 4 cards for war from players[0]
            if p1size >= 4:
                hand1list = p1[:4]
                table = table + hand1list
                i = 0
                while i < 4:
                    del p1[0] ###remove cards from hand
                    i+=1
            elif p1size < 4:
                if p1size > 0:
                    hand1list = p1
                    table = table + hand1list
                else:
                    print("Hand1 does not have enough cards")
                    p2 = p2 + table
                    return 2

            ###Throw down 4 cards for war from players[1]
            if p2size >= 4:
                hand2list = p2[:4]
                table = table + hand2list
                i = 0
                while i < 4:
                    del p2[0] ###remove cards from hand
                    i+=1
            elif p2size < 4:
                if p2size > 0:
                    hand2list = p2
                    table = table + hand2list
                else:
                    print("Hand2 does not have enough cards")
                    p1 = p1 + table
                    return 1

            result = compare_card(hand1list[-1], hand2list[-1])
            print_table(hand1list[-1], hand2list[-1])	    
            if result == 1:
                p1 = p1 + table
                return 1
            elif result == 2:
                p2 = p2 + table
                return 2
            elif result == 3:
                if p1size > 0 and p2size > 0:
                    continue
                else:
                    if p1size == 0:
                        print("Hand1 does not have enough cards to continue")
                        p2 = p2 + table
                        return 2
                    elif p2size == 0:
                        print("Hand2 does not have enough cards to continue")
                        p1 = p1 + table
                        return 1    
    ### END STEP 4    
    
    
def play_game():
    ### STEP 5
    pass
    ### END STEP 5
    
if __name__ == '__main__':
	# Starter Code 1
    deck = ["AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS",
        "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH",
        "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC",
        "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
    print("Unshuffled deck: ", deck) 
    newDeck = shuffle(deck)
    print("Shuffled deck: ", newDeck)
	# Starter Code 2

    players = list()
    players.append(list())
    players.append(list())
    j = 0
    while len(deck) != 0:
        deal(deck,players[j%2])
        j += 1

    for i in range(2):
        print("Hand %d:" % (i), players[i])
    shuffle(players[0])
    shuffle(players[1])
    for i in range(2):
        print("Hand %d:" % (i), players[i])