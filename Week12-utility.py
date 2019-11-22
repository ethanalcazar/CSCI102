#Ethan Alcazar
#Professor Tracy Camp
#CSCI 102
#Week 12 - Utility

#GitHub information
#https://github.com/ethanalcazar/CSCI102
#Professor Tracy Camp
#CSCI 102
#Week 12 - Utility

def PrintOutput(x):
    print('OUTPUT', x)

def LoadFile(t):
    s = open(t, 'r')
    stuff = s.read()
    with open(t) as f:
        line = f.readlines()
        print('OUTPUT', line)
def UpdateString(a,b,c):
    action = a.replace(a[c], b, 1)
    PrintOutput(action)

def FindWordCount(a,b):#"a" is the file which is being opened. Type in the name of the file, and it does the rest.
    s = open(a, 'r')
    stuff = s.read()
    x = stuff.find(b)
    return x

def ScoreFinder(players, scores, c):
    players = str(players)
    c = str(c)
    players_l = players.lower()
    players_cl = c.lower()
    answer = players_l.find(players_cl)
    result = 0
    if result == -1:
        print('OUTPUT Try again')
    else:
        score = scores[answer]
        print("OUTPUT", players_cl, 'got a score of', score)

def Union(a, b):
    merged_list = a + b
    PrintOutput(merged_list)

def Intersection(a,b):
    names = []
    for i in a:
        if i in b:
            names.append(i)
    print('OUTPUT', names)

def NotIn(a,b):
    i = 0
    lis = []
    while i < len(a):
        if a[i] not in b:
            lis.append(a[i])
            i += 1
        else:
            i += 1
    print('OUTPUT', lis)


