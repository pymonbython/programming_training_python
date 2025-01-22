from random import shuffle

fruits = ['lemon', 'apple', 'orange', 'banana']

shuffle(fruits)

# Modyfikujemy listę, która była na początku
print('Potasowane')
print(fruits)
print('Posortowane')
# Zwraca posrtowaną listę, lecz nie robi tego "in place"
print(sorted(fruits))

print(fruits.sort())
print(fruits.pop(-1))


