with open('1input.txt') as f:
    lines = f.readlines()

leftcol = []
rightcol = []

for line in lines:
    split = line.split('   ')
    leftcol.append(int(split[0]))
    rightcol.append(int(split[1]))

difScore = []

for i in leftcol:
    difScore.append(i * rightcol.count(i))

sum(difScore)