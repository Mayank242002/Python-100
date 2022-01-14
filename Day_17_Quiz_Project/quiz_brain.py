class Quiz_brain:

    def __init__(self,list):
         self.question_number=1
         self.question_list=list
         self.score=0

    def still_question(self):
        if (self.question_number>len(self.question_list)):
            return False
        else:
            return True

    def check_answer(self,user_input,current_question):
        if (user_input==current_question.answer):
            self.score+=1
            print("You got it right.")
        else:
            print("You got it Wrong.")
            print("Total score:",self.score)

    def next_question(self):
        current_question=self.question_list[self.question_number-1]
        user_input=input(f"Q.{self.question_number}: {current_question.text}. True/False?:")
        self.check_answer(user_input,current_question)
        self.question_number+=1

   
        






