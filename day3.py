
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

def foo(int_to_keep, lines, kind, bit_to_check):
	global oxyrating
	global co2rating
	firstbitone = []
	firstbitzero = []
	zeroes = 0
	ones = 0
	# loop over each row
	for j in range(len(lines)):
		if(lines[j][bit_to_check] == "0"): 
			firstbitzero.append(lines[j])
			zeroes += 1
		else:
			firstbitone.append(lines[j])
			ones += 1

	if(ones >= zeroes and kind == "oxy"):
		int_to_keep = 1
	elif(ones < zeroes and kind == "oxy"):
		int_to_keep = 0
	elif(ones >= zeroes and kind == "co2"):
		int_to_keep = 0
	else:
		int_to_keep = 1

	if(int_to_keep == 0):
		if(len(firstbitzero) == 1):
			if(kind == "oxy"):
				oxyrating = firstbitzero[0]
			else:
				co2rating = firstbitzero[0]
			return
		else:
			foo(int_to_keep, firstbitzero, kind, bit_to_check = bit_to_check + 1)
			return
	else:
		if(len(firstbitone) == 1):
			if(kind == "oxy"):
				oxyrating = firstbitone[0]
			else:
				co2rating = firstbitone[0]
			return
		else:
			foo(int_to_keep, firstbitone, kind, bit_to_check = bit_to_check + 1)
			return

zeroes = 0
ones = 0
starting_index = 0

for j in range(len(lines) - 1):
	if(lines[j][0] == "0"): 
		zeroes += 1
	else:
		ones += 1

# find what digit to look for
if zeroes > ones:
	foo(0, lines, "oxy", starting_index)
	foo(1, lines, "co2", starting_index)
else:
	foo(1, lines, "oxy", starting_index)
	foo(0, lines, "co2", starting_index)

# convert to decimal
print("solution for part 2: " + str(int(oxyrating, 2) * int(co2rating, 2)))