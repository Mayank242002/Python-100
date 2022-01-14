class Question:
    def __init__(self,text,answer):
        self.text=text
        self.answer=answer


new_q=Question("what is name?","Mayank")
print(new_q.answer)