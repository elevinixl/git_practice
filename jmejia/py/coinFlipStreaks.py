import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    flipSet = ''
    for i in range(100):
        flipSet += 'H' if random.randint(0,1) else 'T'

    # Code that checks if there is a streak or 6 heads or tails in a row.
    if ('HHHHHH' in flipSet) or ('TTTTTT' in flipSet):
        numberOfStreaks += 1
print('Chance of streak: %s%%' % (numberOfStreaks / 100))