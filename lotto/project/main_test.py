from main import draw_numbers

def test_draw_numbers():
    # given

    # when
    for _ in range(501):
        ai_numbers = sorted(list(draw_numbers()))

        # than

        assert len(ai_numbers) == 6
        # @TODO Zakres od 1 do 49

        assert ai_numbers[0] >= 1
        assert ai_numbers[-1] <= 49

