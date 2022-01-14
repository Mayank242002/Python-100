import random
choice=int(input("What do you choose> Type 0 for Rock, 1 for Paper, 2 for scissors."))
computer=random.randint(0,2)
if (computer==0):
    print("Computer chooses Rock")
elif (computer==1):
    print("Computer chooses Paper")
else:
    print("Computer chooses scissors")

if (computer==choice):
    print("Match Tie")
elif ((choice==2) & (computer==1)):
    print("You won")
elif ((choice==2) & (computer==0)):
    print("You lose")
elif ((choice==1) & (computer==0)):
    print("You won")
elif ((choice==1) & (computer==2)):
    print("You lose")
elif ((choice==0) & (computer==1)):
    print("You lose")
elif ((choice==0) & (computer==2)):
    print("You won")    


   