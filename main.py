from art import logo
import random

numbers = list(range(1, 101))

chosen_number = random.choice(numbers)
print(logo)
print("Welcome to Guess The Number!\nI'm thinking of a number between 1 and 100")
# print(f"Chosen number is {chosen_number}")


def difficulty():
    """ Easy has 10 ,hard has 5 attempts."""
    level_of_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level_of_difficulty == "easy":
        return 10
    elif level_of_difficulty == "hard":
        return 5
    else:
        print("You didn't choose a difficulty.")
        return difficulty()


def remaining_attempt():
    return f"Guess again.\nYou have {attempt} attempts remaining to guess the number."


attempt = difficulty()
while attempt != 0:
    guess = int(input("Make a guess: "))
    if guess < chosen_number:
        print("It's higher!")
        attempt -= 1
        print(remaining_attempt())
    elif guess > chosen_number:
        attempt -= 1
        print("It's lower!")
        print(remaining_attempt())
    else:
        print(f"You got it! The answer was {chosen_number}.")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again == "y":
            chosen_number = random.choice(numbers)
            attempt = difficulty()
        else:
            break
    if attempt == 0:
        print(f"You've run out of guesses.\nThe answer was {chosen_number}\nYOU LOSE!")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again == "y":
            chosen_number = random.choice(numbers)
            attempt = difficulty()
        else:
            break


