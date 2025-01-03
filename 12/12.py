with open('extraExample.txt') as f:
    lines = [list(line.strip()) for line in f.readlines()]

def get_neighbours(x, y, rows, cols):
