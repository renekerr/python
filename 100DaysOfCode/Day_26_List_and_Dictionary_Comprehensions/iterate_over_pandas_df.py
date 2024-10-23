import pandas

students_score = {
    "student": ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    "score": [90, 67, 88, 100, 99]
}

print('-Looping through dictionaries')
for (key, value) in students_score.items():
    print(key, value)

print('\n-Generating a pandas dataframe')
students_score_dataframe = pandas.DataFrame(students_score)
print(students_score_dataframe)

print('\n-Looping through a dataframe')
for (key, value) in students_score_dataframe.items():
    print(key)

print('\n-Looping through a dataframe using built-in function')
for (index, row) in students_score_dataframe.iterrows():
    if row.score >= 90:
        print(row.student)  # Students with score higher than or equal to 90
