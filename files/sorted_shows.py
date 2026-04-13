"""
Write a program that first reads in the name of an input file and then reads the input file using 
the file.readlines() method. The input file contains an unsorted list of number of seasons followed 
by the corresponding TV show. Your program should put the contents of the input file into a dictionary where 
the number of seasons are the keys, and a Python list of TV shows are the values (since multiple shows could have 
the same number of seasons).

Sort the dictionary by key (greatest to least) and output the results to a file named output_keys.txt. 
Separate multiple TV shows associated with the same key with a semicolon (;), ordering by appearance in the input file. 
Next, sort the dictionary by values (in reverse alphabetical order), and output the results to a file named 
output_titles.txt.
"""

f = open(input())
lines = f.readlines()
f.close()

shows = {}

for i in range(0, len(lines), 2):
    seasons = int(lines[i].strip())
    show = lines[i + 1].strip()

    if seasons in shows:
        shows[seasons].append(show)
    else:
        shows[seasons] = [show]

write_file = open("output_keys.txt", "w")

for key in sorted(shows.keys(), reverse=True):
    shows_list = "; ".join(shows[key])
    write_file.write(f"{key}: {shows_list}\n")

write_file.close()

titles = []

for season_list in shows.values():
    for show in season_list:
        titles.append(show)

titles.sort(reverse=True)

write_file2 = open("output_titles.txt", "w")

for show in titles:
    write_file2.write(f"{show}\n")

write_file2.close()
