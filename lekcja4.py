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

playersDictionary = {
                        'firstPlayer':[],
                        'secondPlayer':[],
                        'thirdPlayer':[],
                        'fourthPlayer':[],
                        'fifthPlayer':[],

                    }

# Lista graczy
playerList = list(playersDictionary.keys())

# Funkcja rozdająca karty
def give_cards(playersDictionary, cardList):
    for player in playersDictionary:
        for _ in range(5):
            card = cardList.pop()
            playersDictionary[player].append(card)
        print(f"Karty gracza {player}: {playersDictionary[player]}")

# Rozdaj karty każdemu graczowi
give_cards(playersDictionary, cardList)

# Pozostałe karty
print("Pozostałe karty w talii:", cardList)



