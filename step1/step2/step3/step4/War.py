import random

# Starter Code 1
deck = ["AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS",
        "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH",
        "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC",
        "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"]

def shuffle():
    ### STEP 1
    for i in range(0, 100):
        j = random.randint(0, 51)
        k = random.randint(0, 51)
        temp = deck[j]
        deck[j] = deck[k]
        deck[k] = temp
    ### END STEP 1

# Starter Code 1
print("Unshuffled deck: ", deck)
shuffle()
print("Shuffled deck: ", deck)

def deal():
    ### STEP 2
    return deck.pop()
    ### END STEP 2

# Starter Code 2
players = list()
for i in range(5):
    players.append(list())
j = 0
while len(deck) != 0:
    players[j%5].append(deal())
    j += 1
for i in range(5):
    print("Hand %d:" % (i), players[i])

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
    if switch(p1Card) > switch(p2Card):
        return 1
    elif switch(p1Card) < switch(p2Card):
        return 2
    elif switch(p1Card) == switch(p2Card):
        return 3

def war(p1hand, p2hand):
    p1size = len(p1hand)
    p2size = len(p2hand)
    
    ###Throw down 4 cards for war from p1hand
    if p1size >= 4:
        hand1list = p1hand[:4]
        i = 0
        while i < 4:
            del p1hand[0] ###remove cards from hand
            i+=1
    elif p1size < 4:
        if p1size > 0:
            hand1list = p1hand
        else:
            print("Hand1 does not have enough cards")
            return 2
    
    ###Throw down 4 cards for war from p2hand
    if p2size >= 4:
        hand2list = p2hand[:4]
        i = 0
        while i < 4:
            del p2hand[0] ###remove cards from hand
            i+=1
    elif p2size < 4:
        if p2size > 0:
            hand2list = p2hand
        else:
            print("Hand2 does not have enough cards")
            return 1
      
    result = compare_card(hand1list[-1], hand2list[-1])
    
    if result == 1:
        return 1
    elif result == 2:
        print('hi') ##this prints
        return 2 ##this doesn't return :(
    elif result == 3:
        if p1size > 0 and p2size > 0:
            war(p1hand, p2hand) ###call the war function again if tied
        else:
            if p1size == 0:
                print("Hand1 does not have enough cards to continue")
                return 2
            elif p2size == 0:
                print("Hand2 does not have enough cards to continue")
                return 1    
        
        
        
        
        
        

#print(switch(players[0][0]))
#print(switch(players[1][0]))

#print(compare_card(players[0][0], players[1][0]))
    
#if compare_card((switch(players[0][0])), (switch(players[1][0]))) == 3:
 
#test1 = ["10S", "1S", "2H", "3D", "1H", "2C", "3D", "4S", "5H", "6C", "7D", "8S", "9H", "10C", "JD", "QS", "KH", "1C", "2D", "3S", "4H", "5C", "6D", "8S"]
#test2 = ["10S", "1S", "2H", "3D", "1H", "2C", "3D", "4S", "5H", "6C", "7D", "8S", "9H", "10C", "JD", "QS", "KH", "1C", "2D", "3S", "4H", "5C", "6D", "7S"]

test1 = ["1D"]
test2 = ["2D"]

print(war(test1, test2))

