from importFile import *

def calcASCII(cut):
    value = 0
    if cut.islower():
        value = ord(cut) - 96
    elif cut.isupper():
        value = ord(cut) - 38
    elif cut == '':
        pass
    return value
def day3():
    text = importFileAsTXT("C:/Users/Geri/Documents/AdventOfCode/resources/day3_input.txt")
    text = text.split("\n")
    
    priorities = []

    for r in text:
        value = 0
        comp01 = r[:(len(r)//2)]
        comp02 = r[(len(r)//2):]

        share = set(comp01) & set(comp02)
        cut = ''
        if share:
            cut = share.pop()
        value = calcASCII(cut)
        priorities.append(value)

    print("FIRST TASK:",sum(priorities))
    
    priorities = []
    rucksacks = []
    for r in text:
        if len(rucksacks) < 4:
            rucksacks.append(r)
        if len(rucksacks) == 3:
            #comp01 = rucksacks[0]
            #comp02 = rucksacks[1]
            #comp03 = rucksacks[2]
            share = set(rucksacks[0]) & set(rucksacks[1]) & set(rucksacks[2])
            cut = ''
            if share:
                cut = share.pop()
            value = calcASCII(cut)
            priorities.append(value)
            rucksacks = []
    print("SECOND TASK:",sum(priorities))

if __name__ == "__main__":
    day3()
