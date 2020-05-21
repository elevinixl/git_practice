import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    streakList = []
    for i in range(100):
        streakList.append(random.randint(0,1))
    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(len(streakList)-7):
        if sum(streakList[i:i+6]) == 6 or sum(streakList[i:i+6]) == 0:
            numberOfStreaks += 1
            break

print('Chance of streak: %s%%' % (numberOfStreaks / 100))