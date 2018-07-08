from army import *


W1 = Healer()
W2 = Vampire()

A1 = Army(Vampire, 10)
A2 = Army(Healer, 20)

B1 = Battle(A1, A2)
B1.ww_fight(W1, W2)

B1.fight()