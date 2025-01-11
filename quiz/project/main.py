from string import ascii_lowercase
import json


class Question:
    def __init__(self, question_id: int,  text: str, answers: list, right_answer: str) -> dict:
        self.question_id = question_id
        self.text = text
        self.answers = answers
        self.right_answer = right_answer

    def __str__(self):
        output = f'Pytanie: {self.text}.\n'
        output += f'Możliwe odpowiedzi: \n'

        for letter, answer in zip(ascii_lowercase, self.answers):
            output += f'[{letter}] ' + answer + '\n'

        return output

    def check_answer(self, user_answer: str) -> bool:
        return user_answer == self.right_answer


points = 0

# Polskie znaki OK => encoding=
with open('questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)
    for question in questions:
        print('\n')
        print('--' * 20)
        # print('Pytanie: ' + question['question'])
        # print('Odpowiedzi: ')

        # for letter, answer in zip(ascii_lowercase, question['answers']):
        #     print(f'[{letter}] ' + answer)

        question_obj = Question(
            question_id=question['id'],
            text=question['question'],
            answers=question['answers'],
            right_answer=question['right_answer']
        )

        print(question_obj)

        your_answer = input('Którą odpowiedź wybierasz? [a-d]: ')

        points += 1 if your_answer == question['right_answer'] else 0
        
        if your_answer not in ['a', 'b', 'c', 'd']:
            continue


print('\n')
print('Koniec gry (Game Over)')
print(f'Zdobywasz: {points}. punktów')
print('\n')

