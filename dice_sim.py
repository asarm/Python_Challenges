from random import randint
from collections import Counter

def roll_dice(*side,attemps_num):
    counts = Counter()
    for roll in range(attemps_num):
        counts[sum((randint(1, sides) for sides in side))] += 1

    print('\nOUTCOME\tPROBABILITY')
    for outcome in range(len(side), sum(side) + 1):
        print('{}\t{:0.2f}%'.format(outcome, counts[outcome] * 100 / attemps_num))


if __name__ == '__main__':
    attemp_num = int(input())
    roll_dice(4, 6, 6,attemps_num=attemp_num)
