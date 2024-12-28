import numpy as np

with open('8input.txt') as f:
    lines = [list(line.strip()) for line in f.readlines()]

grid = np.array(lines)
blank_matrix = np.full(grid.shape, '.')

def antiNodes(coordinates):
    antiNodes = []
    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates)):
                if coordinates[i][0] != coordinates[j][0] and coordinates[i][1] != coordinates[j][1]:
                    # Calculate two additional points on the same line
                    ydif = coordinates[j][0] - coordinates[i][0]
                    xdif = coordinates[j][1] - coordinates[i][1]
                    node1 = (coordinates[i][0] - ydif, coordinates[i][1] - xdif)
                    node2 = (coordinates[j][0] + ydif, coordinates[j][1] + xdif)
                    antiNodes.append(node1)
                    antiNodes.append(node2)
    return [antinode for antinode in antiNodes if antinode[0] in yRange and antinode[1] in xRange]

yRange = range(len(lines))
xRange = range(len(lines[0]))

foundRadios = []
for y in lines:
    for x in y:
        if x != '.' and x not in foundRadios:
            foundRadios.append(x)
            #find coordinates of all x in lines
            coordinates = [(i, j) for i in range(len(lines)) for j in range(len(lines[i])) if lines[i][j] == x]
            for a in antiNodes(coordinates):
                blank_matrix[a[0]][a[1]] = 'x'

count_x = np.count_nonzero(blank_matrix == 'x')
print(f"Count of 'x' in blank_matrix: {count_x}")