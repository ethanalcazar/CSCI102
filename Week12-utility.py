def PrintOutput(x):
    print('OUTPUT', x)

def LoadFile(t):
    lines = []
    s = open(t, 'r')
    stuff = s.read()
    with open(t) as f:
        line = f.readlines()
        lines.append(line[0])
        lines.append(line[1])
        lines.append(line[2])
        lines.append(line[3])
        liness = str(lines)
        liness = liness.strip('\n')
        print(liness)

def UpdateString(a,b,c):
        d = a.replace(a[c], b)
        print(d)
