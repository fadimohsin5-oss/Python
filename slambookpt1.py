
import sys

def initial_slambook():
    rows = int(input("How many friends do you want to add? "))
    cols = 5

    slam_book = []

    for i in range(rows):
        print("\nEnter details for friend", i + 1)
        print("* indicates mandatory fields")
        print("--------------------------------")

        temp = []

        for j in range(cols):

            if j == 0:
                name = input("Enter name*: ")

                if name.strip() == "":
                    sys.exit("Name cannot be empty!")

                temp.append(name)

            elif j == 1:
                number = input("Enter number*: ")

                if number.strip() == "":
                    sys.exit("Phone number cannot be empty!")

                temp.append(number)

            elif j == 2:
                about = input("Something about your friend: ")

                if about.strip() == "":
                    about = None

                temp.append(about)

            elif j == 3:
                dob = input("Date of birth (dd/mm/yy): ")

                if dob.strip() == "":
                    dob = None

                temp.append(dob)

            elif j == 4:
                category = input(
                    "Category (Family/Friends/Work/Others): "
                )

                if category.strip() == "":
                    category = None

                temp.append(category)

        slam_book.append(temp)
        print("\nFriend added successfully!")

    return slam_book


def menu():
    print("\n*************************************")
    print("            MY SLAM BOOK")
    print("*************************************")
    print("1. View all friends")
    print("2. Exit")
    print("*************************************")

print("=====================================")
print("       WELCOME TO MY SLAM BOOK")
print("=====================================")

slam_book = initial_slambook()

while True:
    menu()

    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        print("\n======= MY FRIENDS =======")

        if len(slam_book) == 0:
            print("No friends added yet!")

        for i in range(len(slam_book)):
            print("\nFriend", i + 1)
            print("Name:", slam_book[i][0])
            print("Phone:", slam_book[i][1])
            print("About:", slam_book[i][2])
            print("Birthday:", slam_book[i][3])
            print("Category:", slam_book[i][4])

    elif choice == "2":
        print("\nThank you for using my Slam Book!")
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
