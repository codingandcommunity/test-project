import random

# Starter Code 1
deck = ["AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS",
        "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH",
        "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC",
        "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"]

def shuffle(deck):
    ### STEP 1
    for i in range(0, 100):
        j = random.randint(0, len(deck)-1)
        k = random.randint(0, len(deck)-1)
        temp = deck[j]
        deck[j] = deck[k]
        deck[k] = temp
    ### END STEP 1

# Starter Code 1
print("Unshuffled deck: ", deck)
shuffle(deck)
print("Shuffled deck: ", deck)

def deal(deck1,deck2):
    ### STEP 2
    deck2.append(deck1.pop())
    ### END STEP 2

# Starter Code 2
players = list()

for i in range(2):
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
    
    ### END STEP 3