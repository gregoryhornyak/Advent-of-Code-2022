from importFile import *

def dayX():
    filename = "day3_input"
    text = importFileAsTXT(f"C:/Users/Geri/Documents/AdventOfCode/resources/{filename}.txt")
    text = text.split("\n")


def matrix_rotation():
    sample = [[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]]
    print(sample)
    copy = list(zip(*sample[::-1]))
    print(copy)


"""

[11, 12, 13, 14, 15]
[16, 17, 18, 19, 20]
[21, 22, 23, 24, 25]
[26, 27, 28, 29, 30]

"""
if __name__ == "__main__":
    matrix_rotation()
