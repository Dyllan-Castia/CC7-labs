grid_size = int(input())

grid_2d = []
for j in range(grid_size):
    row = []
    for k in range(grid_size):
        row.append(" ")
    grid_2d.append(row)

for j in range(grid_size):
    for k in range(grid_size):
        if (j + k) % 2 == 1:
            grid_2d[j][k] = "X"
            

for row in grid_2d:
    for cell in row:
        print(cell, end="")
    print()
