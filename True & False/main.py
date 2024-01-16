from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(q_list=question_bank)

while quiz.still_has_questions():
    quiz.next_question()
if not quiz.still_has_questions():
    print(f"You've completed the quiz.\n Your final score was {quiz.score}/{len(question_bank)}")
