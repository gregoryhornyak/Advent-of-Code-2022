from importFile import *

def readCommand(stack,command):
    cmds = command.split(' ')
    src = int(cmds[3])
    dst = int(cmds[5])
    num = int(cmds[1])

    item = ''
    for i in range(num):
        item = stack[src].pop()
        stack[dst].append(item)

    return stack

def readCommand2(stack,command):
    cmds = command.split(' ')
    src = int(cmds[3])
    dst = int(cmds[5])
    num = int(cmds[1])

    item = ''
    temp_list = []
    for i in range(num):
    #    print(stack[src])
        t=''
        if stack[src]:
            t = stack[src].pop()
        temp_list.append(t)
        #print(temp_list)
    #print(temp_list)
    temp_list = temp_list[::-1]
    #print(temp_list)
    for a in temp_list:
        stack[dst].append(a)

    return stack

def day5():
    filename = "day5_input"
    text = importFileAsTXT(f"C:/Users/Geri/Documents/AdventOfCode/resources/{filename}.txt")
    text = text.split("\n")
    #----------------------#
    stacks = {1:[],2:[],3:[],4:[],5:[],
              6:[],7:[],8:[],9:[],}
    #[B] [T] [M] [B] [J] [C] [T] [G] [N]
    #01234567890123456789012345678901234
    # 1   5   9  13  17  21  25  29
    # difference: 4 -> if (x-1)%4==0 then CHAR
    
    #------------------< POPULATE DICT >------------------#
    
    i=0
    line = text[i]
    while line[:4] != '':
        for a in range(len(line)):
            if (a-1)%4==0 and line[a] != " " and not line[a].isnumeric():
                ind = (a-1)/4 + 1
                stacks[ind].append(line[a])
        i+=1
        line = text[i]

    for k,v in stacks.items():
        v = v.reverse()
    print(stacks)
    stacks20 = dict()
    stacks20 = stacks.copy()
    print(stacks20)
    #-----------< COMMANDS >-------------#

    for line in text[i+1:-1]:
        stacks = readCommand(stacks,line)

    #print(stacks)
    last_crates = ''
    for k,v in stacks.items():
        last_crates += v[-1]
    print("FIRST TASK:",last_crates)
    #---------------------------#
    print(stacks20)
    for line in text[i+1:-1]:
        stacks20 = readCommand2(stacks20,line)
    last_crates = ''
    for k,v in stacks20.items():
        last_crates += v[-1]
    print("SECOND TASK:",last_crates)


if __name__ == "__main__":
    day5()

# sanitize code
# separate reading and popping
# implement cycle to do multiple commands
