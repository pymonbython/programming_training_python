import json

json_string = '''
{
  "consumption": 9.6,
  "drive": {"type": "permanent",
  "type_2": "4x4"},
  "marka": "Honda",
  "model": "CR-V",
  "gas": true
}
'''

with open('json.json') as file:
    car_data = json.load(file)

print(type(car_data))
print(car_data)

json_dict = json.loads(json_string)
# print(json_dict)
