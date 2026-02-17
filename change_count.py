import sys

total_change = int(input())
if total_change == 0:
    print("No change")
    sys.exit()


dollars = total_change // 100
total_change %= 100

quarters = total_change // 25
total_change %= 25

dimes = total_change // 10
total_change %= 10

nickels = total_change // 5
total_change %= 5

pennies = total_change

if dollars > 1:
    bills = "Dollars"
elif dollars == 1:
    bills = "Dollar"
else:
    bills = 0

if quarters > 1:
    q = "Quarters"
elif quarters == 1:
    q = "Quarter"
else:
    q = 0

if dimes > 1:
    d = "Dimes"
elif dimes == 1:
    d = "Dime"
else:
    d = 0

if nickels > 1:
    n = "Nickels"
elif nickels == 1:
    n = "Nickel"
else:
    n = 0

if pennies > 1:
    p = "Pennies"
elif pennies == 1:
    p = "Penny"
else:
    p = 0

message = []

if bills != 0:
    message.append(f"{dollars} {bills}")

if q != 0:
    message.append(f"{quarters} {q}")

if d != 0:
    message.append(f"{dimes} {d}")

if n != 0:
    message.append(f"{nickels} {n}")

if p != 0:
    message.append(f"{pennies} {p}")

result = "\n".join(message)
print(result)
