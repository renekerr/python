# Count how many squirrels are based on fur color
import pandas

# Read data from a CSV file into a DataFrame
data = pandas.read_csv('Squirrel_Census_20240603.csv')

# Primary Fur Color
print(data['Primary Fur Color'])

gray = (data[data['Primary Fur Color'] == 'Gray'])
print(gray.count())