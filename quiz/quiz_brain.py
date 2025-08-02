class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        question = self.question_list[self.question_number].text
        self.question_number +=1
        u_answer = input(f"Q.{self.question_number}: {question} (True/False)?")
        self.check_asnwer(u_answer, question)

    def check_asnwer(self,u_answer, correct_answer):
        if u_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That´s worng.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
