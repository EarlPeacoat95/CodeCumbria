import random

class Player:
    __location = [0,0]
    health = 100
    inventory = []

    def move(self, x:int, y:int):
        pass

    def attack(self):
        pass

    def pickup(self):
        pass


class Enemy:
    location = [100,100]
    health = 100
    enemyType = 1
    damage = 10

    def __init__(self, typeOfEnemy):
        self.damage = random.randint(8,12)
        self.enemyType = typeOfEnemy

    def move(self, x, y):
        pass

    def attack(self):
        pass


p = Player()

print(p.health)

enemies =[]
for i in range(0,100):
    enemies += [Enemy()]



