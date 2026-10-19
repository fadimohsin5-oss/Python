
import sys

# MY SMARTPHONE DIRECTORY / SLAM BOOK

def initial_slambook():
    return [["Name", "Phone", "Email", "DOB", "Category"]]


def menu():
    print("\n========== SLAM BOOK MENU ==========")
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Search for a friend")
    print("4. Exit phonebook")

    choice = input("Enter your choice (1-4): ")
    return choice


def add_contact(pb):
    print("\n--- ADD A NEW FRIEND ---")

    name = input("Enter name: ")
    number = input("Enter phone number: ")
    email = input("Enter e-mail address: ")
    dob = input("Enter date of birth (dd/mm/yy): ")
    category = input(
        "Enter category (Family/Friends/Work/Others): "
    )

    contact = [name, number, email, dob, category]
    pb.append(contact)

    print("\nFriend added successfully!")
    return pb


def view_contacts(pb):
    print("\n========== ALL CONTACTS ==========")

    if len(pb) == 1:
        print("No friends added yet!")
    else:
        for i in range(1, len(pb)):
            print("\nFriend", i)
            print("Name:", pb[i][0])
            print("Phone:", pb[i][1])
            print("Email:", pb[i][2])
            print("Birthday:", pb[i][3])
            print("Category:", pb[i][4])


def search_contact(pb):
    name = input("\nEnter friend's name to search: ")
    found = False

    for i in range(1, len(pb)):
        if pb[i][0].lower() == name.lower():
            print("\nFriend found!")
            print("Name:", pb[i][0])
            print("Phone:", pb[i][1])
            print("Email:", pb[i][2])
            print("Birthday:", pb[i][3])
            print("Category:", pb[i][4])
            found = True

    if not found:
        print("Friend not found!")


def thanks():
    print("\n************************************")
    print("Thank you for using our Slam Book!")
    print("Please visit again!")
    print("************************************")
    sys.exit("Goodbye! Have a nice day!")


# MAIN PROGRAM

print("====================================")
print("       SMARTPHONE DIRECTORY")
print("====================================")
print("Hello dear friends!")
print("Welcome to our Slam Book!")
print("Save your friends' details here.")

pb = initial_slambook()

while True:
    ch = menu()

    if ch == "1":
        pb = add_contact(pb)

    elif ch == "2":
        view_contacts(pb)

    elif ch == "3":
        search_contact(pb)

    elif ch == "4":
        thanks()

    else:
        print("Invalid choice! Please try again.")

