import random

def game(user,computer):
    if user==computer:
        return None
     #snake vs water
    if user=="s" and computer=="w":
     return True
    if user=="w" and computer=="s":
      return False
     # water vs gun
    if user=="w" and computer=="g":
     return True
    if user=="g" and computer=="w":
      return False
     #gan vs snake
    if user=="g" and computer=="s":
     return True
    if user=="s" and computer=="g":
      return False
      
 
random_no=random.randint(1,3)
print("compueter turn:snake(s),water(w),gun(g):")
if random_no==1:
    computer="s"
elif random_no==2:
    computer="g"
else:
    computer="w"
user=input("user turns:snake(s),water(w),gun(g):").lower()
result=game(user,computer)
print(f"user choice:{user}")
print(f"computer choice:{computer}")

if result is None:
    print("game draw")
elif(result):
    print("you win")
else:
    print("lose!")