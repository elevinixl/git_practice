def collatz(number):
    return (3 * number + 1) if (number % 2) else (number // 2)

while True:
    try:
        print('Enter number: ', end='')
        startingValue = int(input())
        break
    except ValueError:
        print('That\'s not a number...  Let\'s try again.')

print('Alright, starting with ' + str(startingValue) + '...')

sequenceValue = startingValue
while sequenceValue != 1:
    print(str(sequenceValue))
    sequenceValue = collatz(sequenceValue)
print(str(sequenceValue))

print('Phew, done!')
