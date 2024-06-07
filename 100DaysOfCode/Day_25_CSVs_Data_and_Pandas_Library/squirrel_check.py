# Count how many squirrels are based on fur color
import pandas

# Read data from a CSV file into a DataFrame
data = pandas.read_csv('Squirrel_Census_20240603.csv')
gray_ones_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_ones_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_ones_count = len(data[data['Primary Fur Color'] == 'Black'])
print(gray_ones_count)
print(red_ones_count)
print(black_ones_count)

data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray_ones_count, red_ones_count, black_ones_count]
}

print(data_dict)
