def init(part):
	input = open("day5_input.txt")
	lines = []
	i = input.readline()

	condition = bool()
	while(i):
		i = i[:-1]
		first_and_second = i.split(" -> ")
		x_start = int(first_and_second[0].split(",")[0])
		x_end = int(first_and_second[1].split(",")[0])
		y_start = int(first_and_second[0].split(",")[1])
		y_end = int(first_and_second[1].split(",")[1])
		if(part == "1"):
			condition = (x_start == x_end or y_start == y_end)
		else:
			condition = (x_start == x_end or y_start == y_end or (x_start - x_end == y_start - y_end and x_start - y_start == x_end - y_end))
			
		if(condition):
			lines.append(i)		
		i = input.readline()

	return lines, x_start, x_end, y_start, y_end

lines, x_start, x_end, y_start, y_end = init("1")

grid = [["x" for _ in range(1000)] for y in range(1000)]

for i in range(len(lines)):
	first_and_second = lines[i].split(" -> ")
	x_start = int(first_and_second[0].split(",")[0])
	x_end = int(first_and_second[1].split(",")[0])
	y_start = int(first_and_second[0].split(",")[1])
	y_end = int(first_and_second[1].split(",")[1])
	for j in range(min(x_start, x_end), max(x_start, x_end) + 1):
		for k in range(min(y_start, y_end), max(y_start, y_end) + 1):
			if(grid[j][k] == "x"):
				grid[j][k] = 1
			elif(grid[j][k] == 1):
				grid[j][k] = 2
			else:
				pass

sum_of_covered = 0
for i in range(len(grid)):
	sum_of_covered += grid[i].count(2)

print("solution of part 1 is: " + str(sum_of_covered))


lines, x_start, x_end, y_start, y_end = init("2")

grid = [["x" for _ in range(1000)] for y in range(1000)]

for i in range(len(lines)):
	first_and_second = lines[i].split(" -> ")
	x_start = int(first_and_second[0].split(",")[0])
	x_end = int(first_and_second[1].split(",")[0])
	y_start = int(first_and_second[0].split(",")[1])
	y_end = int(first_and_second[1].split(",")[1])
	for j in range(min(x_start, x_end), max(x_start, x_end) + 1):
		for k in range(min(y_start, y_end), max(y_start, y_end) + 1):
			if(grid[j][k] == "x"):
				grid[j][k] = 1
			elif(grid[j][k] == 1):
				grid[j][k] = 2
			else:
				pass


sum_of_covered = 0
for i in range(len(grid)):
	sum_of_covered += grid[i].count(2)

#not 939711, should be less
print("solution of part 2 is: " + str(sum_of_covered))