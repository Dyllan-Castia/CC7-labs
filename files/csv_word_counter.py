"""
Write a program that first reads in the name of an input file and then reads 
the file using the csv.reader() method. The file contains a list of words separated by commas. 
The program must output the words and their frequencies (the number of times each word appears in the file) 
without any duplicates.
"""

import csv

filename = input()
f = open(filename)
reader = csv.reader(f)

words = []

for row in reader:
    for word in row:
        words.append(word)

counts = {}

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

for word in counts:
    print(f"{word} - {counts[word]}")

f.close
