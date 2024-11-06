from game_of_life.life import Life


def test_count_living_nearby():
    game = Life()
    zero = game.count_living_nearby(0, 0)
    assert zero == 0

    zero = game.count_living_nearby(0, 7)
    assert zero == 0

    zero = game.count_living_nearby(3, 0)
    assert zero == 0

    zero = game.count_living_nearby(3, 7)
    assert zero == 0

    one = game.count_living_nearby(0, 4)
    assert one == 1

    two = game.count_living_nearby(2, 4)
    assert two == 2

    two = game.count_living_nearby(3, 3)
    assert two == 2
