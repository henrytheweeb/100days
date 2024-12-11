class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.score=0
        self.questions_list=q_list
        
    def next_question(self):
        user_answer=input(f"Q.{self.question_number+1}: {self.questions_list[self.question_number].text} (True/False)?: ")
        if self.check_answer(user_answer,self.questions_list[self.question_number].answer):
            print("Correct!")
            self.score+=1
        else:
            print(f"Incorrect ;-; The correct answer was {self.questions_list[self.question_number].answer}")
        self.question_number+=1
        print(f"Your current score is {self.score}/{self.question_number} ({float(self.score)/self.question_number*100:.2f}%)")
    def check_answer(self,user_ans,quiz_ans):
        return user_ans.lower()==quiz_ans.lower()
    def still_has_questions(self):
        return self.question_number<len(self.questions_list)
    def finish(self):
        print("You have finished the quiz!")
        print(f"Your final score was {self.score}/{self.question_number} ({float(self.score)/self.question_number*100:.2f}%)")