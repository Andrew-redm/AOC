with open('6input.txt') as f:
    lines = [list(line.strip()) for line in f.readlines()]

directions = ['>', 'v', '<', '^']
guard = None
def stepOrTurn(lines, guard):
    if not guard:
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                if char in directions:
                    guard =  [[y, x], char]
    if guard[1] == '>':
        if lines[guard[0][0]][guard[0][1] + 1] != '#':
            guard[0][1] += 1
            lines[guard[0][0]][guard[0][1]] = guard[1]
            lines[guard[0][0]][guard[0][1]] = 'X' #y, x

        else:
            guard[1] = 'v'
    if guard[1] == 'v':
        if lines[guard[0][0]+1][guard[0][1]] != '#':
            guard[0][0] += 1
            lines[guard[0][0]][guard[0][1]] = guard[1]
            lines[guard[0][0]][guard[0][1]] = 'X' #y, x

        else:
            guard[1] = '<'
    if guard[1] == '<':
        if lines[guard[0][0]][guard[0][1] - 1] != '#':
            guard[0][1] -= 1
            lines[guard[0][0]][guard[0][1]] = guard[1]
            lines[guard[0][0]][guard[0][1]] = 'X' #y, x

        else:
            guard[1] = '^'
    if guard[1] == '^':
        if lines[guard[0][0]-1][guard[0][1]] != '#':
            guard[0][0] -= 1
            lines[guard[0][0]][guard[0][1]] = guard[1]
            lines[guard[0][0]][guard[0][1]] = 'X' #y, x

        else:
            guard[1] = '>'

    return guard

while True:
    try:
        guard = stepOrTurn(lines, guard)
        count_X = sum(line.count('X') for line in lines) + 1
    except IndexError:
        break
print(count_X)

# with open('output.txt', 'w') as f:
#     for line in lines:
#         f.write(''.join(line) + '\n')