with open('1input.txt') as f:
    lines = f.readlines()
lines
leftcol = []
rightcol = []

for line in lines:
    split = line.split('   ')
    leftcol.append(int(split[0]))
    rightcol.append(int(split[1]))

leftcol.sort()
leftcol
rightcol.sort()
rightcol
difcol = []

len(leftcol) == len(rightcol)
difcol
for i in range(len(leftcol)):
    dif = leftcol[i] - rightcol[i]
    difcol.append(abs(dif))
difcol
sum(difcol)

counter = 0
for report in reports:
    #logic
    if rule 1 and rule 2:
        counter = counter + 1
