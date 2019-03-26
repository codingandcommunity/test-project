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