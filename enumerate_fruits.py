num_salads = int(input())
ingredient_lists = []
for row_index in range(num_salads):
    ingredient_lists.append(input().split())

for index, row in enumerate(ingredient_lists):
    print(f"Fruit used in salad {index + 1}:")
    
    for ingredient in row:
        print(ingredient, end=" ")
    print()
