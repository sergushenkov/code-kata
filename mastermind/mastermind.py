from random import randint


def make_number():
    rez = []
    for _ in range(4):
        x = randint(0, 9)
        rez.append(x)
    return rez


def compare_numbers(original_num, test_num):
    bulls = cows = 0
    for i in range(4):
        if original_num[i] == test_num[i]:
            bulls += 1
            original_num[i] = 10
            test_num[i] = -1
    for x in test_num:
        if x in original_num:
            cows += 1
            original_num.remove(x)
    return (bulls, cows)


if __name__ == "__main__":
    original_num = make_number()
    while True:
        player_str = input("Ваше число? ")
        test_num = list(map(int, player_str))
        bulls_num, cows_num = compare_numbers(original_num.copy(), test_num)
        bulls = ""
        if bulls_num == 4:
            print("4 быка - вы угадали число")
            break
        if bulls_num == 1:
            bulls = "1 бык "
        if bulls_num in (2, 3):
            bulls = "{bulls_num} быка ".format(bulls_num=bulls_num)
        cows = ""
        if cows_num == 1:
            cows = "1 корова"
        if cows_num > 1:
            cows = "{cows_num} коровы".format(cows_num=cows_num)
        print(bulls, cows, sep="")
