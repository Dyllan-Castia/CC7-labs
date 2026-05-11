# TODO: Import NumPy
import numpy as np

file_name = input()

# TODO: Load student scores from file_name into a NumPy array
scores = np.loadtxt(file_name, dtype=int)
# TODO: Calculate the median and average of student scores
median_score = np.median(scores)
average_score = np.mean(scores)
# TODO: Curve student scores
curve_amount = 100 - np.max(scores)
curved_scores = scores + curve_amount
# TODO: Output the median, average, and curved scores
print(f"Median = {median_score:.2f}")
print(f"Average = {average_score:.2f}")
print(f"Curved scores = {curved_scores}")
