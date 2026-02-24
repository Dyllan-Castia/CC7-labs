num_rows = int(input())
num_columns = int(input())

for row in range(num_rows):
    letter = chr(ord("A") + row)
    for col in range(1, num_columns + 1):
        print(f"{letter}{col}", end=" ")
    print()  
