from time import perf_counter
import random

def waiting_game():
    time = random.randint(2,5)
    print(f'TARGET TO {time} SECOND')

    input('Press a key to begin')
    start = perf_counter()

    input('Press again to stop')
    stop = perf_counter()-start

    if stop < time:
        print('you are so fast')
    elif stop > time:
        print('you are so slow')
    else:
        print('You are perfect!')
    print(f'your time is {stop}')

waiting_game()