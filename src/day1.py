from importFile import *

def day1():
    text = importFileAsTXT("C:/Users/Geri/Documents/AdventOfCode/resources/day1_input.txt")
    list_of_elves = []
    calorie_sum = 0
    for line in text.split("\n"):
        if line != "":
            calorie_sum += int(line)
        else:
            list_of_elves.append(calorie_sum)
            calorie_sum = 0

    first = max(list_of_elves)
    list_of_elves.remove(first)
    second = max(list_of_elves)
    list_of_elves.remove(second)
    third = max(list_of_elves)
    print("FIRST TASK:",first,second,third)
    print("SECOND TASK:",first+second+third)

if __name__ == "__main__":
    day1()
