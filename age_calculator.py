import math
user_age_years = int(input("Enter your age in years: "))

# Complete step 1 here
user_age_secs = user_age_years * 365 * 24 * 60 * 60
print(f"User's age in seconds: {user_age_secs:,}")
# Complete step 2 here
user_heart_beats = user_age_secs / 72
print(f"Estimated Heart Beats Total: {user_heart_beats:,}")
# Complete step 3 here
user_loosely_defined_calories_burned = user_age_years * 365 * 2100
print(f"Estimated Calories Burned: {user_loosely_defined_calories_burned:,}")
# Complete step 4 here
user_breaths_taken = user_age_secs / 60 * 16
print(f"Estimated Breaths Taken: {user_breaths_taken:,}")
# Complete step 5 here
print("What is the max amount of fucks you can give on a given day?:")
average_fucks_per_day = float(input())          # F_max
apathy_rate = 0.03

user_fucks_given = (average_fucks_per_day / apathy_rate) * (1 - math.exp(-apathy_rate * user_age_years)) * 365.25
print(f"Fucks Given: {user_fucks_given:,}")
