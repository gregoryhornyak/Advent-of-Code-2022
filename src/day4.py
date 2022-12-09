from importFile import *

def day4():
    filename = "day4_input"
    text = importFileAsTXT(f"C:/Users/Geri/Documents/AdventOfCode/resources/{filename}.txt")
    text = text.split("\n")
    includes = 0
    for line in text[:-1]:

        elf01,elf02 = line.split(",")

        if (int(elf01.split("-")[0]) >= int(elf02.split("-")[0]) and
            int(elf01.split("-")[-1]) <= int(elf02.split("-")[-1])): # elf02 is outer
                includes+=1
                
        elif (int(elf01.split("-")[0]) <= int(elf02.split("-")[0]) and
              int(elf01.split("-")[-1]) >= int(elf02.split("-")[-1])): # elf01 is outer
                includes+=1
                
    print("FIRST TASK:",includes)

    overlaps = 0
    for line in text[:-1]:

        elf01,elf02 = line.split(",")
        
        e1_set = set([i for i in range( int(elf01.split("-")[0]) , int(elf01.split("-")[-1])+1 ) ])
        e2_set = set([j for j in range( int(elf02.split("-")[0]) , int(elf02.split("-")[-1])+1 ) ])
        overlap = e1_set & e2_set
        if overlap:
            overlaps += 1

    print("SECOND TASK:",overlaps)
        
if __name__ == "__main__":
    day4()
