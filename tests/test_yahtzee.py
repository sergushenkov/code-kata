from yahtzee.yahtzee import read_input, analyze_roll, calculate_score

def test_read_input():
    in_str = 'on 2 4 2 5 5'
    rez = read_input(in_str)
    assert rez == ('on', [2, 4, 2, 5, 5])

def test_analyze_roll():
    combo, dices = analyze_roll([2, 4, 2, 5, 5])
    assert combo == {2: {2, 5}, 1: {2, 4, 5}}
    assert dices == {2: 2, 4: 1, 5: 2}

def test_analyze_roll_ya():
    combo, dices = analyze_roll([5, 5, 5, 5, 5])
    assert combo == {5: {5}, 4: {5}, 3: {5}, 2: {5}, 1: {5}}
    assert dices == {5: 5}

def test_calculate_score_on():
    params = ('on', [1, 1, 2, 5, 5])
    rez = calculate_score(*params)
    assert rez == 2

def test_calculate_score_tw():
    params = ('tw', [2, 5, 2, 5, 5])
    rez = calculate_score(*params)
    assert rez == 4

def test_calculate_score_tw_0():
    params = ('tw', [3, 3, 4, 5, 6])
    rez = calculate_score(*params)
    assert rez == 0

def test_calculate_score_th():
    params = ('th', [3, 3, 2, 5, 3])
    rez = calculate_score(*params)
    assert rez == 9

def test_calculate_score_ya():
    params = ('ya', [5, 5, 5, 5, 5])
    rez = calculate_score(*params)
    assert rez == 25

def test_calculate_score_ch():
    params = ('ch', [2, 4, 2, 5, 5])
    rez = calculate_score(*params)
    assert rez == 18

def test_calculate_score_ss():
    params = ('ss', [1, 2, 4, 3, 5])
    rez = calculate_score(*params)
    assert rez == 15

def test_calculate_score_ls():
    params = ('ls', [2, 4, 3, 6, 5])
    rez = calculate_score(*params)
    assert rez == 20

def test_calculate_score_tp():
    params = ('tp', [2, 4, 2, 5, 5])
    rez = calculate_score(*params)
    assert rez == 14


def test_calculate_score_pa_fh():
    params = ('pa', [2, 5, 2, 5, 5])
    rez = calculate_score(*params)
    assert rez == 10