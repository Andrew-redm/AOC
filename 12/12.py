with open('extraExample.txt') as f:
    lines = [list(line.strip()) for line in f.readlines()]

plants = {}

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for y in range(len(lines)):
    for x in range(len(lines[y])):
        neighbours = 4
        for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 <= ny < len(lines) and 0 <= nx < len(lines[0]):
                    if lines[y][x] != lines[ny][nx]:
                        neighbours -= 1
        if lines[y][x] in plants:
            plants[lines[y][x]] += neighbours
        else:
            plants[lines[y][x]] = neighbours

plants     

# perimeter - can this just be the count of  
# neighbours that are the same for each instance? diagonals dont matter lol
# area - is just sum