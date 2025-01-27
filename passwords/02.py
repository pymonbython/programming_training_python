print(any([True, False, False]))

print(any([True, False, True]))

print(any([False, False, False]))

print(any([True, True, True]))

print('\n')

print(all([True, False, False]))

print(all([True, False, True]))

print(all([False, False, False]))

print(all([True, True, True]))

print('\n')

output = []

for x in [1, 2, 3, 4, 5, 6, 7, -4]:
    output.append(x > 0)

output2 = [x > 0 for x in [1, 2, 3, 4, 5, 6, 7, -4]]

print(all(output))

print(output2)
