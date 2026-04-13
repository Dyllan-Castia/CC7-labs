"""
Write a program that reads the student information from a tab separated values (tsv) file. 
The program then creates a text file that records the course grades of the students. 
Each row of the tsv file contains the Last Name, First Name, Midterm1 score, Midterm2 score, 
and the Final score of a student. A sample of the student information is provided in StudentInfo.tsv. 
Assume the number of students is at least 1 and at most 20. Assume also the last names and first names 
do not contain whitespaces.

The program performs the following tasks:

Read the file name of the tsv file from the user.
Open the tsv file and read the student information.
Compute the average exam score of each student.
Assign a letter grade to each student based on the average exam score in the following scale:
A: 90 =< x
B: 80 =< x < 90
C: 70 =< x < 80
D: 60 =< x < 70
F: x < 60
Compute the average of each exam.
Output the last names, first names, exam scores, and letter grades of the students into a 
text file named report.txt. Output one student per row and separate the values with a tab character.

Output the average of each exam, with two digits after the decimal point, at the end of report.txt. 
Hint: Use the format specification to set the precision of the output.
"""

filename = input()

f = open(filename)
lines = f.readlines()
f.close()

students = []

midterm1_total = 0
midterm2_total = 0
final_total = 0

for line in lines:
    parts = line.strip().split('\t')
    
    last_name = parts[0]
    first_name = parts[1]
    midterm1 = int(parts[2])
    midterm2 = int(parts[3])
    final = int(parts[4])
    
    average = (midterm1 + midterm2 + final) / 3
    
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    students.append([last_name, first_name, midterm1, midterm2, final, grade])
    
    midterm1_total += midterm1
    midterm2_total += midterm2
    final_total += final

count = len(students)

midterm1_avg = midterm1_total / count
midterm2_avg = midterm2_total / count
final_avg = final_total / count

out_file = open('report.txt', 'w')

for student in students:
    out_file.write(f"{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}\t{student[4]}\t{student[5]}\n")

out_file.write(f"\nAverages: midterm1 {midterm1_avg:.2f}, midterm2 {midterm2_avg:.2f}, final {final_avg:.2f}\n")

out_file.close()
