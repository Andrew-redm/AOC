with open('10input.txt') as f:
    grid = [list(line.strip()) for line in f.readlines()]

rows, cols = len(grid), len(grid[0])
result = []

def count_connected_nines(r, c, visited):
    if not (0 <=  r < rows and 0 <= c < cols):
        return set()
    if grid[r][c] == '9':
        return {(r, c)}
    nines = set()
    current_height = int(grid[r][c])
    for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
        next_r, next_c = r + dr, c + dc
        if (0 <= next_r < rows and 0 <= next_c < cols and
            (next_r, next_c) not in visited and
            int(grid[next_r][next_c]) == current_height + 1):
            visited.add((next_r, next_c))
            nines.update(count_connected_nines(next_r, next_c, visited))
    return nines

total_score = 0
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == '0':
            connected_nines = count_connected_nines(i, j, {(i,j)})
            total_score += len(connected_nines)

print(total_score)
connected_nines 