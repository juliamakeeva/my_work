import war
import unittest

class TestWar(unittest.TestCase):
    def setUp(self):
        self.war1 = war.Warrior()
        self.war2 = war.Warrior()
        self.arm1 = war.MixedArmy(20, 30)
        self.arm2 = war.MixedArmy(15, 10)

    def test_check_hp_before(self):
        self.assertEqual(self.war1.health, 25) 
        self.assertEqual(self.war2.health, 25)

    def test_check_hp_after(self):
        war.Fight(self.war1, self.war2)
        self.assertEqual(self.war1.health, -2) 
        self.assertEqual(self.war2.health, -2)

    def test_check_total_hp_before(self):
        self.assertEqual(self.arm1.total_hp, 2200) 
        self.assertEqual(self.arm2.total_hp, 1025)

    def test_check_total_at_after(self):
        self.assertEqual(self.arm1.total_at, 400) 
        self.assertEqual(self.arm2.total_at, 175)

    def test_check_total_hp_hp_after(self):
        war.ArmyFight(self.arm1, self.arm2)
        self.assertEqual(self.arm1.total_at, 400) 
        self.assertEqual(self.arm2.total_at, 175)
    
    
    
        
        
if __name__ == '__main__':
    unittest.main()