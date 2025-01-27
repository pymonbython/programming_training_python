from requests import get

url = 'http://api.datamuse.com/words?rel_rhy={}'

word = input('Jakie rymu będziemy szukali? ')


with get(url.format(word)) as res:
    for word in res.json():
        print(word.get('word', ''))
        break
