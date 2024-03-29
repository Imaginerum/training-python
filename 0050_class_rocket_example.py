from random import randint
from math import sqrt

class Rocket:
    def __init__(self, speed=1, altitude=0, x=0):
        self.altitude = altitude
        self.speed = speed

        self.x = x

    def move_up(self):
        self.altitude += self.speed

    def __str__(self):
        return "Rakieta jest aktualnie na wysokości: " + str(self.altitude)



class RocketBoard:
    def __init__(self, amountOfRockets=5):
        self.rockets = [Rocket(randint(1, 6)) for _ in range(amountOfRockets)]

        for _ in range(10):
            rocketIndexToMove = randint(0, 4)
            self.rockets[rocketIndexToMove].move_up()

        for rocket in self.rockets:
            print(rocket)

    def __getitem__(self, key):
        return self.rockets[key]
    def __setitem__(self, key, value):
        self.rockets[key].altitude = value

    @staticmethod
    def get_distance(rocket1, rocket2):
        ab = (rocket1.altitude - rocket2.altitude) ** 2
        bc = (rocket1.x - rocket2.x) ** 2
        return sqrt(ab + bc)

    def __len__(self):
        return len(self.rockets)
board = RocketBoard()

print(RocketBoard.get_distance(board[0], board[1]))