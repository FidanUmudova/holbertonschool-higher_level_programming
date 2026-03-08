#!/usr/bin/python3
word = "Holberton"
# get first 3 letters
word_first_3 = word[:3]
# get last 2 letters
word_last_2 = word[-2:]
# get middle of the word (without first and last letters)
middle_word = word[1:-1]
# print results
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
