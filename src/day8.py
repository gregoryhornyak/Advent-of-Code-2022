# How many trees are visible from outside the grid?

from importFile import *

class Tree:
    counter = 0
    def __init__(self,x,y,h):
        self.x = x
        self.y = y
        self.h = h
        Tree.counter+=1

def findMax(inlist):
    maxx = inlist[0].h
    for tree in inlist:
        if maxx < tree.h:
            maxx = tree.h
    return maxx

def itemInList(item, inlist):
    for tree in inlist:
        if tree.h == item.h and tree.x == item.x and tree.y == item.y:
            return True
    return False

def day8():

    #---< IMPORTING FILE >---#
    filename = "day8_input"
    text = importFileAsTXT(f"C:/Users/Geri/Documents/AdventOfCode/resources/{filename}.txt")
    text = text.split("\n")[:-1]

    #---< CREATING FOREST >---#
    forest = [[int(l) for l in line] for line in text]
    single_row = []
    visible_trees = [] # (x,y)

    #---< CREATING TREES FROM NUMBERS AND RAYTRACING >---#

    for r in range(4): # rotate the forest 4x times
        scan_len = len(forest)
        for x in range(scan_len): # scanner
            for y in range(scan_len):
                if r%2!=0:
                    single_row.append(Tree(scan_len-x,scan_len-y,forest[y][x])) # CREATE TREE
                else:
                    single_row.append(Tree(x,y,forest[y][x])) # CREATE TREE
            highest = findMax(single_row)

            #---< RAYTRACING >---#
            h = 0
            tree_index = 0
            while h<=highest:
                tree = single_row[tree_index]
                if tree.h >= h: # found a tree
                    # save coordinate
                    if not itemInList(tree,visible_trees):
                        visible_trees.append(tree)
                    h = tree.h + 1                
                tree_index+=1
            single_row = []

        #---< ROTATE THE FOREST >---#
        forest = list(zip(*forest[::-1]))

    #---< PRINT OUTCOME >---#
    print(len(visible_trees))
    print(Tree.counter)
    outfile = open('C:/Users/Geri/Documents/AdventOfCode/resources/trees.txt','w') 
    for tree in visible_trees:
        outfile.write((f"({tree.x},{tree.y}) + {tree.h}"))
        outfile.write('\n')
    outfile.close()

            

        

if __name__ == "__main__":
    day8()
