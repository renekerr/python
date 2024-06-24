# Day 25 - Working with CSV Data and the Pandas Library

import csv


with open('weather_forecast/weather_data.csv') as data_file:
    data = csv.reader(data_file)
    print(data)  # this will print it as an object

    # Skip header
    next(data)

    temperature = []
    for row in data:
        temperature.append(int(row[1]))

print(temperature)

