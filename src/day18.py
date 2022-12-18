from importFile import *

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

def compareCoord(cl1,cl2):
    if cl1.coords.x == cl2.coords.x and cl1.coords.y == cl2.coords.y and cl1.coords.z == cl2.coords.z: return True

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
    for cube in list_of_cubes:
        for comp_cube in list_of_cubes:
            if cube.id == comp_cube.id: break
            if compareCoord(cube.north,comp_cube.north): cube.surfaces-=1
            if cube.south == comp_cube.south: cube.surfaces-=1
            if cube.west == comp_cube.west: cube.surfaces-=1
            if cube.east == comp_cube.east: cube.surfaces-=1
            if cube.top == comp_cube.top: cube.surfaces-=1
            if cube.bot == comp_cube.bot: cube.surfaces-=1
        surface += cube.surfaces
    print(surface)
    


if __name__ == "__main__":
    day18()
