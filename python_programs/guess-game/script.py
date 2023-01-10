# guess game program

import random

print("Hello, What's your name ?")
name = input()

print("Well, " + name + ", I am thinking of a number between 1 to 20")
secret_num = random.randint(1, 20)

for guess_count in range(1, 7):
    print("Take a guess")
    guess = int(input())

    if guess < secret_num:
        print("Your guess is low")
    elif guess > secret_num:
        print("Your guess is high")
    else:
        break #this condition is for the correct guess

if guess == secret_num:
    print("Good job " + name + " You guessed my number in " + str(guess_count) + " guesses")    
else:
    print("Nope, the number I was thinking of was " + str(secret_num))