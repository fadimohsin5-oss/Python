import random

def roll_dice():

    number = random.randint(1, 6)

    print("\nYou rolled a", number)

    dice_faces = {
        1: "⚀",
        2: "⚁",
        3: "⚂",
        4: "⚃",
        5: "⚄",
        6: "⚅"
    }

    print("Dice face:", dice_faces[number])


def main():
    print("Welcome to the Dice Rolling Simulator!")

    while True:
        choice = input("\nDo you want to roll the dice? (yes/no): ")
        
        if choice.lower() == "yes":
            roll_dice()
        elif choice.lower() == "no":
            print("Thanks for playing! Goodbye! 👋")
            break
        else:
            print("Please enter yes or no.")


main()