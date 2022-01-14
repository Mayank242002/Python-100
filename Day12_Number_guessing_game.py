import random
art="""
   _   _                 _                  _____                     _                _____                      
 | \ | |               | |                / ____|                   (_)              / ____|                     
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ _ _ __   __ _  | |  __  __ _ _ __ ___   ___ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __| | '_ \ / _` | | | |_ |/ _` | '_ ` _ \ / _ \
 | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \ | | | | (_| | | |__| | (_| | | | | | |  __/
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/_|_| |_|\__, |  \_____|\__,_|_| |_| |_|\___| 
                                                                                |  |
                                                                              |___/   
"""

print(art)
print("welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
choice=input("Choose a difficulty level.Type 'easy' or 'hard':")
life=0
if  choice=="easy":
    life=10
else:
    life=5

flag=0
rand_no=random.randint(1,100)
print("You have ",life, "attempts to guess the number.")
for i in range(life):
    guessed_no=int(input("Make a Guess:"))
    if (guessed_no>rand_no):
        print("Too High\n")
    elif (guessed_no<rand_no):
        print("Too Low\n")
    else:
        print("You Guessed Right")
        flag=1
        break
    
if (flag==0):
    print("You Loose")


