#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random
from replit import clear

lives_easy = 10
lives_hard = 5

#1
empty = []
for n in range(1,101):
    empty.append(n)

#Now we have a list with 100 numbers
#2
def random_number():
    """choice a random number in empty"""
    random_num = random.choice(empty)
    return random_num

us_number = random_number()

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {us_number}")
choose = input("Choose a difficulty. Type 'easy' or 'hard': ")

game_could_continue = True

while game_could_continue:
    if choose == "easy":
        print(f"You have {lives_easy} attemps remaining to guess the number")
        guess = int(input("Make a guess: "))
        if guess == us_number:
            print(f"You got it! The answer was {us_number}")
            game_could_continue = False

        elif guess < us_number:
            print("To low\nGuess again.")
            lives_easy -= 1
            

        elif guess > us_number:
            print("To high\nGuess again.")
            lives_easy -= 1
            

        if lives_easy == 0:
            print("You've run out of guesses, you lose.")
            game_could_continue = False

    if choose == "hard":
        print(f"You have {lives_hard} attemps remaining to guess the number")
        guess = int(input("Make a guess: "))
        if guess == us_number:
            print(f"You got it! The answer was {us_number}")
            game_could_continue = False

        elif guess < us_number:
            print("To low\nGuess again.")
            lives_hard -= 1
            

        elif guess > us_number:
            print("To high\nGuess again.")
            lives_hard -= 1
            

        if lives_hard == 0:
            print("You've run out of guesses, you lose.")
            game_could_continue = False    