from string import ascii_lowercase
import json


class Question:
    def __init__(self, question_id: int,  text: str, answers: list, right_answer: str) -> None:
        self.question_id = question_id
        self.text = text
        self.answers = answers
        self.right_answer = right_answer

    def __str__(self):
        output = f'Pytanie {self.question_id}: {self.text}.\n'
        output += f'Możliwe odpowiedzi: \n'

        for letter, answer in zip(ascii_lowercase, self.answers):
            output += f'[{letter}] ' + answer + '\n'

        return output

    def check_answer(self, user_answer: str) -> bool:
        return user_answer == self.right_answer


class Quiz:
    def __init__(self, f_path: str) -> None:
        self.points = 0
        self.questions = self.load_questions(f_path)

    def load_questions(self, f_path: str) -> list:
        temp_list = []
        with open(f_path, 'r', encoding='utf-8') as f:
           questions = json.load(f)
           for question in questions:
               temp_list.append(Question(
                    question_id=question['id'],
                    text=question['question'],
                    answers=question['answers'],
                    right_answer=question['right_answer']
                ))
        
        return temp_list


    def play(self) -> int:
        for question in  self.questions:
            print('\n')
            print('--' * 20)
            print(question)
            your_answer = input('Którą odpowiedź wybierasz? [a-d]: ')

            self.points += 1 if your_answer == question.right_answer else 0

        
        print('\n')
        print('Koniec gry (Game Over)')
        print(f'Zdobywasz: {self.points}. punktów')
        print('\n')

        return self.points

# Polskie znaki OK => encoding=


name = input('Podaj swoje imię: ')

quiz = Quiz(
    f_path='questions.json'
)

points = quiz.play()


try:
    with open('results.json', encoding='utf-8') as f:
        results = json.load(f)

except FileNotFoundError:
    results = []


results.append({
    'name': name,
    'points': points
})

with open('results.json', 'w') as f:
    json.dump(results, f)
