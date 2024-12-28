import pandas as pd

with open('2input.txt') as f:
    lines = f.readlines()
lines

bads = []
counter = 0 
for line in lines:
    values = list(map(int, line.split(' ')))
    if values[0] < values[-1]:
        values.reverse()
    good = True
    for i in range(len(values)-1):
        if values[i] - values[i+1] <= 0 or values[i] - values[i+1] > 3:
            good = False
            
            values.pop(i+1)
            
            break 
    if good:
        counter += 1
    else:
        bads.append(values)
counter

#################################################
badToGood = []
beyondSaving = []
#by line
bads[0]
for bad in bads:
    solutionFound = False
    for j in range(len(bad)):
        dummy = bad[:j] + bad[j+1:]
        print(dummy, j, bad)
        good = True
        for i in range(len(dummy)-1):
            # test for goodness
            if dummy[i] - dummy[i+1] <= 0 or dummy[i] - dummy[i+1] > 3 or dummy[i] == dummy[i+1]:
                good = False
                break

        if good:
            badToGood.append(dummy)
            solutionFound = True
            break

    if not solutionFound:
        beyondSaving.append(bad)
len(beyondSaving)
beyondSaving
len(badToGood) + counter
badToGood

for i in badToGood:
    for j in range(len(i)-1):
        if j - j+1 > 3 or j - j+1 <= 0:
            print(i, j)

for i in beyondSaving:
    for j in range(len(i)-1):
        if not(j - j+1 > 3 or j - j+1 <= 0):
            print(i)
            break

len(beyondSaving)

badToGoodSet = set(tuple(bad) for bad in badToGood)
badToGoodSet
len(badToGoodSet) + counter

badToGood
len(beyondSaving)
        

counter = 0 
allVals = []
goods = []

for line in lines:
    values = list(map(int, line.split(' ')))
    allVals.append(values)
    good = True
    posCount = 0
    negCount = 0
    posVal = []
    negVal = []
    indexToDel = False

# can ignore large step sizes(?)
    for i in range(len(values)-1):
        if abs(values[i] - values[i+1]) > 3:
            indexToDel = i+1
            break
        if values[i] == values[i+1]:
            indexToDel = i+1
            break
        if values[i] - values[i+1] > 0:
            posCount += 1
            posVal.append(i)
        elif values[i] - values[i+1] < 0:
            negCount += 1
            negVal.append(i)

    if indexToDel:
        del values[indexToDel]

    if min(posCount, negCount) >= 2:
        good = False

    if posCount < negCount and posCount > 1:
        del values[posVal[0]]

    elif posCount > negCount and negCount > 1:
        del values[negVal[0]]
    
    if values[0] > values[-1]:
        values.reverse()
    
    for i in range(len(values)-1):
            if values[i] - values[i+1] >= 0 or values[i] - values[i+1] < -3:
                good = False
                break

    if good:
        counter += 1
        goods.append(values)
counter
len(allVals)
posVal
values
goods



data = [[int(n) for n in line.split()] for line in open("2input.txt").read().splitlines()]

def gaps(line): return [a-b for a,b in zip(line, line[1:])]
def safe_increase(line): return all(0<g<4  for g in gaps(line))
def safe_decrease(line): return all(0>g>-4 for g in gaps(line))
def is_safe(line): return safe_increase(line) or safe_decrease(line)
print("Part 1:", sum(is_safe(line) for line in data))

def trimmed(line): return [line[:i]+line[i+1:] for i in range(len(line))]
print("Part 2:", sum(any(is_safe(c) for c in [line, *trimmed(line)]) for line in data))