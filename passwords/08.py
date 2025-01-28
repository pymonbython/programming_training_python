from functools import cache


@cache
def tell_me_something(word):
    print(f'Przetwarzam słowo {word}')
    vowels = [letter for letter in word if letter in 'aeiouy']


    return {
        'len': len(word),
        'vowels': len(vowels)
    }


tell_me_something.cache_clear()

print(tell_me_something('abrakadabra'))
print(tell_me_something('kukuryku'))
print(tell_me_something('abrakadabra'))
