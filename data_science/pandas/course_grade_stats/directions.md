Given the file name of a .tsv file read from user input containing student names and the respective course assignment grades, complete a program that performs the following tasks:

Read the input file as a pandas dataframe.
Output the students' names and grades in descending order of Finals scores.
Output each assignment's max score.
Output the median and average of each assignment's scores.
Output the standard deviation of each assignment's scores.
NOTES:

Steps 3 through 5 should only require one function for each step. Ex. Finding the max of each assignment uses max()
Append .to_string() to the end of the function call in order to silence an extraneous line that occurs at the end of the output.
For steps 3, 4, and 5, the functions used will require the parameter numeric_only=True to be passed to specify that only numbers will be calculated (as the input file contains strings for student names).


Input and Output Example
Ex: If the input of the program is:
StudentInfo.tsv
The output is:

      Lname   Fname  Midterm1  Midterm2  Final
1  Bradshaw  Reagan        96        97     88
2  Charlton   Caius        73        94     80
0   Barrett    Edan        70        45     59
4     Stern  Brenda        90        86     45
3      Mayo  Tyrese        88        61     36

Max Scores:
Midterm1    96
Midterm2    97
Final       88

Median Scores:
Midterm1    88.0
Midterm2    86.0
Final       59.0

Average Scores:
Midterm1    83.4
Midterm2    76.6
Final       61.6

Standard Deviation:
Midterm1    11.304866
Midterm2    22.634045
Final       22.210358
