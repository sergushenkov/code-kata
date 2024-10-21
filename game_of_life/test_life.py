from life import Life


def test_set_starting_position():
    game = Life("life_start_test.txt")
    assert game.height == 3
    assert game.width == 2
    assert game.turn == 5
    assert game.grid == [[0, 1], [0, 0], [1, 1]]

    game = Life("life_start.txt")
    assert game.height == 4
    assert game.width == 8
    assert game.turn == 1
    assert game.grid == [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]


def test_show_generation():
    test_file = "life_start_test.txt"
    game = Life(test_file)
    rez = game.show_generation()
    goal = open(test_file).read()
    assert rez == goal

    test_file = "life_start.txt"
    game = Life(test_file)
    rez = game.show_generation()
    goal = open(test_file).read()
    assert rez == goal


def test_check_neighbor():
    game = Life("life_start_test.txt")
    check_points = (
        ((-1, -1), False),
        ((-1, 1), False),
        ((0, 3), False),
        ((2, -1), False),
        ((3, -1), False),
        ((3, 2), False),
        ((3, 1), False),
        ((0, 0), True),
        ((1, 0), True),
        ((0, 2), False),
        ((1, 2), False),
        ((1, -1), False),
        ((1, 4), False),
    )
    for xy, rez in check_points:
        assert game.check_neighbor(xy) == rez


def test_count_alive_neighbors():
    game = Life("life_start_test.txt")
    check_points = (
        ((0, 0), 1),
        ((0, 1), 0),
        ((1, 0), 3),
        ((1, 1), 3),
        ((2, 0), 1),
        ((2, 1), 1),
    )
    for xy, rez in check_points:
        assert game.count_alive_neighbors(*xy) == rez


def test_next_generation():
    game = Life("life_start_test.txt")
    game.next_generation()
    assert game.turn == 6
    assert game.grid == [[0, 0], [1, 1], [0, 0]]
    game.next_generation()
    assert game.turn == 7
    assert game.grid == [[0, 0], [0, 0], [0, 0]]
