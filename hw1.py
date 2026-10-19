
import os

with open("Sample_File.txt", "a") as file:
    file.write("\nHi! My name is Fahad.")
    file.write("\nI am learning Python.")

with open("Sample_File.txt", "r") as file:
    data = file.read()
    words = data.split()
    print("Words in the file:")
    print(words)

if os.path.exists("My_File.txt"):
    print("My_File exists")

else:
    with open("My_File.txt", "w") as file:
        file.write("Hi! My name is Fahad.")
        file.write("\nI am learning Python.")
    print("My_File created")

if os.path.exists("sample_doc.txt"):
    os.remove("sample_doc.txt")
    print("sample_doc deleted")
else:
    print("sample_doc does not exist")
