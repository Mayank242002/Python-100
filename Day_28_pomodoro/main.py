from email.mime import image
from pydoc import text
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 20
reps=0
time=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    reps=0
    Timer.config(text="Timer")
    canvas.itemconfig(timer_text,text="00:00")
    check_label.config(text="")
    global timer
    window.after_cancel(timer)
     
# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodoro")
window.config(padx=20,pady=20,bg=YELLOW)
window.config(padx=60,pady=60)

def start_timer():
    global reps
    reps+=1

    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if (reps%8==0):
        count_down(long_break_sec)
        Timer.config(text="LONG-BREAK",fg=RED)
    elif (reps%2==0):
        count_down(short_break_sec)
        Timer.config(text="SHORT-BREAK",fg=PINK)
    else:
        count_down(work_sec)
        Timer.config(text="WORK",fg=GREEN)

def count_down(count):
    count_sec=count%60
    if count_sec<10:
        count_sec="0"+str(count_sec)
    else:
        count_sec=str(count_sec)
    time_formatted_text=str(count//60)+":"+count_sec
    canvas.itemconfig(timer_text,text=time_formatted_text)
    if (count>0):
        global timer 
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        for _ in range(reps//2):
            marks+="✔"

        check_label.config(text=marks) 



Timer=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,24,"bold"))
Timer.grid(column=1,row=0)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="Day_28_pomodoro/tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,20,"bold"))
canvas.grid(column=1,row=1)

start_button=Button(text="Start",fg='black',bg="white",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

check_label=Label(text="",fg=GREEN,bg=YELLOW,font=(FONT_NAME,30,"bold"))
check_label.config(padx=20,pady=20)
check_label.grid(column=1,row=2)


reset_button=Button(text="Reset",fg='black',bg="white",highlightthickness=0,command=reset)
reset_button.grid(column=2,row=2)




window.mainloop()