import random
HANGMAN_PICS = ['''
   +---+
       |
       |
       |

  ======''', '''
   +---+
   O   |
       |
       |

  ======''', '''
   +---+
   O   |
   |   |
       |

  ======''', '''
    +---+
    O   |
   /|   |
        |

  ======''', '''
    +---+
    O   |
   /|\  |
        |

  ======''', '''
    +---+
    O   |
   /|\  |
   /    |

  ======''', '''
   +---+
    O   |
   /|\  |
   / \  |

  ======''']
word_list=["ardvark","baboon","camel"]
rand_choosen=random.randint(0,len(word_list)-1)
chosen_word=word_list[rand_choosen]
chosen_word_length=len(chosen_word)
display=[]
death_count=1
for i in chosen_word:
    display.append("_")

while ("_" in display):
    guess=str(input("Guess a letter:"))
    guess=guess.lower()

    if guess in display:
        print("You have already guessed ",guess)

    flag=0
    
    for i in range(chosen_word_length):
        if (guess==chosen_word[i]):
            display[i]=guess
            flag=1

    
    print(display)

    if (flag==0):
        print("You guessed ",guess,", which is not present in the List.You Lose a Life.")
        print(HANGMAN_PICS[death_count-1])
        if (death_count==7):
            print("You lose")
            break
          
        death_count+=1

    

    if "_" not in display:
        print("you won")
        break



       