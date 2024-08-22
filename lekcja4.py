"""
sample - próbka/przykład

# def choose_random_numbers(amount,total_amount):
#     print(random.sample(range(total_amount + 1),amount))

# choose_random_numbers(6,49)

"""

import random

cardList = ["9","9","9","9",
            "10","10","10","10",
            "Jack", "Jack", "Jack", "Jack",
            "Queen", "Queen","Queen", "Queen",
            "King", "King", "King", "King",
            "Ace", "Ace", "Ace","Ace",
            "Joker","Joker"]

random.shuffle(cardList)
firstPlayer  = []
secondPlayer  = []
thirdPlayer  = []
fourthPlayer  = []
fifthPlayer  = []



def give_cards(Player):
    for i in range(0,25):
        if i < 5:
            card = cardList.pop()
            Player.append(card)

    print("Karty gracza",Player)

give_cards(firstPlayer)
give_cards(secondPlayer)
give_cards(thirdPlayer)
give_cards(fourthPlayer)
give_cards(fifthPlayer)

print ("Pozostałe karty",cardList)




