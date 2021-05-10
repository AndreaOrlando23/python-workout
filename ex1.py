from random import randint


# Number guessing game
def guessing_game():
    answer = randint(0, 100)

    while True:
        user_input = input("Guess a number from 0 to 100 (blank to quit the game): ")

        if user_input == "":
            print("Thank you!")
            break

        if int(user_input) == answer:
            print("Just right! You Win!")
            break

        if int(user_input) < answer:
            print("Too low.. try again")
        else:
            print("Too high.. try again")


guessing_game()