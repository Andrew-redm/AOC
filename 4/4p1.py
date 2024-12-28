with open('4input.txt') as f:
    lines = f.readlines()
lines


def search_word(grid, word):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def search_from(x, y, dx, dy):
        for i in range(word_len):
            if not in_bounds(x + i * dx, y + i * dy) or grid[x + i * dx][y + i * dy] != word[i]:
                return False
        return True

    count = 0
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if search_from(x, y, dx, dy):
                    count += 1
    return count

grid = [list(line.strip()) for line in lines]
word = 'XMAS'
count = search_word(grid, word)
print(f"Word '{word}' found {count} times")