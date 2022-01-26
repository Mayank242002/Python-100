from tkinter import *
from quiz_brain import Quiz_brain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz_brain: Quiz_brain):
        self.quiz=quiz_brain

        self.window=Tk()
        self.window.title("Quiz App")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
      

        self.score_label=Label(text="SCORE: 0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(column=1,row=0)
        self.score_label.config(padx=20,pady=20)

        self.canvas=Canvas(width=400,height=300,background="white",highlightthickness=0)
        self.quiz_q=self.canvas.create_text(200,150,text="Question hu mian",font=("Arial",20,"italic"),width=380)
        self.canvas.grid(column=0,row=1,columnspan=2,padx=25,pady=25)
        
        

        true_img=PhotoImage(file="Day_17_Quiz_Project/images/true.png")
        wrong_img=PhotoImage(file="Day_17_Quiz_Project/images/false.png")
        self.true_button=Button(image=true_img,highlightthickness=0,padx=15,pady=50,command=self.true_input)
        self.false_button=Button(image=wrong_img,highlightthickness=0,padx=15,pady=50,command=self.false_input)
        
        self.true_button.grid(column=0,row=2)
        self.false_button.grid(column=1,row=2)

        self.get_next_question()

        self.window.mainloop()  

    def get_next_question(self):
        self.canvas.config(bg="white")
        if (self.quiz.question_number>10):
            self.canvas.itemconfig(self.quiz_q,text="You have reached the end of the Quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        else:
            question_to_ask=self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_q,text=question_to_ask)

        

    def true_input(self):
        is_right=self.quiz.check_answer("True")
        self.change_bg(is_right)
        self.maintain_score()
        self.give_feedback()
        
        
    
    def false_input(self):
        is_right=self.quiz.check_answer("False")
        self.change_bg(is_right)
        self.maintain_score()
        self.give_feedback()

    def maintain_score(self):
        score=self.quiz.score
        self.score_label.config(text=f"SCORE: {score}")
 
    def give_feedback(self):
        self.window.after(1000,func=self.get_next_question)


    def change_bg(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        
