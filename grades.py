assignment1 = float(input("Enter score on assignment 1 (out of 50): "))
assignment2 = float(input("Enter score on assignment 2 (out of 50): "))
assignment3 = float(input("Enter score on assignment 3 (out of 50): "))
assignment4 = float(input("Enter score on assignment 4 (out of 50): "))
as1_score = assignment1 / 50
as2_score = assignment2 / 50
as3_score = assignment3 / 50
as4_acore = assignment4 / 50
as_overall_score = ((as1_score + as2_score + as3_score + as4_acore) / 4) * 100
print("Assignments 1-4 overall grade:")
print(as_overall_score)
assignments_grade_percentage = as_overall_score * .40

exam1_grade = float(input("Enter score on Exam 1 (out of 100): "))
exam2_grade = float(input("Enter score on Exam 2 (out of 100): "))
exam3_grade = float(input("Enter score on Exam 3 (out of 100): "))

overall_grade_exams = (exam1_grade + exam2_grade + exam3_grade) / 3
exam_grade_percentage = overall_grade_exams * .60
overall_grade = assignments_grade_percentage + exam_grade_percentage

print(f"Your overall grade is: {overall_grade}")
