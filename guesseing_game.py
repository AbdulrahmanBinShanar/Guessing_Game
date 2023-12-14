import random

def number_guessing_game():
    target_number = random.randint(1, 100)
    
    attempts_left = 3
    
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Try to guess it.")

    while attempts_left > 0:
        user_guess = int(input("Enter your guess: "))

        if user_guess == target_number:
            print(f"Congratulations! You guessed the correct number: {target_number}")
            break
        elif user_guess > target_number:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")
        
        attempts_left -= 1
        print(f"Attempts left: {attempts_left}")

    print(f"The correct number was: {target_number}.")

number_guessing_game()