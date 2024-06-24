# Working with Pandas library

import pandas

# Read data from a CSV file into a DataFrame
data = pandas.read_csv('weather_data.csv')
print('- Data read from csv')
print(data, '\n')

# Check the type of data
print('- Data type:')
print(type(data), '\n')

# Print the 'temp' column
print('- Print the "temp" column:')
print(data['temp'], '\n')

# Convert DataFrame to a dictionary
print('- Convert DataFrame to a dictionary:')
data_dict = data.to_dict()
print(data_dict, '\n')

# Convert the 'temp' column to a list
print('- Convert the "temp" column to a list:')
temp_list = data['temp'].to_list()
print(temp_list, '\n')

# Calculate the average temperature
print('- Calculate the average temperature:')
average_temp = sum(temp_list) / len(temp_list)
print(f'Average temperature : {average_temp:.2F}')

# Calculate the average temperature using the mean() method
print('- Calculate the average temperature using the mean() method:')
print(f'Average temperature : {data["temp"].mean():.2F} [pandas method]')
# +info: https://pandas.pydata.org/docs/reference/api/pandas.Series.mean.html#pandas.Series.mean

# Find the maximum temperature
print('- Find the maximum temperature:')
print(f'Maximum temperature : {data["temp"].max()}', '\n')

# Get data in a column using dictionary-like notation
print('- Get data in a column using dictionary-like notation:')
print(data['day'], '\n')

# Get data in a column using attribute-like notation
print('- Get data in a column using attribute-like notation:')
print(data.day, '\n')

# Get data for a specific day (e.g., Tuesday)
print('- Get data for a specific day (e.g., Tuesday):')
print(data[data.day == 'Tuesday'], '\n')

# Access data that fits a certain criteria (e.g., maximum temperature)
print('- Access data that fits a certain criteria (e.g., maximum temperature):')
print(data[data.temp == data.temp.max()], '\n')

# Get the condition for a specific day (e.g., Friday)
friday = data[data.day == 'Friday']
friday_temp = friday.temp[4]
print('- Get the condition for a specific day (e.g., Friday):')
print(friday.condition, '\n')  # Sunny

# Convert Friday's temperature to Fahrenheit
fahrenheit = ((friday_temp * 9) / 5) + 32
print('- Convert Friday\'s temperature to Fahrenheit:')
print(f'Friday temperature (Fahrenheit): {fahrenheit}', '\n')  # 69.8

# Create a DataFrame from scratch
countries_and_capitals = {
    'country': [
        "United States",
        "Canada",
        "United Kingdom",
        "France",
        "Germany",
        "Italy",
        "Spain",
        "Australia",
        "Japan",
        "India"
    ],
    'capital': [
        "Washington, D.C.",
        "Ottawa",
        "London",
        "Paris",
        "Berlin",
        "Rome",
        "Madrid",
        "Canberra",
        "Tokyo",
        "New Delhi"
    ]
}

data = pandas.DataFrame(countries_and_capitals)
print('- Create a DataFrame from scratch:')
print(data)

# Save data to csv file
data.to_csv('countries_capitals.csv')
