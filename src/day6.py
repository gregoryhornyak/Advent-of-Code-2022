from importFile import *

def day6():
    filename = "day6_input"
    text = importFileAsTXT(f"C:/Users/Geri/Documents/AdventOfCode/resources/{filename}.txt")
    visited_chars = []
    for c in range(len(text)-4):
        items = text[c:c+4]
        if len(set(items)) == len(items):
            print("FIRST TASK:",c+4)
            break
    for c in range(len(text)-14):
        items = text[c:c+14]
        if len(set(items)) == len(items):
            print("SECOND TASK:",c+14)
            break
        
if __name__ == "__main__":
    day6()
