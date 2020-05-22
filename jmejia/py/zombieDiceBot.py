import zombiedice, random

'''
class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll()  # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll results information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        # 'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #           ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll()  # roll again
            else:
                break
'''

# Randomly take 2 rolls
'''
class MyZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        if diceRollResults is not None:
            if random.randint(0,1):
                diceRollResults = zombiedice.roll()
'''

# Stop after 2 brains
'''
class MyZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains < 2:
                diceRollResults = zombiedice.roll()
            else:
                break
'''

# Stop after 2 shotguns.
'''
class MyZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        brains = 0
        shotguns = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotguns += diceRollResults['shotgun']
            if shotguns < 2:
                diceRollResults = zombiedice.roll()
            else:
                break
'''

# Commit to 1-4 rolls, but bail if too many shotguns.
'''
class MyZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        plan = random.randint(0,3)
        brains = 0
        shotguns = 0
        while diceRollResults is not None and plan > 0:
            brains += diceRollResults['brains']
            shotguns += diceRollResults['shotgun']
            if shotguns < 2:
                diceRollResults = zombiedice.roll()
                plan -= 1
            else:
                break
'''

# Stop after more shotguns than brains.
'''
class MyZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        brains = 0
        shotguns = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotguns += diceRollResults['shotgun']
            if shotguns <= brains:
                diceRollResults = zombiedice.roll()
            else:
                break
'''

# Try to be savvy.
# Update: Savvy failed.  Just try to be slightly more opportunistic than Stop At 2 Bot.
class MyZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        brains = 0
        shotguns = 0
        '''weights = {'red': 0.5, 'yellow': 0.667, 'green': 0.833}
        count = {'red': 3, 'yellow': 4, 'green': 6}'''
        while diceRollResults is not None:
            '''reroll = {'red': 0, 'yellow': 0, 'green': 0}'''
            brains += diceRollResults['brains']
            shotguns += diceRollResults['shotgun']
            '''for color,result in diceRollResults['rolls']:
                count[color] -= 1
                if result == 'footsteps':
                    reroll[color] += 1'''
            '''avgWeight = 0
            for color in count:
                avgWeight += weights[color] * count[color]
            avgWeight /= sum(count.values())'''
            '''for i in range(sum(reroll.values()),3):
                reroll.append(avgWeight)'''  # this is borked at this point.  ignore
            if brains == 0 or shotguns < 2:
                diceRollResults = zombiedice.roll()
                '''elif ((shotguns + 1) * 0.14) < product(reroll):
                diceRollResults = zombiedice.roll()'''  # broken ATM.  ignore
                '''elif shotguns == 1:
                if reroll['green'] > 1:
                    diceRollResults = zombiedice.roll()
                elif reroll['red'] < 3 and brains < 2:
                    diceRollResults = zombiedice.roll()
                elif count['green'] > count['yellow'] and brains < 3:
                    diceRollResults = zombiedice.roll()
                else:
                    break'''
                '''elif shotguns == 2 and reroll['green'] == 3 and brains < 2:
                diceRollResults = zombiedice.roll()'''
            else:
                break

def product(list):
    total = 1
    for x in list:
        total *= x
    return total


zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotguns', minShotguns=1),
    MyZombie(name='My Zombie Bot'),
    # Add any other zombie players here.
)


# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=10000)
#zombiedice.runWebGui(zombies=zombies, numGames=1000)