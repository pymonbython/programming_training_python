""" Program gra "Quiz". Zadaniem użytkownika jest odpowiedzień na 3 pytnia.
"""

print('Witaj w grze. Masz \'3 pytania\' do skarbu.')
print('Aby zdobyć skarb (beczka rumu) musisz odpowiedzieć na 3. pytnia.')

# Dane (Krotka, sekwencja)
QUESTIONS = (
    ('Ile dni ma rok 2025?', '365'),
    ('Kto jest najważniejszy na statku?', 'Chief officer'),
    ('Co przychodzi po nocy?', 'Dzień')
)

SUCCESS_MESSAGE = 'Brawo, Twoja odpowiedź jest prawidłowa.'
FAILURE_MESSAGE = 'Zła odpowiedź.'

# Logika
def play_game(succes_msg: str, failure_msg: str, questions) -> None:
    """Ask user with specific questions and check if the user answer is correct or not.

    Args:
        succes_msg (str): Message after correct user answer.
        failure_msg (str): Message after incorrect user answer.
    """
    for question in questions:
        user_answer = input(question[0] + ": ")

        if question[1] == user_answer:
            print(succes_msg)
        else:
            print(failure_msg)
            return question
        
    return 'Brawo! Wygrałeś całą grę.'

end_code = play_game(SUCCESS_MESSAGE, FAILURE_MESSAGE, QUESTIONS)
print(end_code)
