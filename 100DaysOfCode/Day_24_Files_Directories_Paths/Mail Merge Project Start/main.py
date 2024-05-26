# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".


PLACEHOLDER = '[name]'

# Read the list of names from the input file
with open('./Input/Names/invited_names.txt') as names_file:
    invited_names = names_file.readlines()  # saves it as list item.

# Read the letter template content
with open('Input/Letters/starting_letter.txt') as letter_template_file:
    letter_template = letter_template_file.read()

# Create a personalized letter for each invited name
for name in invited_names:
    cleaned_name = name.strip()  # removes any leading, and trailing whitespaces
    personalized_letter = letter_template.replace(PLACEHOLDER, cleaned_name)

    # Write the personalized letter to a new file
    with open(f'./Output/ReadyToSend/letter_for_{cleaned_name}.txt', mode='w') as output_letter_file:
        output_letter_file.write(personalized_letter)
