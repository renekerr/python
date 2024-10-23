import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
# Read the CSV file into a DataFrame
nato_data = pandas.read_csv('nato_phonetic_alphabet.csv')

# Create a dictionary from the DataFrame where the key is the letter and the value is the phonetic code
nato_phonetic_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
print(nato_phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# Get a word from the user and convert it to uppercase
user_word = input('Enter a word: ').upper()

# Create a list of phonetic code words corresponding to each letter in the user-provided word
phonetic_code_words = [nato_phonetic_dict[letter] for letter in user_word]
print(phonetic_code_words)
