

def to_negative(number):
    return number * -1


def change_to_negative(numbers):
    return list(map(to_negative, numbers))
    # new_list = []
    # for number in numbers:
    #     new_list.append(number * -1)

    # return new_list


def do_something(numbers: list, function):
    return function(numbers)

print(do_something([1, 2,3, 4, 6], sum))
print(do_something([1, 2,3, 4, 6], max))
print(do_something([1, 2,3, 4, 6], sorted))
print(do_something([1, 2, 3, 4, 5, 6], change_to_negative))
