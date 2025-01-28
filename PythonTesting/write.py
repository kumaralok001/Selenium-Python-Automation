# file = open('test.txt')
#
# file.close()

# optimize way to open file with closing it automatically
#read the file and store all the lines in list
#reverse the list
#write the list back to the file

# with open('test.txt', 'r') as reader:
#     content = reader.readlines() #[abc, boy, cat, dog, elephant, f]
#     reversed(content) #[f, elephant, dog, cat, boy, abc]
#     with open('test.txt', 'w') as writer:
#         for line in reversed(content):
#             writer.write(line)
















with open('test.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)

with open('test.txt', 'r') as reader:
    content = reader.readlines()
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)