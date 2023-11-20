import random
print('Oi lad, what\'s ya name?')
name = input()
print('Roight, now I will think of a number and ya have ta guess wot it is, yeah?')
number = random.randint(1, 9)
print('Orite, come on then!')
for x in range(1, 7):
    print: ("Pick wisely!")
    try:
        guess = int(input())
    except ValueError:
        print("Give a number, laddie! Not a string!")
        continue
    if guess > number:
        print("Your guess is too high!")
    if guess < number:
        print("Your guess is too low!")
    else:
        break
if guess == number:
    print("You did it! You got the number!")
else:
    print("Better luck next time!")
