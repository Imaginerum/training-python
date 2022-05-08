import random

def choose_random_numbers(amount, total_amount):
    print(random.sample(range(total_amount+1), amount))

choose_random_numbers(6, 49)
from enum import Enum

def findAproximateValue(value, percentRange):
    lowestValue = value - percentRange / 100 * value
    highestValue = value + percentRange / 100 * value
    return random.randint(lowestValue, highestValue)

Event = Enum("Event", ["Chest", 'Empty'])
gameLength = 5
eventDictionary = {Event.Chest: 0.6, Event.Empty: 0.4}

eventList = tuple(eventDictionary.keys())
eventPropability = tuple(eventDictionary.values())

Colours = Enum("Colours", {"Green": "zielony",
                           "Orange": "pomarańczowy",
                           "Purple": "fioletowy",
                           "Gold": "złoty"})
chestColoursDictionary = {
                            Colours.Green : 0.75,
                            Colours.Orange : 0.2,
                            Colours.Purple : 0.04,
                            Colours.Gold : 0.01
}
chestColoursList = tuple(chestColoursDictionary.keys())
chestColoursPropability = tuple(chestColoursDictionary.values())

rewardsForChests = {
                    chestColoursList[reward]: (reward + 1)*(reward + 1)* 1000
                    for reward in range(len(chestColoursList))
}
goldAcquired = 0

print("Welcom in my game called KOMNATA.")
print("""You have only 5 steps to make, 
        see for yourself how much gold you gonna acquire till the end!""")
while gameLength > 0:
    gameAnswer = input("Do you want to move forward?\n")
    if (gameAnswer == 'yes'):
        print("Great! Let's see what you got!")
        drawnEvent = random.choices(eventList, eventPropability)[0]
        if drawnEvent == Event.Chest:
            print("You've drawn a CHEST")
            drawnChest = random.choices(chestColoursList, chestColoursPropability)[0]
            print("The chest colour is", drawnChest.value)
            gamerReward = findAproximateValue(rewardsForChests[drawnChest], 10)
            goldAcquired += gamerReward
        elif drawnEvent == Event.Empty:
            print("You've drawn nothing. You are so unlucky!")
    else:
        print("You can only go foward man. This game is simple")
        continue
    gameLength -= 1
print("\nCongratulation. You have acquired", goldAcquired, "gold")