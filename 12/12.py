from collections import deque

with open('12input.txt') as f:
    lines = [list(line.strip()) for line in f.readlines()]

def get_neighbours(x, y, rows, cols):
    neighbors = []
    if x > 0:
        neighbors.append((x-1, y))
    if x < rows - 1:
        neighbors.append((x+1, y))
    if y > 0:
        neighbors.append((x, y-1))
    if y < cols - 1:
        neighbors.append((x, y+1))
    return neighbors

def search(start, plant_type, visited, lines):
    queue = deque([start])
    visited.add(start)
    area = 0
    perimeter = 0
    rows, cols = len(lines), len(lines[0])
    
    while queue:
        x, y = queue.popleft()
        area += 1
        local_perimeter = 4
        
        for nx, ny in get_neighbours(x, y, rows, cols):
            if lines[nx][ny] == plant_type:
                local_perimeter -= 1
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
        
        perimeter += local_perimeter
    
    return area, perimeter

def calculate_total_price(lines):
    visited = set()
    total_price = 0
    
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if (i, j) not in visited:
                plant_type = lines[i][j]
                area, perimeter = search((i, j), plant_type, visited, lines)
                total_price += area * perimeter
    
    return total_price

total_price = calculate_total_price(lines)
print(total_price)

