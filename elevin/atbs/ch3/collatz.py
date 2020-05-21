def collatz(num):
    if num % 2 == 0:
        print(num//2)
        return num//2
    else:
        print(3*num+1)
        return 3*num+1

print("Enter number")
try:
    number = int(input())
    while number != 1:
        number = collatz(number)
except ValueError:
    print('Input must be an integer.')