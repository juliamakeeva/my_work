class Warrior:
    health = 50
    attack = 10

    def real_attack(self, warr):
        return warr.attack

    def kick(self, warr):
        warr.health -= warr.real_attack(self)

    def is_alive(self):
        return not self.health <=0

    def show_status(self):
        print("H:{}".format(self.health))


class Mechnik(Warrior):
    attack = 20

class Konnica(Warrior):
    defence = 5

    def real_attack(self, warr):
        real_attack = warr.attack - self.defence
        if real_attack > 0:
            return real_attack

        return 0

class Healer(Warrior):
    attack = 10
    health = 40

class Vampire(Warrior):
    health = 30
    attack = 10
    max_health = 50


    def kick(self, warr):

        super().kick(warr)

        if (self.health + self.attack * 0.5) <= self.max_health:
            self.health += self.attack * 0.5

class Army:
    def __init__(self, cls, amount):
        self.units = []
        for i in range(amount):
            self.units.append(cls())

class Battle:
    def __init__(self, army1, army2):
        self.army1 = army1
        self.army2 = army2

    def ww_fight(self, war1, war2):
        kicker = war1
        reciever = war2

        while war1.is_alive() and war2.is_alive():
            kicker.kick(reciever)
            kicker, reciever = reciever, kicker
            war1.show_status()
            war2.show_status()
            print("ROUND")

        return war1.is_alive()

    def fight(self):
        army1 = self.army1
        army2 = self.army2
        while army1.has_units() and army2.has_units():
            kicker = army1.get_first()
            reciever = army2.get_first()

            result = self.ww_fight(kicker, reciever)

            if result:
                army2.remove_unit()
            else:
                army1.remove_unit()