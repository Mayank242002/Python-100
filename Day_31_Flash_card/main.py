from textwrap import fill
import time
import pandas as pd
from tkinter import *
import random


BACKGROUND_COLOR = "#d3f0e1"
current_card={}

def new_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card=list[random.randint(0,len(list)-1)]
    canvas.itemconfig(word_text,text=current_card['French'],fill="black")
    canvas.itemconfig(title_text,text="French",fill="black")
    canvas.itemconfig(image_container,image=card_img)
    flip_timer=window.after(3000,func=flip_card)

def flip_card():
   
   
    canvas.itemconfig(image_container,image=back_img)
    canvas.itemconfig(word_text,text=current_card["English"],fill="white")
    canvas.itemconfig(title_text,text="English",fill="white")

def update_csv():
 
    list.remove(current_card)
    df2=pd.DataFrame(list)
    df2.to_csv("Day_31_Flash_card/data/words_to_learn.csv",index=False)


window=Tk()
window.title("Flashy")
window.config(padx=50,pady=60,bg=BACKGROUND_COLOR)

flip_timer=window.after(3000,func=flip_card)

try:
    new_words_df=pd.read_csv("Day_31_Flash_card/data/words_to_learn.csv")
except FileNotFoundError:
    df=pd.read_csv("Day_31_Flash_card/data/french_words.csv")
    list=df.to_dict(orient="records")
else:
    list=new_words_df.to_dict(orient="records")





canvas=Canvas(width=800,height=550,bg=BACKGROUND_COLOR,highlightthickness=0)
card_img=PhotoImage(file="Day_31_Flash_card/images/card_front.png")
back_img=PhotoImage(file="Day_31_Flash_card/images/card_back.png")
image_container=canvas.create_image(410,270,image=card_img)
title_text=canvas.create_text(400,100,text="French",font=("Ariel", 30, "italic"))
word_text=canvas.create_text(400,250,text="",font=("Ariel", 40, "bold"))
canvas.grid(column=0,row=0,columnspan=2)

wrong_img=PhotoImage(file="Day_31_Flash_card/images/wrong.png")
wrong_button=Button(image=wrong_img,highlightthickness=0,command=new_word)
wrong_button.grid(column=0,row=1)
wrong_button.config(padx=50,pady=15)

right_img=PhotoImage(file="Day_31_Flash_card/images/right.png")
right_button=Button(image=right_img,highlightthickness=0,command=update_csv)
right_button.grid(column=1,row=1)
right_button.config(padx=50,pady=15)

new_word()


window.mainloop()


