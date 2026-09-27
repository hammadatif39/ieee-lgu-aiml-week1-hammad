import random

def get_valid_guess():
    # Loop until the user enters a valid number
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            
            # Checking if the number is within the correct range
            if 1 <= guess <= 100:
                return guess
            else:
                print("Out of bounds! Please enter a number between 1 and 100.")
        except ValueError:
            # This prevents the program from crashing if a letter is typed
            print("Invalid input! Please type a whole number.")

def play_round():
    # Pick a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 7
    
    print("\nI have picked a secret number between 1 and 100.")
    print(f"You have {attempts} attempts to guess it!")
    
    # Keep asking for guesses while the user has attempts
    while attempts > 0:
        guess = get_valid_guess()
        attempts -= 1
        
        if guess < secret_number:
            print(f"Too Low! Try a bigger number. (Attempts left: {attempts})")
        elif guess > secret_number:
            print(f"Too High! Try a smaller number. (Attempts left: {attempts})")
        else:
            print(f"Congratulations! You guessed the secret number {secret_number}!")
            return # Exit the function because the user won
            
    # If the loop finishes, the user ran out of attempts
    print(f"Game Over! You ran out of tries. The secret number was {secret_number}.")

def start_game():
    while True:
        play_round()
        
        # Ask to play again
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

# This line makes sure the game only runs when the script is executed directly
if __name__ == "__main__":
    start_game()