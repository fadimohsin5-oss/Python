
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

print("================================")
print("      FIND THE VALUE")
print("================================")

print("Dictionary:", d)

key = int(input("Enter a key (1-6): "))

if key in d:
    print("The value of key", key, "is", d[key])
else:
    print("Sorry! This key does not exist in the dictionary.")

