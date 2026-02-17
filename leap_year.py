input_year = int(input())

if input_year % 400 == 0:
    result = f"{input_year} - leap year";
elif input_year % 100 == 0:
    result = f"{input_year} - not a leap year";
elif input_year % 4 == 0:
    result = f"{input_year} - leap year";
else:
    result = f"{input_year} - not a leap year";

print(result)
