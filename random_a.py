#!/usr/bin/python3
import fileinput

text = ""
with open("D2_input.txt","r") as inputs:
    text = inputs.read()

text = text.split("\n")

fileinput = text

beats = {'A':'Z', 'B':'X', 'C':'Y', 'X':'C', 'Y':'A', 'Z':'B'}
score = {'X':1, 'Y':2, 'Z':3}

total = 0
for line in fileinput:
	plays = line.rstrip().split(' ')
	total += score[plays[1]]
	if plays[0] == beats[plays[1]]:
		# print('%s beats %s' % (plays[1], plays[0]))
		total += 6
	elif plays[1] == beats[plays[0]]:
		# print('%s loses to %s' % (plays[1], plays[0]))
		pass
	else:
		# print('%s draws against %s' % (plays[1], plays[0]))
		total += 3	# draw

print(total)
