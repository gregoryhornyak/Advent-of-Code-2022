from importFile import *

class Tree:
    drive = {'/':{},'sum':0}

    def test(self):
        filename = "day7_input"
        text = importFileAsTXT(f"C:/Users/Geri/Documents/AdventOfCode/resources/{filename}.txt")
        text = text.split("\n")
        scroll = True
        i = 0 # iterator
        parent_dir = self.drive['/']
        while scroll: # loop until reaches end
            line = text[i] # always get current line
            line = line.split(' ') # break into words
            if line[0]+' '+line[1] == '$ cd': # directory name
                directory = line[-1]
                # possible new directory
                self.drive = parent_dir # save parent directory
                # change parent_dir to current dir
                parent_dir = parent_dir[directory]
                if directory not in parent_dir: # (list(DICT.keys())[list(DICT.values()).index(VALUE)]) 
                    currently_in_directory = {}
                    currently_in_directory['sum'] = 0
            # skip first line of input!
            elif line[0]+' '+line[1] == '$ ls': # store items | dir or number
                i+=1 # next line
                next_line = text[i]
                while next_line[0] != '$': # shoot hook / fishing
                    next_line = next_line.split(' ')
                    if next_line[0] == 'dir': # store dictionary
                        if next_line[-1] not in parent_dir:
                            parent_dir[next_line[-1]] = {}
                            parent_dir[next_line[-1]]['sum'] = 0
                    elif next_line[0].isnumeric(): # if number
                        if next_line not in parent_dir:
                            parent_dir[next_line] = int(next_line[0])
                            parent_dir['sum'] += int(next_line[0])
                    i += 1 # next item




            i += 1 # next line


def day7():
    filename = "day7_input"
    text = importFileAsTXT(f"C:/Users/Geri/Documents/AdventOfCode/resources/{filename}.txt")
    text = text.split("\n")
    

if __name__ == "__main__":
    day7()

