import random

class Warrior:
    attack = 3
    health = 25
        
class Swordsman(Warrior):
    attack = 5
    health = 35
    
class Archer(Warrior):
    attack = 10
    health = 50
    
class Healer(Warrior):
    pass
       
class Vampire(Warrior):
    pass
            
class Fight(Warrior):
    def __init__(self, war1, war2):
        self.war1 = war1
        self.war2 = war2
        while self.war1.health > 0 and self.war2.health > 0:
            self.war2.health -= self.war1.attack
            print('HP2: ', self.war2.health)
            self.war1.health -= self.war2.attack
            print('HP: ', self.war1.health)

        if self.war1.health > self.war2.health:
            print('War1 win')
        elif self.war1.health < self.war2.health:
            print('War2 win')
        else:
            print('No winner')

class ArmyFight(Fight):
    def __init__(self, army1, army2):
        self.army1 = army1
        self.army2 = army2
        i = 1
        while self.army1.total_hp > 0 and self.army2.total_hp > 0:
            print('Round: ', i)
            print('Army 1 total hp: {}, Army 1 total att: {}'.format(self.army1.total_hp, self.army1.total_at))
            print('Army 2 total hp: {}, Army 2 total att: {}'.format(self.army2.total_hp, self.army2.total_at))
            self.army1.total_hp -= self.army2.total_at
            print('FIGHT')
            print('Army 1 HP left: ', self.army1.total_hp)
            self.army2.total_hp -= self.army1.total_at
            print('Army 2 HP left: ', self.army2.total_hp)
            i += 1
        print('*' * 50)
        if self.army1.total_hp > self.army2.total_hp:
            print('Army 1 WIN')
        else:
            print('Army 2 WIN')
     
    
class MixedArmy(Swordsman, Archer):
    def __init__(self, amount_sw, amount_arch):
        self.amount_sw = amount_sw
        self.amount_arch = amount_arch
        self.total_hp = 0
        self.total_at = 0
        army = []
        
        for i in range(self.amount_sw):
            self.total_at += Swordsman.attack
            self.total_hp += Swordsman.health
            army.append(Swordsman)
        for i in range(self.amount_arch):
            self.total_at += Archer.attack
            self.total_hp += Archer.health
            army.append(Archer)
        random.shuffle(army)