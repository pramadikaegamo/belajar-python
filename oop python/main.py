# __ -> private acces modfier
# _ -> protected


class player:
    def __init__(self, health=100, energy=100):
        self.health = health
        self.energy = energy

    def attack(self, target, damage=1):
        target.health -= damage
        self.energy -= damage
        print(f"attacking to monster, monster health : {target.health} left")


class monster:
    def __init__(self, health=500):
        self.health = health


player1 = player()
player2 = player()
dragon = monster(10000)


player1.attack(target=dragon, damage=80)
player2.attack(target=dragon)
