import random

def game_win(user,computer):
 if user==computer:
    return None

    #SNAKE VS WATER
 if user=="s" and computer=="w":
  return True
 if user=="w" and computer=="s":
     return False
   # WATER VS GUN
 if user=="w" and computer=="g":
  return True
 if user=="g" and computer=="w":
  return False
    # GUN VS SNAKE 
 if user=="g" and computer=="s":
     return True
 if user=="s" and computer=="g":
     return False

random_no=random.randint(1,3)
print("compueter's trun: snake(s), water(w), gun(g)")
if random_no==1:
 computer="s"
elif random_no==2:
 computer="w"
else:
 computer="g"

 user=input("your turns: snake(s), water(w), gun(g):").lower()
result=game_win(user,computer)
print(f"\nyou choice:{user}")
print(f"\ncomputer choice:{computer}")

if result is None:
 print("its draw")
elif (result):
  print("you win")
else:
 print("you loss")