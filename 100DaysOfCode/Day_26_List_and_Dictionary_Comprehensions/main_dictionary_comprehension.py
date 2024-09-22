# Day 26 - Working with List & Dictionary Comprehensions

import random

# DICTIONARY COMPREHENSION: EXAMPLES & HOW IT WORKS

# Example 1: Create a dictionary of student scores and filter those who passed
student_names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
print("Student's scores")
student_scores = {student: random.randint(60, 100) for student in student_names}
print(student_scores)

print('\nPassed students')
passed_students = {student: score for student, score in student_scores.items() if score >= 80}
print(passed_students)

# Example 2: Convert a sentence into a dictionary with words and their lengths
sentence_text = "What is the Airspeed Velocity of an Unladen Swallow?"
word_list = sentence_text.split()
word_length_dict = {word: len(word) for word in word_list}
print(f"\nSentence: {sentence_text}")
print('Words and its length')
print(word_length_dict)

# Example 3: Convert a dictionary of weather in Celsius to Fahrenheit
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day: (temp_celsius * 9/5) + 32 for (day, temp_celsius) in weather_c.items()}
print(f"\nWeather in Celsius:\n{weather_c}")
print(f"\nWeather in Fahrenheit:\n{weather_f}")
