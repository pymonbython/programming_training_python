import json

with open('szymon.json') as file:
    data = json.load(file)

print(type(data), data)

print(data[0])



