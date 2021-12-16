from typing import final


def init():
	input = open("day10_input.txt")
	lines = []
	while(i := input.readline()):
		i = i.rstrip("\n")
		lines.append(i)

	return lines

lines = init()

error_value = 0
queue = []

discarded_lines = lines[:]

for i in range(len(lines)):
   #print(str(error_value) + " for line: " + str(i))
    for j in range(len(lines[i])):
        entry = lines[i][j]
        if(entry == "("):
            queue.append(entry)
        elif(entry == "["):
            queue.append(entry)
        elif(entry == "{"):
            queue.append(entry)
        elif(entry == "<"):
            queue.append(entry)
        elif(entry == ")"):
            if(queue.pop() != "("):
                error_value += 3
                discarded_lines.remove(lines[i])
                break
        elif(entry == "]"):
            if(queue.pop() != "["):
                error_value += 57
                discarded_lines.remove(lines[i])
                break
        elif(entry == "}"):
            if(queue.pop() != "{"):
                error_value += 1197
                discarded_lines.remove(lines[i])
                break
        elif(entry == ">"):
            if(queue.pop() != "<"):
                error_value += 25137
                discarded_lines.remove(lines[i])
                break

print("solution of part 1 is: " + str(error_value))

new_discard = discarded_lines[:]

final_sequences = []
for i in range(len(discarded_lines)):
    for k in range(100):
        for j in range(len(discarded_lines[i]) - 1):
            entry = discarded_lines[i][j]
            entry2 = discarded_lines[i][j + 1]
            #print(entry + "\n" + entry2)
            if( (entry == "(" and entry2 == ")") or 
            (entry == "[" and entry2 == "]") or
            (entry == "{" and entry2 == "}") or
            (entry == "<" and entry2 == ">") ):
                new_discard[i] = new_discard[i][:j] + new_discard[i][j + 2:]
                discarded_lines[i] = new_discard[i][:]
                break
        
for i in range(len(new_discard)):
    new_discard[i] = list(new_discard[i][::-1])
    for j in range(len(new_discard[i])):
        if new_discard[i][j] == "(":
            new_discard[i][j] = ")"
        elif new_discard[i][j] == "{":
            new_discard[i][j] = "}"
        elif new_discard[i][j] == "[":
            new_discard[i][j] = "]"
        elif new_discard[i][j] == "<":
            new_discard[i][j] = ">"

for i in range(len(new_discard)):
    new_discard[i] = "".join(new_discard[i])
  
scores = []
for seq in new_discard:
    score = 0
    for i in range(len(seq)):
        score *= 5
        if(seq[i] == ")"):
            score += 1
        elif(seq[i] == "]"):
            score += 2
        elif(seq[i] == "}"):
            score += 3
        elif(seq[i] == ">"):
            score += 4
    scores.append(score)

print("solution of part 1 is: " + str(sorted(scores)[len(scores) // 2]))