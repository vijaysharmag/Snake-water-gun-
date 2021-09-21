##### snake water gun game

import random


def gameWin(comp, vijay):
    if comp == vijay:
        return None
    elif comp == 'g':
        if vijay == 's':
            return True
        elif vijay == 'w':
            return False
    elif comp == 'w':
        if vijay == 's':
            return True
        elif vijay == 'g':
            return False
    elif comp == 's':
        if vijay == 'g':
            return True
        elif vijay == 'w':
            return False


print("comp turn: snake(s) water(w) gun(g)? ")
randNo = random.randint(1, 3)
print(randNo)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

vijay = input("your turn : snake(s) water(w) gun(g)? ")
a = gameWin(comp, vijay)
print(f"computer choose {comp}")
print(f"vijay choose {vijay}")
if a == None:
    print("this game is tie!")
elif a:
    print("vijay win")
else:
    print("vijay lose")