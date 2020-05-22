import random
import logging
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug('Start of program')


guess = ''
while guess.lower() not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    if guess.lower() not in ('tails', 'heads'):
        raise Exception('You must guess "heads" or "tails".')
    logging.debug('The user\'s guess is: ' + guess)
toss = random.randint(0, 1) # 0 is tails, 1 is heads
logging.debug('The toss is: ' + str(toss))

if guess.lower() == 'tails':
    guess = 0
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if guess.lower() not in ('tails', 'heads'):
        raise Exception('You must guess "heads" or "tails".')
    logging.debug('The user\'s guess is: ' + guess)
    if guess.lower() == 'heads':
        guess = 1
    if toss == guess:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

logging.debug('End of program')