
def init():
	input = open("day11_input.txt")
	lines = []
	while(i := input.readline()):
		i = i.rstrip("\n")
		lines.append(i)

	return lines

lines = init()

