highway_number = int(input())

if (highway_number % 2 == 0):
    is_east_west = True
else:
    is_east_west = False

if highway_number >= 99:
    is_primary = False
else:
    is_primary = True

if ((is_primary == False) and (highway_number // 100 > 0)):
    is_valid == False
    print(f"{highway_number} is not a valid interstate highway number.") 

if (is_primary == True) and (is_east_west == True):
    print(f"{highway_number}")
