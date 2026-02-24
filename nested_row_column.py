num_rows = int(input())
num_columns = int(input())

for row in range(num_rows):
    letter = chr(ord("A") + row)
    for col in range(1, num_columns + 1):
        print(f"{letter}{col}", end=" ")
    print()  
#input:
    #3
    #5
    
#Output:
#A1 A2 A3 A4 A5 
#B1 B2 B3 B4 B5 
#C1 C2 C3 C4 C5 
