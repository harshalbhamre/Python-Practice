#File I/O Basics

"""
"r" = open file for reading - default mode
"w" = open a file for writing
"x" = creates file if not exist
"a" = add more content to a file at the end
"t" = text mode - default mode
"b" = binary mode
"+" = read and write the file

"""
# f = open("harsh.txt")
# content = f.read()
# print(content)
# f.close()

# f = open("harsh.txt", "rb")  #reads in binary
# content = f.read()
# print(content)
# f.close()

# f = open("harsh.txt", "rt")
# content = f.read(3)  # reads 3 character
# print(content)
# content = f.read(5) # prints next 5 character
# print("next 5 characters are : ", content)
# f.close()

# f = open("harsh.txt")
# content = f.read()
# print(content)
# for line in content:
#     print(line)  # prints everything character by charter
# f.close()

# f = open("harsh.txt")
# for line in f:
#     print(line, end="")  # prints everything as is
# f.close()

# f = open("harsh.txt")
# print(f.readline())  # prints first line
# print(f.readline())  #prints next line also prints a new line charcter
# f.close()

f = open("harsh.txt")
print(f.readlines())  #prints all lines in a list
f.close()
