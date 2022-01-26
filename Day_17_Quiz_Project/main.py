from question_model import  Question
from data import question_data
from quiz_brain import Quiz_brain
from ui import QuizInterface
question_bank=[]

for question in question_data:
    text=question["question"]
    answer=question["correct_answer"]
    question_bank.append(Question(text,answer))

quiz=Quiz_brain(question_bank)

quiz_ui=QuizInterface(quiz)

while quiz.still_question():
    quiz.next_question()



print("You completed the quiz")
print("Your final score:",quiz.score,"/",quiz.question_number-1)