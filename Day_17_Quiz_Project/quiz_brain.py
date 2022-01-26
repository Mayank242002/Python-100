import html

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

    def check_answer(self,user_input):
        if (user_input==self.current_question.answer):
            self.score+=1
            return True
        else:
            return False


    def next_question(self):
        if (self.question_number<=10):
            self.current_question=self.question_list[self.question_number-1]
            self.question_number+=1
            q_text=html.unescape(self.current_question.text)
        
            return f"Q.{self.question_number-1}: {q_text}"
        
        
        

    

   
        






