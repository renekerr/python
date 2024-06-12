# Import the pandas library for data manipulation and analysis
import pandas

# Read data from a CSV file into a DataFrame
data = pandas.read_csv('Squirrel_Census_20240603.csv')

# Count the number of squirrels with gray fur
gray_ones_count = len(data[data['Primary Fur Color'] == 'Gray'])

# Count the number of squirrels with cinnamon (red) fur
red_ones_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])

# Count the number of squirrels with black fur
black_ones_count = len(data[data['Primary Fur Color'] == 'Black'])

# Print the counts of each fur color
print(gray_ones_count)
print(red_ones_count)
print(black_ones_count)

# Create a dictionary with fur color and their corresponding counts
data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray_ones_count, red_ones_count, black_ones_count]
}

# Convert the dictionary to a DataFrame
df = pandas.DataFrame(data_dict)

# Print the DataFrame
print(df)

# Save the DataFrame to a new CSV file
df.to_csv('squirrel_count.csv')
