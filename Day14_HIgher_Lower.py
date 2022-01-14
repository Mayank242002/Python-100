import random
data=[
    {
        'name':'Instagram',
        'follower_count':346,
        'description':'Social Media Platform',
        'country':'United states'
    },
    {
        'name':'Ronaldo',
        'follower_count':340,
        'description':"Footballer",
        'country':'Portugal'
    },
    {
        'name':'Ariana Grande',
        'follower_count':183,
        'description':'Musician and actress',
        'country':'United states'
    },
    {
        'name':'Dwayane jonson',
        'follower_count':290,
        'description':'Actor',
        'country':'United states'
    },
    {
        'name':'salman khan',
        'follower_count':200,
        'description':"actor",
        'country':'India'
    }
]

score=0
rand1=random.randint(0,len(data)-1)
rand2=random.randint(0,len(data)-1)
choice_1=data[rand1]
choice_2=data[rand2]
if (choice_1==choice_2):
    choice_2=random.choice(data)
while True:
    print("Compare A:",choice_1["name"],",",choice_1["description"]," from ",choice_1["country"])
    print("VS")
    print("Against B:",choice_2["name"],",",choice_2["description"]," from ",choice_2["country"])
    guess=input("Who has more followers? Type 'A' or 'B':")
    if ((guess=='A') & (choice_1["follower_count"]>choice_2["follower_count"])):
        score+=1
        choice_1=choice_2.copy()
        choice_2=data[random.randint(0,len(data)-1)]
    elif ((guess=='B') & (choice_2["follower_count"]>choice_1["follower_count"])):
        score+=1
        choice_1=choice_2.copy()
        choice_2=data[random.randint(0,len(data)-1)]
    else:
        print("Sorry thats wrong")
        print("Final score:",score)
        break