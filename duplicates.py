outputFile=open('UpdatedFile.txt', 'w')
inputFile=open('Codingal.txt', 'r')

lines_seem_so_far=set()
print("Eliminating duplicate lines...")
for line in inputFile:
    if line not in lines_seem_so_far:
        outputFile.write(line)
        lines_seem_so_far.add(line)
inputFile.close(
)
outputFile.close(
)