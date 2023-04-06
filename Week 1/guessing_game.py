import random

random_num = random.randint(1, 100)
lives = 10

print(random_num) 

user_guess = int(input(f"You have {lives} lives remaining, please enter a number from 1 to 100: "))
while True:
    if user_guess < random_num:
        print("Guess is too low")
        lives -=1
        print(f"You have {lives} live(s) remaining.")
        user_guess = int(input("Please enter another number: "))

    elif user_guess > random_num:
        print("Guess is too high")
        lives -=1
        print(f"You have {lives} live(s) remaining.")
        user_guess = int(input("Please enter another number: "))

    else:
        print(f"You got it! with {lives} lives remaining!")
        break

    if lives == 11:
        print(f"Game over! the number was {random_num}.")
        break
