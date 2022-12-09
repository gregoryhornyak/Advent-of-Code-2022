def reader():
    text = ""
    with open("C:/Users/Geri/Documents/AdventOfCode/D7_input.txt","r") as inputt:
        text = inputt.read()
    return text

def loop_through(text):
    for line in text.split("\n"):
        print(line)
        break

if __name__ == "__main__":
    text = reader()
    loop_through(text)