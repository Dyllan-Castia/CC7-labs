input_line = input()
while input_line != "exit":
	name, food = input_line.split() #Initialize 2 variables for 1 input line (2 entries sperated by spaces)
	order_records1[name] = food
	input_line = input()
