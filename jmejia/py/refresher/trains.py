
train = [['engine room','The engine is hot, help the engineer shovel some coal into the boiler!'],
         ['First class car','Look at all the fancy people!'],
         ['Passenger car','You should find your seat.'],
         ['caboose','Everything is red!']]


dictHuh = { 0: "You're not making any sense...",
            1: "That's not a direction you can go.",
            2: "I don't understand.",
            3: "There's no door that way." }


loc = len(train) // 2

print("You're in the " + train[loc][0] + ".")
print(train[loc][1])
print()
while True :
   print("Where do you want to go?")
   action = input("[f]orwards, [b]ackwards, [j]ump off > ").lower()
   if action not in ('f','b','j') :
      print()
      print("You're not making any sense...")
      print()
      continue
   elif action == 'j' :
      print()
      print("Looks like this is your stop!  Remember to roll when you hit the ground!")
      break
   elif action == 'f' :
      loc -= 1
      if loc < 0 :
         print()
         print("Stepping in front of a moving train is a bad idea, even if you're on the train!  Luckily, the train had already pulled up to the station -- but you still feel embarrassed.")
         break
   elif action == 'b' :
      loc += 1
      if loc >= len(train) :
         print()
         print("Oddly, you just hover in the air when you step off the back of the caboose.  Convenient day for the gravity to be turned off.  But, oh no! -- all your stuff is still on the train!")
         break
   print()
   print("You're now in the " + train[loc][0] + ".")
   print(train[loc][1])
   print()
