import random
import time


def welcome_message():
    """Displays a welcoming message with an Indian touch."""
    print("--------------------------------------------------")
    print("     नमस्ते! Welcome to the Odd/Even Guessing Game!     ")
    print("--------------------------------------------------")
    print("Get ready to test your luck and intuition!")
    print("Let's see if you can outsmart the computer...")
    time.sleep(2)


def get_player_name():
    """Gets the player's name."""
    while True:
        name = input("Before we begin, what's your name, champion? ").strip()
        if name.replace(" ", "").isalpha():
            return name.title()
        else:
            print("Please enter a valid name (letters only).")


def get_player_choice():
    """Gets the player's choice of 'odd' or 'even'."""
    while True:
        choice = input("Will you choose ODD or EVEN? (Type 'odd' or 'even'): ").lower().strip()
        if choice in ['odd', 'even']:
            return choice
        else:
            print("Invalid choice. Please type 'odd' or 'even'.")


def get_player_number():
    """Gets the player's number (1-10)."""
    while True:
        try:
            num = int(input("Now, pick a number between 1 and 10: "))
            if 1 <= num <= 10:
                return num
            else:
                print("Your number must be between 1 and 10. Try again!")
        except ValueError:
            print("That's not a valid number. Please enter an integer.")


def determine_winner(player_choice, player_num, computer_num):
    """Determines the winner of the round."""
    total_sum = player_num + computer_num
    print(f"\nYour number: {player_num}")
    print(f"Computer's number: {computer_num}")
    print(f"The total sum is: {total_sum}")

    is_sum_even = (total_sum % 2 == 0)

    if (player_choice == 'even' and is_sum_even) or \
            (player_choice == 'odd' and not is_sum_even):
        print("🎉 Congratulations! You guessed it right!")
        return True
    else:
        print("Better luck next time! Your guess was incorrect.")
        return False


def play_game():
    """Main function to play the Odd/Even Guessing Game."""
    welcome_message()
    player_name = get_player_name()
    print(f"\nGreat to have you here, {player_name}!")
    time.sleep(1)

    player_score = 0
    computer_score = 0
    rounds_played = 0

    while True:
        rounds_played += 1
        print(f"\n--- Round {rounds_played} ---")

        player_choice = get_player_choice()
        player_num = get_player_number()

        # Computer generates its number and then 'makes' its choice based on what will give it a better chance
        # For simplicity, let's just make the computer's choice random for now.
        # A more complex AI could try to counter the player's choice.
        computer_num = random.randint(1, 10)
        computer_choice = random.choice(['odd', 'even'])  # This choice isn't directly used for winning logic

        print("\nDrumroll please...")
        time.sleep(1)
        print("Calculating results...")
        time.sleep(1.5)

        if determine_winner(player_choice, player_num, computer_num):
            player_score += 1
        else:
            computer_score += 1

        print(f"\n--- Current Score ---")
        print(f"{player_name}: {player_score} | Computer: {computer_score}")

        while True:
            play_again = input("\nWant to play another round? (yes/no): ").lower().strip()
            if play_again in ['yes', 'no']:
                break
            else:
                print("Please enter 'yes' or 'no'.")

        if play_again == 'no':
            break

    print("\n--------------------------------------------------")
    print("           Game Over!  धन्यवाद! (Thank you!)        ")
    print("--------------------------------------------------")
    if player_score > computer_score:
        print(f"🎉 Well done, {player_name}! You are the champion with {player_score} points!")
    elif computer_score > player_score:
        print(f"Hard luck, {player_name}. The computer won this time with {computer_score} points.")
    else:
        print("It's a tie! A truly balanced match!")
    print(f"Final Score: {player_name} - {player_score} | Computer - {computer_score}")
    print("Hope to see you again soon for another round of fun!")


if __name__ == "__main__":
    play_game()