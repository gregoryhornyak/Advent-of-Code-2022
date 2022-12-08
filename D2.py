text = ""
with open("D2_input.txt","r") as inputs:
    text = inputs.read()

score_matrix = {'A':1,'B':2,'C':3,
                'X':1,'Y':2,'Z':3}
beat_matrix = {'A':'Z','B':'X','C':'Y',
               'X':'C','Y':'A','Z':'B'}

# 0 = loss | 3 = draw | 6 = won
# total score = choice + end
text = text.split("\n")

total_score = 0
for l in range(len(text)):
    line = text[l]
    
    opp, me = line.split(" ")

    total_score += score_matrix[me]

    if me != beat_matrix[opp]: # didnt beat me
        if opp != beat_matrix[me]: # didnt beat him
            total_score += 3 
        else: # beat him
            total_score += 6
    else: # beat me
        if opp != beat_matrix[me]: # didnt beat him
            pass
        else: # beat him
            total_score += 3
            
print("TOTAL:",total_score)

#-------Second Part--------------------

end_matrix = {'A':'C','C':'B','B':'A'}

# X = LOSE | Y = DRAW | Z = WIN
total_score = 0
for l in range(len(text)):
    line = text[l]
    
    opp, me = line.split(" ")

    if me == "X": # lose
        total_score += score_matrix[end_matrix[opp]]
    elif me == "Y": # draw
        total_score += score_matrix[opp] + 3
    elif me == "Z": # win
        total_score += score_matrix[list(end_matrix.keys())[list(end_matrix.values()).index(opp)]] + 6
    else:
        print("ERROR")

print("TOTAL:",total_score)
