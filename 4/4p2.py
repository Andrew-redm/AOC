with open('4input.txt') as f:
    lines = f.readlines()
lines
linecount = 0
counter = 0
for line in lines[:-2]:
    first = ['M', 'S']
    second = ['M', 'S']
    for char in range(len(line)-2):
        if line[char] in first and line[char+2] in second and lines[linecount+1][char+1] == 'A':
            first.remove(line[char])
            second.remove(line[char+2])
            
            if lines[linecount+2][char] in second and lines[linecount+2][char+2] in first:
                counter += 1
                print(line[char], line[char+2])
            first = ['M', 'S']
            second = ['M', 'S']
            
    linecount += 1
counter
