def init():
	input = open("day8_input.txt")
	lines = []

	while(i := input.readline()):
		i = i.rstrip("\n").split(" | ")
		lines.append(i[1].split(" "))

	return lines

lines = init()

count = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        length_to_check = len(lines[i][j])
        if (length_to_check == 2 or length_to_check == 3 or length_to_check == 4 or length_to_check == 7):
            count += 1


print("solution of part 1 is: " + str(count))
