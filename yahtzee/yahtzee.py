def read_input(in_str=None):
    category_list = """Выберите категорию и введите расклад через пробел (пример: 'pa 2 4 2 5 5'):
on - Ones
tw- Twos
th- Threes 
fo- Fours
fi- Fives
si- Sixes
pa- Pair
tp- Two pairs
tk- Three of a kind
fk- Four of a kind 
ss- Small straight 
ls- Large straight 
fh- Full house
ya- Yahtzee
ch - Chance
""" 
    if in_str is None:
        print(category_list)
        in_str = input()
    in_str = in_str.split()    
    category = in_str[0]
    roll = [int(x) for x in in_str[1:]]
    return category, roll

def analyze_roll(roll):
    dices = dict()
    for dice in roll:
        dices[dice] = dices.get(dice, 0) + 1
    combo = dict()
    for key, value in dices.items():
        combo[value] = combo.get(value, set())
        combo[value].add(key)
    inc_combo = set()
    for key in range(5, 0, -1):
        if key in combo:
            inc_combo = inc_combo | combo[key]
        if inc_combo:    
            combo[key] = inc_combo
    return combo, dices


def calculate_score(category, roll):
    small_straight = {1,2,3,4,5}
    large_straight = {2,3,4,5,6}
    combo, dices = analyze_roll(roll)
    if category == 'on' and 1 in dices:
        return dices[1]
    if category == 'tw' and 2 in dices:
        return 2*dices[2]
    if category == 'th' and 3 in dices :
        return 3*dices[3]
    if category == 'fo' and 4 in dices :
        return 4*dices[4]
    if category == 'fi' and 5 in dices :
        return 5*dices[5]
    if category == 'si' and 6 in dices :
        return 5*dices[6]
    if category == 'pa' and 2 in combo:
        return 2*max(combo[2])
    if category == 'th' and 3 in combo:
        return 3*max(combo[3])
    if category == 'fk' and 4 in combo:
        return 4*max(combo[4])
    if category == 'ya' and 5 in combo:
        return 5*max(combo[5])
    if category == 'ch':
        return sum(roll)
    if category == 'ss' and set(roll)&small_straight == small_straight:
        return 15
    if category == 'ls' and set(roll)&large_straight == large_straight:
        return 20
    if category == 'tp' and 2 in combo and len(combo[2])>= 2:
        return 2 * (max(combo[2]) + min(combo[2]))
    return 0

    

if __name__ == '__main__':
    category, roll = read_input()
    calculate_score(category, roll)