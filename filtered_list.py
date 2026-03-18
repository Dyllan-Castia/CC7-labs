data_list = [int(x) for x in input().split()]

filtered_list = [x for x in data_list if x <= 24]

print(f"All numbers: {data_list}")
print(f"Numbers less than or equal to 24: {filtered_list}")
