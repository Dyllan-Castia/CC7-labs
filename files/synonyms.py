"""
Given a set of text files containing synonyms for different words, complete the main 
program to output the synonyms for a specific word. Each text file contains synonyms 
for the word specified in the file's name, and each row within the file lists the word's 
synonyms that begin with the same letter, separated by a space. The program reads a word and a 
letter from the user and opens the text file associated with the input word. The program then stores 
the contents of the text file into a dictionary predefined in the program. Finally the program searches 
the dictionary and outputs all the synonyms that begin with the input letter, one synonym per line, or a message 
if no synonyms that begin with the input letter are found.

Hints: Use the first letter of a synonym as the key when storing the synonym into the dictionary. 
Assume all letters are in lowercase.
"""

synonyms = {}   # Define dictionary

word = input()
letter = input()

filename = word + ".txt"

f = open(filename)
lines = f.readlines()
f.close()

for line in lines:
    words = line.strip().split()
    for w in words:
        first_letter = w[0]
        
        if first_letter in synonyms:
            synonyms[first_letter].append(w)
        else:
            synonyms[first_letter] = [w]

if letter in synonyms:
    for w in synonyms[letter]:
        print(w)
else:
    print(f"No synonyms for {word} begin with {letter}.")
