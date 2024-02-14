import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    attempts = 0
    max_attempts = 10

    print("Welcome to the Guess the Number game!")
    print(f"I have selected a random number between 1 and 100. Can you guess it in {max_attempts} attempts?")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts!")
            break
        elif guess < secret_number:
            print("Too low. Try again!")
        else:
            print("Too high. Try again!")

    if attempts == max_attempts:
        print(f"Sorry, you have used all {max_attempts} attempts. The correct number was {secret_number}.")

if _name_ == "_main_":
    guess_the_number()
