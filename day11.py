
def init():
	input = open("day11_input.txt")
	lines = []
	while(i := input.readline()):
		i = i.rstrip("\n")
		lines.append(i)

	return lines

lines = init()

lines = [list(x) for x in lines]

lines = [[int(x) for x in y] for y in lines]

count = 0
for _ in range(100):
	print(*lines)
	updated_lines = [[int(x) + 1 for x in y] for y in lines]
	step_done = False
	while(not step_done):
		flash_count = [[False for _ in lines] for _ in lines]
		step_done = True
		for i in range(len(lines)):
			for j in range(len(lines[i])):
				entry = lines[i][j]
				if(entry > 9 and flash_count[i][j] == False):
					flash_count[i][j] = True
					count += 1
					updated_lines[i][j] = 0
					if(i > 0 and j > 0 and flash_count[i - 1][j - 1] == False):
						updated_lines[i - 1][j - 1] = updated_lines[i - 1][j - 1] + 1
					if(i > 0 and flash_count[i - 1][j] == False):
						updated_lines[i - 1][j] = updated_lines[i - 1][j] + 1
					if(j > 0 and flash_count[i][j - 1] == False):
						updated_lines[i][j - 1] = updated_lines[i][j - 1] + 1
						
					if(i < len(lines) - 1 and j < len(lines[i]) - 1 and flash_count[i + 1][j + 1] == False):
						updated_lines[i + 1][j + 1] = updated_lines[i + 1][j + 1] + 1
					if(i < len(lines) - 1 and flash_count[i + 1][j] == False):
						updated_lines[i + 1][j] = updated_lines[i + 1][j] + 1
					if(j < len(lines[i]) - 1 and flash_count[i][j + 1] == False):
						updated_lines[i][j + 1] = updated_lines[i][j + 1] + 1
					if(i < len(lines) - 1 and j > 0 and flash_count[i + 1][j - 1] == False):
						updated_lines[i + 1][j - 1] = updated_lines[i + 1][j - 1] + 1
					if(j < len(lines) - 1 and i > 0 and flash_count[i - 1][j + 1] == False):
						updated_lines[i - 1][j + 1] = updated_lines[i - 1][j + 1] + 1
		lines = updated_lines[:]

		for x in updated_lines:
			for y in x:
				if(y > 9):
					step_done = False


print(count)