
def addition(a, b):
    return a + b

def multiplication(a, b):
    return a * b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("1. Addition")
print("2. Multiplication")
choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    print("Sum =", addition(num1, num2))
elif choice == 2:
    print("Product =", multiplication(num1, num2))
else:
    print("Invalid choice")