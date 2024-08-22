"""
sample - próbka/przykład

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


for i in range(0,25):
    # card = cardList.pop()
    if i < 5:
        firstPlayer  = []
        firstPlayer.append(cardList[i])

print(firstPlayer)
print(cardList)

# def choose_random_numbers(amount,total_amount):
#     print(random.sample(range(total_amount + 1),amount))

# choose_random_numbers(6,49)