# Day 26 - Working with List & Dictionary Comprehensions

# Example 1: Using a for loop to increment each number in a list by 1
numbers = [1, 2, 3, 4]
incremented_numbers = []
for number in numbers:
    number += 1
    incremented_numbers.append(number)
print("Original numbers:", numbers)
print("Incremented numbers list:", incremented_numbers)

# Example 2: Using list comprehension to increment each number in a list by 10
ages = [20, 30, 40, 50]
incremented_ages = [age + 10 for age in ages]
print("\nOriginal ages:", ages)
print("Incremented ages list:", incremented_ages)

# Example 3: Using list comprehension to convert each letter in a name to uppercase
name = 'Rene'
uppercase_letters = [letter.upper() for letter in name]
print("\nUppercase letters in name:", uppercase_letters)

# Example 4: Using list comprehension to create a list of multiples of 10
multiples_of_ten = [number * 10 for number in range(1, 5)]
print("Multiples of 10:", multiples_of_ten)

# Conditional list comprehension
# Example 5: Using list comprehension to find unregistered servers
existing_servers = ['server01', 'server02', 'server03', 'server04']
active_directory_ou_servers = ['server01', 'server02', 'server03', 'server04', 'server05', 'server06', 'server07']
unregistered_servers = [item.upper() for item in active_directory_ou_servers if item not in existing_servers]
print("\nUnregistered servers:", unregistered_servers)

# Some more examples
# ---------------------

# Example 6: Squaring each number in a list
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n * n for n in numbers]  # Create a new list with the square of each number
print(squared_numbers)

# Example 7: Filtering even numbers from a list of strings after converting them to integers
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(x) for x in list_of_strings]  # Convert each string in the list to an integer
even_numbers = [num for num in numbers if (num % 2) == 0]  # Create a new list with only even numbers
print(even_numbers)

# Example 8
print('\nFinding common numbers in two files using list comprehension')
with open('file1.txt') as file1:
    file1_lines = file1.readlines()  # Read lines from file1 and save them as a list
with open('file2.txt') as file2:
    file2_lines = file2.readlines()  # Read lines from file2 and save them as a list

file1_numbers = [int(line) for line in file1_lines]  # Convert each line from file1 to an integer
file2_numbers = [int(line) for line in file2_lines]  # Convert each line from file2 to an integer

print(f"file1.txt numbers: {file1_numbers}")
print(f"file2.txt numbers: {file2_numbers}")

common_numbers = [num for num in file1_numbers if num in file2_numbers]  # Find common numbers in both lists
print(f"Common numbers in both files: {common_numbers}")
