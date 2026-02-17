input_month = input()
input_day = int(input())
""" Type your code here. """

if ((input_month == "March" and input_day >= 20) or 
     input_month in ["April", "May"] or 
     (input_month == "June" and input_day <= 20)):
    print("Spring")
elif ((input_month == "June" and input_day >= 21) or 
       input_month in ["July", "August"] or 
       (input_month == "September" and input_day <= 21)):
    print("Summer")
elif ((input_month == "September" and 22 <= input_day <= 30) or 
       input_month in ["October", "November"] or 
       (input_day == "December" and input_day <= 20)):
    print("Autumn")
elif ((input_month == "December" and input_day >= 21) or 
       (input_month in ["January", "February"] and (0 < input_day <= 31)) or (input_month == "March" and input_day <= 21)):
    print("Winter")
else:
    print("Invalid")
