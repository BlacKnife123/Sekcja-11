"""
choice - zwraca losowy element
choices - zwraca listę elementów i ma większe możliwości

"""

import random
from collections import Counter

movieList = ["Avengers 1", "Avengers 2", "Avengers 3" ,"Avengers 4"]

event = ["śmierć", "wygrana", "przegrana", "utrata złota", "utrata życia"]

nagrodaZeSkrzynki = ["zielona", "pomarańczowa", "purpurowa", "legendarna"]


print(random.choice(movieList))

print(Counter(random.choices(nagrodaZeSkrzynki,[0.8,0.15,0.04,0.01],k = 100)))