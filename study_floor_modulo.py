#Use % to get the desired rightmost digits. 
#Ex: The rightmost 2 digits of 572 is gotten by 572 % 100, which is 72.

#Use // to shift right by the desired amount.
#Ex: Shifting 572 right by 2 digits is done by 572 // 100, which yields 5.
#(Recall integer division discards the fraction).

phone_number = int(input()) #10 digits no parentheses or dashes (just numbers)
area_code = phone_number // 10000000 #gets rid of last 7 digits(amount of zeroes)
first6 = phone_number // 10000 #gets rid of last 4 digits and keeps the first 6
middle3 = first6 % 1000 #gets rid of first 3 digits and keeps the last 3 (or middle of phone_number)
last4 = phone_number % 10000 #gets rid of the first 6 digits and keeps the last 4
print(f"({area_code}) {middle3}-{last4}") #(nnn) nnn-nnnn
