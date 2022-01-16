import random

def game(comp,You):
    if comp == You:
        return None
    elif comp == 's':
        if You == 'w':
            return False
        elif You == 'g':
            return True

    elif comp == 'w':
        if You == 's':
            return True
        elif You == 'g':
            return False
    
    elif comp == 'g':
        if You == 's':
            return False
        elif You == 'w':
            return True
     
# print("comp:snake(1),water(2),gun(3)?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 's'

elif randNo == 2:
    comp = 'w'

elif randNo == 3:
    comp = 'g'

You = input("Your turn: Snake(s), Water(w), Gun(g)? ")
a = game(comp,You)

print(f"computer chosse {comp}")
print(f"you chosse {You}")

if a == None:
    print("Game Tie")
elif a:
    print("You win")
else:
    print("You lost")