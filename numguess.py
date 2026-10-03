import random

attempts_list = []

def show_score():
    if not attempts_list:
        print("There is currently no high score.")
    else:
        print("The current high score is {} attempts".format(min(attempts_list)))

def start_game():
    print("Hey there! Welcome to the guessing game!")

    player_name = input("Enter your name: ")
    wanna_play = input("Hi, {}, would you like to play the guessing game? (Enter Yes/No): ".format(player_name)).strip().lower()

    while wanna_play == "yes":
        random_number = random.randint(1, 10)
        attempts = 0
        show_score()

        while True:
            try:
                guess = int(input("Pick a number from 1-10: "))
                if guess < 1 or guess > 10:
                    raise ValueError("Please guess a number within the given range")
            except ValueError as err:
                print("That's not a valid number. Try again.")
                print("({})".format(err))
                continue

            attempts += 1

            if guess == random_number:
                print("Congrats! You guessed it right!")
                print("It took you {} attempts".format(attempts))
                attempts_list.append(attempts)
                show_score()
                break
            elif guess < random_number:
                print("It's higher")
            else:
                print("It's lower")

        play_again = input("Would you like to play again? (Enter Yes/No): ").strip().lower()
        if play_again == "no":
            print("That's fine, have a nice day!")
            break
        wanna_play = play_again

    else:
        print("That's fine, have a nice day!")

if __name__ == '__main__':
    start_game()
                
            
    