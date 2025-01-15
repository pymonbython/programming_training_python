my_set = set()

my_list = [1, 2, 3]

# {}

set2 = {1, 2, 3, 4}

print(my_set)
print(type(my_set))

print(set2)

# print(set2[0])

print(my_list[0])

new_list = [1, 3, 2]

new_set = {1, 3, 2, 4}

if my_list == new_list:
    print(f'Obie listy posiadają identyczne wartości.')
else:
    print('not ok')

if set2 == new_set:
    print('ok set')
else:
    print('not ok set')
