import pandas as pd

file_name = input()

# TODO: Read in file_name as a dataframe
df = pd.read_csv(file_name, sep='\t')
# TODO: Output rows by descending Final scores
print(df.sort_values(by='Final', ascending=False).to_string())

print("\nMax Scores:")

# TODO: Output the max scores of each assignment
print(df.max(numeric_only=True).to_string())

print("\nMedian Scores:")

# TODO: Output the median scores of each assignment
print(df.median(numeric_only=True).to_string())

print("\nAverage Scores:")

# TODO: Output the average scores of each assignment.
print(df.mean(numeric_only=True).to_string())

print("\nStandard Deviation:")

# TODO: Output the standard devation of each assignment.
print(df.std(numeric_only=True).to_string())
