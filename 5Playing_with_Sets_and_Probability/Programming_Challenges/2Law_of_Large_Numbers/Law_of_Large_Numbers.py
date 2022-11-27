import random


def expectation(number):

    trial_list = []
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0

    for n in range(0, number):
        trial_list.append(random.randint(1, 6))

    for n in trial_list:
        if n == 1:
            ones += 1
        if n == 2:
            twos += 1
        if n == 3:
            threes += 1
        if n == 4:
            fours += 1
        if n == 5:
            fives += 1
        if n == 6:
            sixes += 1

    e = 1*(ones/len(trial_list)) + 2*(twos/len(trial_list)) + 3*(threes/len(trial_list)) + 4*(fours/len(trial_list)) + 5*(fives/len(trial_list)) + 6*(sixes/len(trial_list))
    
    print("Trials: {0} Trial average: {1:.2f}".format(number, e))


if __name__ == '__main__':
    e = 1*(1/6) + 2*(1/6) + 3*(1/6) + 4*(1/6) + 5*(1/6) + 6*(1/6)
    print("Expected value: ", e)
    expectation(100)
    expectation(1000)
    expectation(10000)
    expectation(100000)
    expectation(500000)