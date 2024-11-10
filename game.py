import random

def rps():
    choices = ['rock', 'paper', 'scissors']
    user_wins = 0
    system_wins = 0
    ties = 0
    rounds = 3  # You can adjust this to make more rounds

    for _ in range(rounds):
        user = input("Enter rock, paper, or scissors: ").lower()
        while user not in choices:
            print("Invalid input. Please choose either 'rock', 'paper', or 'scissors'.")
            user = input("Enter rock, paper, or scissors: ").lower()

        system = random.choice(choices)
        print("System choice:", system)

        if user == system:
            ties += 1
            print("It's a tie!")
        elif (user == 'rock' and system == 'scissors') or \
             (user == 'paper' and system == 'rock') or \
             (user == 'scissors' and system == 'paper'):
            user_wins += 1
            print("You win this round!")
        else:
            system_wins += 1
            print("You lose this round!")

        print(f"Round result: {user} vs {system}")

    print("\nGame over!")
    print(f"Total wins: {user_wins}")
    print(f"Total losses: {system_wins}")
    print(f"Ties: {ties}")
    if user_wins > system_wins:
        print("Congratulations! You won the game!")
    elif user_wins < system_wins:
        print("Better luck next time! The system won.")
    else:
        print("It's a tie game overall!")

def guessing():
    number = random.randint(1, 50)
    attempts = 0
    print("\nGuess the number between 1 and 50!")

    guess = int(input("Enter your guess: "))
    attempts += 1

    while number != guess:
        if guess > number:
            print("Oops, too high! Try a lower number.")
        elif guess < number:
            print("Oops, too low! Try a higher number.")
        guess = int(input("Enter your guess: "))
        attempts += 1

    print(f"Correct guess! The number was {number}. You guessed it in {attempts} attempts.")

def main():
    print("Welcome to the Game World! Choose a game to play:")
    while True:
        game = input("Enter 'rps' for Rock-Paper-Scissors or 'guessing' for Guessing Game (or 'exit' to quit): ").lower()

        if game == 'rps':
            rps()
        elif game == 'guessing':
            guessing()
        elif game == 'exit':
            print("Thanks for playing! See you next time.")
            break
        else:
            print("Invalid choice! Please enter a valid game name (rps/guessing).")

# Run the main loop
if __name__ == "__main__":
    main()
