from main import sum_numbers

#  1. test case
def test_sum_numbers():
    score = sum_numbers(2, 2)

    assert score == 4


def test_sum_diff_numbers():
    score = sum_numbers(2, 3)

    assert score == 5

    