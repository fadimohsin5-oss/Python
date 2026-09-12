file = open ('Codingal.txt')
print(file.read())
file.close()

file_write = open('Codingal.txt', 'w')
file_write.write("File in write mode...")
file_write.write("Hi! I am Penguin. I am 1 yr old")
file_write.close()

file_append = open('Codingal.txt', 'a')
file_append.write("\n File in append mode...")
file_append.write("Hi! I am Penguin. I am 1 yr old")
file_append.close()

