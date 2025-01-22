# 1)
# x, y = z (12)
# 6, 4 = 10


# 2)
# 6, 4, 8 = 18
# x, y, x (8) = 20


# 3)
# pass
# pass

my_list = [1, 2, 3]

new_list = []

for element in my_list:
    new_element = element*2
    new_list.append(new_element)

# List comprehension
new_list_2 = [element *2 for element in my_list]

print(new_list)
print(new_list_2)
