import numpy as np

TEST_NUM = 10000  # К-сть випадкових випробувань...


def krap_play(n_dice, win_values, lose_values, lose_values_repeat, bet):
    dices = np.random.randint(1, 7, n_dice)
    value = np.sum(dices)
    if value in win_values:
        return 2 * bet
    elif value in lose_values:
        return 0
    else:
        our_value = value
    while True:
        dices = np.random.randint(1, 7, n_dice)
        value = np.sum(dices)
        if value == our_value and value == 6 or value == 8:
            return 2 * bet
        elif value == our_value and value == 4 or value == 10:
            return 3 * bet
        elif value == our_value and value == 5 or value == 9:
            return (3/2) * bet + bet
        elif value in lose_values_repeat:
            return 0


def krap_win(n_dice, win_values, lose_values, lose_values_repeat, bet):
    rez = np.zeros(TEST_NUM)
    for i in range(TEST_NUM):
        rez[i] = krap_play(n_dice, win_values, lose_values, lose_values_repeat, bet)
    return f"Кількість виграних грошей в середньому: ${(np.sum(rez) / TEST_NUM) - bet}"


if __name__ == '__main__':
    p = krap_win(2, (7, 11), (2, 3, 12), (7, ), 1)
    print(p)


