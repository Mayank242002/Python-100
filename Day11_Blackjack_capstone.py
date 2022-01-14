import random

cards=[11,1,2,3,4,5,6,7,8,9,10,10,10,10]
users=[]
computer=[]
game=True
def make_move(cards):
    random_card=random.choice(cards)
    return random_card

def sum(list):
    total=0
    for i in list:
        total+=i
    return total

def check_win(users,computers):
    if (sum(users)>sum(computers) & sum(users)<=21):
        print("User win")
    elif (sum(users)<sum(computers) & sum(computer)<=21):
        print("Dealer Win")
    elif (sum(users)==sum(computer)):
        print("Match Draw")


print("Welcome to the Black Jack Game")
users.append(make_move(cards))
users.append(make_move(cards))
computer.append(make_move(cards))
print("Users: ",users)
print("Dealer: ",computer)
while game:
    if (sum(users)>21):
        game=False
        print("Dealer Win")
    elif (sum(users)<=21):
        choice=input("enter 'yes' to make move and 'no' to pass:")
        if (choice=="yes"):
            users.append(make_move(cards))
            print("Users: ",users)
            print("Dealer: ",computer)
        elif (choice=="no"):
            while (sum(computer)<17):
                random_card2=make_move(cards)
                computer.append(random_card2)
                print("Dealer: ",computer)
            print("Users: ",users)
            if (sum(computer)>21):
                print("User Wins")
            check_win(users,computer)
            break
            
            


            



