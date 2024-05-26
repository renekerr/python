# Day 24 - Files, Directories and Paths

# Accessing, reading, printing the content of a text file and closing it.
# Option 1
# file = open('file.txt')
# content = file.read()
# print(content)
# file.close()

print('-' * 30)

# Option 2 (no need to use close())
with open('file.txt') as file:
    content = file.read()
    print(content)

"""
Example: 
Absolute path if file is located on Desktop 
    /Users/your_user/Desktop/file.txt

Relative path if file is located on Desktop
    ../../Desktop/file.txt
"""

print('-' * 30)

# Writing in an existing file
with open('file.txt', mode='a') as file:
    file.write('Cost an arm and a leg')

with open('file.txt') as file:
    content = file.read()
    print(content)

print('-' * 30)

# Creating and writing in a new file (using absolute path)
with open('/Users/rene/Desktop/file.txt', mode='w') as new_file:
    new_file.write('Beat around the bush')

# Reading from a file using relative path
with open('../../../../../Desktop/file.txt') as file:
    content = file.read()
    print(content)
