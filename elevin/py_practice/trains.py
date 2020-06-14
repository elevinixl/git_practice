def trainNav(train):
    currentLocation = len(train)//2
    while True:
        print('You are in the ' + train[currentLocation][0])
        move = input('Where would you like to go? [f]orwards, [b]ackwards, [j]ump off')
        # INSERT logic for each of these options.

trainNav([['engine','The engine is hot, help the engineer shovel some coal into the boiler!'],
       ['First class car','Look at all the fancy people!'],
       ['Passenger car','You should find your seat.'],
       ['caboose','Everything is red!']])