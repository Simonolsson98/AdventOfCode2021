
input = open("day4_input.txt")
lines = []
i = input.readline()

bingonums = i.split(",")
# remove newline
bingonums[-1] = bingonums[-1][:2]

input.readline()
i = input.readline()

while(i):
	subrows = []
	for _ in range(5):
		num = i[:-1].split(" ")
		while(num.count("") > 0):
			num.remove("")
		subrows.append(num)
		i = input.readline()
	lines.append(subrows)
	i = input.readline()

while(lines.count([]) > 0):
	lines.remove([])

columns = []
for i in range(0, len(lines)):
	subcols = []
	for j in range(5):
		subcols.append([lines[i][k][j] for k in range(5)])
	[lines[i].append(subcols[i]) for i in range(5)]

drawn_numbers = []
win_index = -1

def find_winning_board():
	global win_index
	for i in range(len(bingonums)):
		drawn_numbers.append(bingonums[i])
		for j in range(len(lines)):
			for k in range(len(lines[j])):
				if(all(x in drawn_numbers for x in lines[j][k])):
					win_index = j
					return

find_winning_board()

for i in range(len(lines[win_index])):
	for j in range(len(drawn_numbers)):
		if(lines[win_index][i].count(drawn_numbers[j]) > 0):
			lines[win_index][i].remove(drawn_numbers[j])

unmarked_nums = set()
for i in range(len(lines[win_index])):
	for j in range(len(lines[win_index][i])):
		unmarked_nums.add(int(lines[win_index][i][j]))

print("solution of part 1 is: " + str(sum(unmarked_nums) * int(drawn_numbers[-1])))
