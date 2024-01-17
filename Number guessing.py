import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Set the range for the random number (1 to 100 in this case)
    min_number = 1
    max_number = 100
    secret_number = random.randint(min_number, max_number)
    
    attempts = 0
    max_attempts = 10
    
    print(f"I have chosen a number between {min_number} and {max_number}. Can you guess it?")
    
    while attempts < max_attempts:
        guess = int(input("Your guess: "))
        
        if guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts + 1} attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")
        
        attempts += 1

    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()
