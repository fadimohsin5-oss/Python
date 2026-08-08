def menu():
    print("************************************************")
    print("\t\t\tSMARTPHONE DIRECTORY", flush=False)
    print("\tYou can now perform the following operations on this phonebook\n")
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit phonebook")
    choice = int(input("Please enter your choice"))

def add_contact(pb):
    dip = []
    for i in range (len(pb[0])):
        if i == 0:
            dip.append(str(input("Enter name : ")))
        if i == 1:
            dip.append(str(input("Enter number : ")))
        if i == 2:
            dip.append(str(input("Enter e-mail : ")))
        if i == 3:
            dip.append(str(input("Enter dob(dd/mm/yy) : ")))
        if i == 4:
            dip.append(str(input("Enter category(Family/Friends/Work/Other): ")))
    pb.append(dip)
    return pb

def remove_existing(pb):
    query = str(input("Please enter the name you wish to remove."))
    temp = 0
    for i in range(len(pb)):
        if query == pb[i][0]:
            temp += 1
            print(pb.pop(i))
            print("This query has now been removed.")
            return pb

    if temp == 0:
        print("Contact not found. Recheck.")
        return pb

def delete_all(pb):
    return pb.clear()
       
def search_existing(pb):
    choice = int(input("Enter search criteria \n\n\n 1. Name\n2. Number\n3. E-mail\n4. DOB\n5. Category (Family/Friends/Work/Other) \nPlease enter:"))
    temp = []
    check = -1
    if choice ==1:
        query = str(input("Please enter the name of the contact you wish to search: "))
        for i in range (len(pb)):
            if query == pb[i][0]:
                check = i
                temp.append(pb[i])

    elif choice ==2:
            query = str(input("Please enter the number of the contact you wish to search: "))
            for i in range (len(pb)):
                if query == pb[i][1]:
                    check = i
                    temp.append(pb[i])

    elif choice ==3:
            query = str(input("Please enter the email of the contact you wish to search: "))
            for i in range (len(pb)):
                if query == pb[i][2]:
                    check = i
                    temp.append(pb[i])

    elif choice ==4:
            query = str(input("Please enter the DOB of the contact you wish to search: "))
            for i in range (len(pb)):
                if query == pb[i][3]:
                    check = i
                    temp.append(pb[i])

    elif choice ==5:
            query = str(input("Please enter the category of the contact you wish to search: "))
            for i in range (len(pb)):
                if query == pb[i][4]:
                    check = i
                    temp.append(pb[i])

    else:
        print("invalid search criteria")
        return -1