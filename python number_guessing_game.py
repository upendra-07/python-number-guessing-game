
import random

while True:

    secret_number = random.randint(1, 100)

    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:

        guess = input("Guess a number between 1 and 100: ")

        if not guess.isdigit():
            print("Please enter a valid number!")
            continue

        guess = int(guess)

        if guess < 1 or guess > 100:
            print("Enter a number between 1 and 100!")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try higher.")

        elif guess > secret_number:
            print("Too high! Try lower.")

        else:
            print("Congratulations! You won!")
            break

    if attempts == max_attempts and guess != secret_number:
        print("Game over! The number was:", secret_number)

    play_again = input("Do you want to play again? (yes/no): ")

    if play_again.lower() != "yes":
        print("Thanks for playing!")
        break
