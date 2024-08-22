"""
Napisz krótką grę w której masz 5 ruchów w jedną stronę poprzez KOMNATĘ.

za każdym razem masz szansę spotkać po drodzę skrzynkę lub NIC.

Skrzynki mają różne kolory.

Kolor skrzynki oznacza jak rzadka jest ta skrzynka.

zielona - 75%
pomarańczowa - 20%
fioletowa - 4%
złota (legendarna) - 1%

Ustaw, że jest 40%, że nie spotkasz niczego. 60%, że będzie to skrzynka.

Ustaw złoto jako to co może wypaść ze szkrzynki:

zielony - 1000
pomaranczowy - 4000
fioletowy - 9000
zlota - 16000

Pamiętaj o:
1) Czytsym kodzie
2) nazywaniu zmiennych tak by było samoopisujące się
3) spróuj napisać program po angielsku"""

import random
from enum import Enum

Event = Enum('Event', ['Chest','Empty'])

eventDictionary = {
    Event.Chest: 0.6,
    Event.Empty: 0.4
}


eventList = list(eventDictionary.keys())
eventProbability = list(eventDictionary.values())

Colours = Enum('Colours', {'Green': 'zielony',
                           'Orange': 'pomaranczowy',
                           'Purple': 'fioletowy',
                           'Gold': 'złoty'}
                           )

eventColoursDictionary = {
            Colours.Green : 0.75,
            Colours.Orange : 0.2,
            Colours.Purple : 0.04,
            Colours.Gold : 0.01 
}


chestColourList = tuple(eventColoursDictionary.keys())
chestColourProbability = list(eventColoursDictionary.values())


rewardForChests = {
            chestColourList[reward] : (reward+1)*(reward+1)*1000
            for reward in range(len(chestColourList))
}

gameLenght = 5
goldAcquired = 0
while gameLenght > 0:
    
    gamerAnswer = input("Do you want to move forward?")
    if(gamerAnswer == "yes"):
        print("Greate, let's see what you got...")
        drawEvent = random.choices(eventList,eventProbability)[0]

        if drawEvent == Event.Chest:
            print("You have drawn a CHEST")
            drawColor = random.choices(chestColourList,chestColourProbability)[0]
            print("The chest is", drawColor.value)
            gamerReward = rewardForChests[drawColor]
            goldAcquired += gamerReward

        elif drawEvent == Event.Empty:
            print("You have drawn nothing")

    else:
        print("You can go just straith man, nothing else")
    
    gameLenght-=1

print("you earn", goldAcquired)

