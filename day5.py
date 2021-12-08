def init():
	input = open("day5_input.txt")
	lines = []
	i = input.readline()

	while(i):
		lines.append(i)
		i = input.readline()

	return lines




lines = init()

grid = [["."] * 990] * 990

# unmarked nums * last drawn number
#print("solution of part 1 is: " + str(sum(unmarked_nums) * int(drawn_numbers[-1])))

for i in range(len(lines)):
	first_and_second = lines[i].split(" -> ")
	first_and_second[1] = first_and_second[1][:-1]

	print(first_and_second)
	x_start = int(first_and_second[0].split(",")[0])
	x_end = int(first_and_second[1].split(",")[0])
	y_start = int(first_and_second[0].split(",")[1])
	y_end = int(first_and_second[1].split(",")[1])
	if(x_start == x_end or y_start == y_end):
		for j in range(min(x_start, x_end), max(x_start, x_end) + 1):
			for k in range(min(y_start, y_end), max(y_start, y_end) + 1):
				if(grid[j][k] == "."):
					grid[j][k] = 1
				elif(grid[j][k] == 1):
					grid[j][k] = 2

sum = 0
for i in range(len(grid)):
	sum += grid[i].count(2)

print(sum)
#print(lines)
#print("solution of part 2 is: " + str(sum(unmarked_nums) * int(drawn_numbers[-1])))