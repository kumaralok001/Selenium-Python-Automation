file = open('test.txt')
#Read all the contents of file
#read n number of characters by passing parameter

# print(file.read(5))

#read one single line at a time readline()
# print(file.readline())
# print(file.readline())



#-----print line by line using readLine method

# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

for line in file.readlines():
    print(line)

file.close()