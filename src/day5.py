def reader():
    f = open("D5_input.txt","r")
    text = ""
    with open("D5_input.txt","r") as my_file:
        lines = my_file.read()
    found = False
    for line in lines.split('\n'):
        if len(line) == 0:
            found = True
        if found:
            text += line + '\n'
    text = text.strip(' \n')
    print(text)
    return text

class Crane():
    
    stacks = [['B','G','S','C'],['T','M','W','H','J','N','V','G'],['M','Q','S'],['B','S','L','T','W','N','M'],['J','Z','F','T','V','G','W','P'],['C','T','B','G','Q','H','S',],['T','J','P','B','W',],['G','D','C','Z','F','T','Q','M',],['N','S','H','B','P','F',]]

    commandsList=""

    def getCL(self,CL):
        self.commandsList = CL
    
    def readCommand(self,command):
        cmds = command.split(' ')
        src = int(cmds[3])
        dst = int(cmds[5])
        rng = int(cmds[1])
        print(f'Move {rng} pcs from pile {src} to pile {dst}')
        print(self.stacks[src])
        print(self.stacks[dst])
        item = ''
        for i in range(rng):
            item = self.stacks[src].pop()
            self.stacks[dst].append(item)
        print(self.stacks[src])
        print(self.stacks[dst])         

        
crane01 = Crane()
crane01.getCL(reader())
crane01.readCommand('move 2 from 4 to 2')

# sanitize code
# separate reading and popping
# implement cycle to do multiple commands
