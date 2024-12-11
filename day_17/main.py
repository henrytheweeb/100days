from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank=[]
for question in question_data:
    question_bank.append(Question(text=question["text"],answer=question["answer"]))
quizzer=QuizBrain(question_bank)
while(quizzer.still_has_questions()):
    quizzer.next_question()
quizzer.finish    