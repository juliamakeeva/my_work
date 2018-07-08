import army

import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.unit1 = army.Warrior()
        self.unit2 = army.Vampire()
        self.unit3 = army.Healer()
        self.unit4 = army.Mechnik()
        self.unit5 = army.Konnica()
        self.A1 = army.Army(army.Vampire, 10)
        self.A2 = army.Army(army.Healer, 20)
        self.B1 = army.Battle(self.A1, self.A2)


    def test_healer_vs_vampire (self):
        self.assertFalse(self.B1.ww_fight(self.unit3, self.unit2))


if __name__ == '__main__':
    unittest.main()