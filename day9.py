def init():
	input = open("day9_input.txt")
	lines = []
	while(i := input.readline()):
		i = i.rstrip("\n")
		lines.append(i)

	return lines

lines = init()

low_points = []

def less_than(entry, y):
	return entry < y

indices = []
for i in range(len(lines)):
	for j in range(len(lines[i])):
		entry = lines[i][j]
		nums_to_check = []
		if(i > 0):
			nums_to_check.append(lines[i - 1][j])
		if(i < len(lines) - 1):
			nums_to_check.append(lines[i + 1][j])
		if(j > 0):
			nums_to_check.append(lines[i][j - 1])
		if(j < len(lines[i]) - 1):
			nums_to_check.append(lines[i][j + 1])
	
		if(all(map(lambda x: less_than(entry, x), nums_to_check))):
			low_points.append(int(entry) + 1)
			indices.append((i, j))

print("solution of part 1 is: " + str(sum(low_points)))

# basins should include low_points, 
# this works since len(indices) == len(low_points)
basins = [[indices[i]] for i in range(len(low_points))]

def recurse_foo(k, i, j):
	entry = int(lines[i][j])
	if(i > 0):
		num = int(lines[i - 1][j])
		if(num > entry and num < 9 and basins[k].count((i - 1, j)) == 0):
			basins[k].append((i - 1, j))
			recurse_foo(k, i - 1, j)
	if(i < len(lines) - 1):
		num = int(lines[i + 1][j])
		if(num > entry and num < 9 and basins[k].count((i + 1, j)) == 0):
			basins[k].append((i + 1, j))
			recurse_foo(k, i + 1, j)
	if(j > 0):
		num = int(lines[i][j - 1])
		if(num > entry and num < 9 and basins[k].count((i, j - 1)) == 0):
			basins[k].append((i, j - 1))
			recurse_foo(k, i, j - 1)
	if(j < len(lines[i]) - 1):
		num = int(lines[i][j + 1])
		if(num > entry and num < 9 and basins[k].count((i, j + 1)) == 0):
			basins[k].append((i, j + 1))
			recurse_foo(k, i, j + 1)

for k in range(len(indices)):
	recurse_foo(k, indices[k][0], indices[k][1])

for i in range(len(basins)):
	basins[i] = len(basins[i])

result = 1
for i in range(3):
	result *= max(basins)
	basins.remove(max(basins))

print("solution of part 2 is: " + str(result))	