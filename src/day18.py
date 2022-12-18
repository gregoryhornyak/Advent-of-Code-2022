from importFile import *

def compareCoord(cl1,cl2):
    if cl1.x == cl2.x and cl1.y == cl2.y and cl1.z == cl2.z: 
        #print("SAME")
        return True
    return False

class Coordinate:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

class Cube:
    num_of_cubes = 0

    def __init__(self,x,y,z):
        self.id = Cube.num_of_cubes
        # coordinate
        self.coords = Coordinate(x,y,z)
        self.surfaces = 6
        self.calc_sides_coords()
        Cube.num_of_cubes+=1

    def calc_sides_coords(self):
        self.north = Coordinate(self.coords.x,self.coords.y+0.5,self.coords.z)
        self.south = Coordinate(self.coords.x,self.coords.y-0.5,self.coords.z)
        self.east = Coordinate(self.coords.x+0.5,self.coords.y,self.coords.z)
        self.west = Coordinate(self.coords.x-0.5,self.coords.y,self.coords.z)
        self.top = Coordinate(self.coords.x,self.coords.y,self.coords.z+0.5)
        self.bot = Coordinate(self.coords.x,self.coords.y,self.coords.z-0.5)
        self.side_coords = [self.north,self.south,self.east,self.west,self.top,self.bot]

def day18():
    filename = "day18_input"
    text = importFileAsTXT(f"C:/Users/Geri/Documents/AdventOfCode/resources/{filename}.txt")
    text = text.split("\n")
    list_of_cubes = []

    for line in text:
        coords = list(map(int,line.split(",")))
        list_of_cubes.append(Cube(coords[0],coords[1],coords[2]))
    #print(Cube.num_of_cubes)
    surface = 0
    _6sides = 0
    diff = False
    for cube in list_of_cubes:
        for comp_cube in list_of_cubes:
            if cube.id != comp_cube.id:
                diff = True
                for side in cube.side_coords:
                    for side_comp in comp_cube.side_coords:
                        if compareCoord(side,side_comp):
                            cube.surfaces-=1
        if diff:
            surface += cube.surfaces
        diff = False

            
    print("FIRST TASK:",surface)



if __name__ == "__main__":
    day18()
