'''
Roll a die until the total score is 20
'''
import random

target_score = 20


def toss():
    return random.randint(0, 1)


if __name__ == '__main__':

    amount = int(input('Enter your starting amount: '))
    num_toss = 0

    while amount > 0:
        result = toss()
        if result == 1:
            amount += 1
            print('Heads! Current amount: {0}'.format(amount))
        else:
            amount -= 1.50
            print('Tails! Current amount: {0}'.format(amount))

        num_toss += 1

    print('Game over: ( Current amount: {0}. Coin tosses: {1})'.format(amount, num_toss))
