text = ""
with open("D3_input.txt","r") as inputs:
    text = inputs.read()

text = text.split("\n")

priorities = []

for r in text:
    value = 0
    comp01 = r[:(len(r)//2)]
    comp02 = r[(len(r)//2):]

    share = set(comp01) & set(comp02)
    e = ''
    if share:
        e = share.pop()
        
    if e.islower():
        value = ord(e) - 96
    elif e.isupper():
        value = ord(e) - 38
    elif e == '':
        pass
    priorities.append(value)

print(sum(priorities))

    
