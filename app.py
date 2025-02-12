#lets create the wariors file to show battle between two woriors 

import random
import math

class warrior:
    def __init__(self,name="",health=0,attack=0,block=0):
        self.name=name
        self.health=health
        self.attack=attack
        self.block=block
    def block1(self):
        return self.block*(random.random()+.5)
    def attack1(self):
        return self.attack * (random.random()+.5)
class fighting:
    def start_fighting(self, warrior1,warrior2):
        while True:
            if self.get_attack_result(warrior1,warrior2)=="Game Over":
                print("Game Over")
                break
            if self.get_attack_result(warrior2,warrior1)=="Game Over":
                print("Game Over")
                break
    def get_attack_result(self, warriorA, warriorB):
        attack_result = math.ceil(warriorA.attack1() - warriorB.block1())
        if attack_result > 0:
            warriorB.health = warriorB.health - attack_result
        else:
            attack_result = 0
        print("{} attacks {} and deals {} damage".format(warriorA.name, warriorB.name, attack_result))
        print("{} is down to {} health".format(warriorB.name, warriorB.health))
        if warriorB.health <= 0:
            print("{} has died and {} is the winner".format(warriorB.name, warriorA.name))
            return "Game Over"
        else:
            return "Fight Again"
def main():
    maximus = warrior("Maximus", 50, 20, 10)
    commodus = warrior("Commodus", 50, 20, 10)
    battle = fighting()
    battle.start_fighting(maximus, commodus)
main()
