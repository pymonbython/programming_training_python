class Question:
    def __init__(self, text: str, answers: list, right_answer: str) -> None:
        self.question = text
        self.answers = answers
        self.right_answer = right_answer

    def __str__(self) -> str:
        return self.question

    def check_answer(self, user_answer):
        return user_answer == self.right_answer


# Typ danych charakteryzuje się daną strukturą przekazanych wartości.

question = Question('Co jest stolicą Polski?', [
    'Warszawa',
    'Kraków'
], 'Warszawa')

print(type(question))
print(question)
print(question.question)
print(question.answers)
print(question.right_answer)

if question.check_answer(input(question.question + ": ")):
    print('Correct')
