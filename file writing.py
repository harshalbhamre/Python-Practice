# f = open("harsh2.txt", "w")  #opens in write mode
# f.write("Yo Whatsup") # empties the content and adds the given content
# # if file doesn't exist it creates a new one
# f.close()

# f = open("harsh2.txt", "a") # opens in append mode and adds the characters to the existing file
# f.write(" Hi bhai")
# f.close()


#handle read and write both
f = open("harsh2.txt", "r+") #  r+ reads and writes both
print(f.read())
f.write("\n  kaise ho")
f.close()
