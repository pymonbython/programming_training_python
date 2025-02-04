# x = 5
# print(id(x))
# x = 5

# print(x)

# print(id(x))

# x = (5, )
# print(id(x))
# x = (5, )

# print(x)

# print(id(x))

# x = [5]
# print(id(x))
# x = [5]

# print(x)

# print(id(x))

# x = 'Very complicated string !@#$% żćśłó ZAQ!2wx'
# y = x
# z = 'Very complicated string !@#$% żćśłó ZAQ!2wx'
# print(id(x))
# print(id(y))
# print(id(z))

# x = 'ahoj'
# xyz = x
# print(id(x))
# print(id(xyz))
# y = ' piraci'
# x = x + y
# print(x)
# print(xyz)

# print(id(x))
# print(id(xyz))

# x = 'ahoj'
# print(id(x))
# x = (x + ' piraci')[:-7]
# print(x)
# print(id(x))

# x = 5
# print(id(x))
# x = x * 1 + 1 - 1 + 256 - 256 + (456*7) - (456*7) + 80**7 - 80**7 + 900**9 - 900**9
# print(x)
# print(id(x))


x = 10

def foo():
    global x
    x = x + 1
    print(x)

foo()

print(x)

