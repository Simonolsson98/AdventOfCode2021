
input = open("day3_input.txt")
lines = []
i = input.readline()
while i:
	lines.append(i[:-1])
	i = input.readline()

gamma = ""
epsilon = ""
zeroes = 0
ones = 0
# loop over each column
for i in range(len(lines[0])):
	# loop over each row
	for j in range(len(lines)):
		if(lines[j][i] == "0"): 
			zeroes += 1
		else:
			ones += 1
	# find most and least common bit of index i
	if zeroes > ones:
		gamma += "0"
		epsilon += "1"
	else:
		gamma += "1"
		epsilon += "0"

	zeroes = 0
	ones = 0

# convert to decimal
print("solution for part 1: " + str(int(gamma, 2) * int(epsilon, 2)))

# --------------------------- part 2 ---------------------------------

oxyrating = ""
co2rating = ""

firstbitone = ""
firsbitzero = ""
# loop over each column
for i in range(len(lines[0])):
	# loop over each row
	for j in range(len(lines)):
		if(lines[j][i] == "0"): 
			zeroes += 1
		else:
			ones += 1
	# find most and least common bit of index i
	if zeroes > ones:

	else:
		gamma += "1"
		epsilon += "0"

	zeroes = 0
	ones = 0


def recursivefunc(common):
	for i in range(len(lines[0])):
	# loop over each row
	if(common == "0"):
		for j in range(len(lines)):
			entry = lines[j][i]
				if(lines[j][i] == "0"): 
					firstbitzero.append(lines[j][i])
			else:
				ones += 1


print("solution for part 2: " + str(int(oxyrating, 2) * int(co2rating, 2)))