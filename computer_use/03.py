a, b, c, d = (1, 2, 3, 4)


my_cars = [
  {
    "consumption": 9.6,
    "drive": {
      "is_4x4": True,
      "type": "permanent"
    },
    "manufacture": "Honda",
    "model": "CR-V",
    "gas": True,
    "year": 2006,
    "is_lift": True
  },
  {
    "consumption": 4.4,
    "drive": {
      "is_4x4": False,
      "type": None
    },
    "manufacture": "Skoda",
    "model": "Fabia",
    "gas": True,
    "year": 2004,
    "is_lift": False
  }
]

# print(a, b, c, d)

def foo(a, b, c, d):
    print(a, b, c, d)


sample_data = [1, 2, 3, 4]
*a, = sample_data
*a, = my_cars
sample_var = {"1": 1}.values()
sample_var2 = {"1": 1}
print(*list(sample_var))
print(*sample_var)
# print(*my_cars)
# print(type(**sample_var2))
# print(**sample_var2)
# print(**sample_var2)
# print(a)