# file = open("my_file.txt")
# content = file.read()
# print(content)

# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)

# with open("my_file.txt", mode='a') as file:
#     file.write("\n New Text Line 4")

with open("next_text_file.txt", mode='w') as file:
    file.write("My New text file for testing w mode")