text = ""
with open("D1_input.txt","r") as inputs:
    text = inputs.read()

list_of_elves = []


calorie_sum = 0
for line in text.split("\n"):
    if line != "":
        calorie_sum += int(line)
    else:
        #print("BLANK")
        list_of_elves.append(calorie_sum)
        calorie_sum = 0

first = max(list_of_elves)
list_of_elves.remove(first)
second = max(list_of_elves)
list_of_elves.remove(second)
third = max(list_of_elves)
print(first,second,third)
print(first+second+third)
        
