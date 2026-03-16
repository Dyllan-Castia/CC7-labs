# User inputs string w/ numbers: '203 12 5 800 -10'
user_input = input("Enter numbers: ")

tokens = user_input.split()  # Split into separate strings

# Convert strings to integers
print()
nums = []
for pos, token in enumerate(tokens):
    nums.append(int(token))
    print(f"{pos}: {token}")

sum = 0
for num in nums:
    sum += num
    if num > 21:
        print(num)

# FIXME: Modify the print statement below to print sum and average.
print(f"Sum: {sum}")
print(f"Average: {sum / len(nums)}")
