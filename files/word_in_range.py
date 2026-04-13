"""
Write a program that first reads in the name of an input file, followed by two strings 
representing the lower and upper bounds of a search range. The file should be read using 
the file.readlines() method. The input file contains a list of alphabetical, ten-letter strings, 
each on a separate line. Your program should determine if the strings from the list are within that range 
(inclusive of the bounds) and output the results.
"""
f = open(input())
lines = f.readlines()
lower = input()
upper = input()

for line in lines:
    word = line.strip()
    if lower <= word <= upper:
        print(f"{word} - in range") 
    else:
        print(f"{word} - not in range")

f.close()
