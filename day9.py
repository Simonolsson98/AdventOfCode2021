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
	
		[low_points.append(int(entry) + 1) for entry in entry if(all(map(lambda x: less_than(entry, x), nums_to_check)))]

print("solution of part 1 is: " + str(sum(low_points)))