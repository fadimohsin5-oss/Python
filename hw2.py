
sample_notes = [
    "IMPORTANT: Complete Python homework\n",
    "TODO: Revise file handling concepts\n",
    "NOTE: read(n) previews characters\n",
    "IMPORTANT: Submit assignment today\n",
    "SKIP: This line is not needed\n",
    "NOTE: readlines() stores lines in a list\n",
    "TODO: Practise loops with files\n"
]

file = open("class-notes.txt", "w")
file.writelines(sample_notes)
file.close()


print("\nPART 1")

file = open("class-notes.txt", "r")
print(file.read(40))
file.close()


print("\nPART 2")

file = open("class-notes.txt", "r")
lines = file.readlines()
file.close()

print("Total lines in file:", len(lines))

for i in range(len(lines)):
    print(i + 1, "->", lines[i].strip())


print("\nPART 3")

file = open("class-notes.txt", "r")

for line in file:
    print("Reading:", line.strip())

file.close()


print("\nPART 4")

file = open("class-notes.txt", "r")
kept = 0
skipped = 0

for line in file:
    if line.startswith("SKIP"):
        print("Skipped:", line.strip())
        skipped = skipped + 1
    else:
        print("Kept:", line.strip())
        kept = kept + 1

file.close()

print("Kept:", kept)
print("Skipped:", skipped)

print("\nPART 5")

file = open("class-notes.txt", "r")
lines = file.readlines()
file.close()

output = open("organized-notes.txt", "w")
copied = 0

for line in lines:
    if line.startswith("IMPORTANT") or line.startswith("TODO"):
        output.write(line)
        copied = copied + 1

output.close()

print("Copied", copied, "lines")

print("\nPART 6")

file = open("organized-notes.txt", "r")

for line in file:
    print(line.strip())

file.close()
