
def addition(numbers):
    return sum(numbers)

def subtraction(numbers):
    answer = numbers[0]
    for n in numbers[1:]:
        answer = answer - n
    return answer

def multiplication(numbers):
    answer = 1
    for n in numbers:
        answer = answer * n
    return answer

def average(numbers):
    return sum(numbers) / len(numbers)


print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Average")

choice = int(input("Enter your choice (1-4): "))

numbers = []

while True:
    num = input("Enter a number or type done: ")

    if num == "done":
        break

    numbers.append(float(num))


if len(numbers) == 0:
    print("No numbers entered")

elif choice == 1:
    print("Sum =", addition(numbers))

elif choice == 2:
    print("Difference =", subtraction(numbers))

elif choice == 3:
    print("Product =", multiplication(numbers))

elif choice == 4:
    print("Average =", average(numbers))

else:
    print("Invalid choice")

print("Total numbers =", len(numbers))

