from tqdm import trange

with open('11input.txt') as f:
    stones = [line.strip() for line in f.readlines()]
stones = stones[0].split(' ')
stones
# test = ['0', '1', '10', '99', '999']
secondTest = ['125', '17']
def blink(stones):
    newStones = []
    for  i in stones:
        if i == '0':
            newStones.append('1')
        elif len(i) % 2 == 0:
            newStones.append(i[:len(i)//2])
            newStones.append(str(int(i[len(i)//2:])))
        else:
            newStones.append(str(int(i)*2024))

    return newStones

for i in trange(25):
    stones = blink(stones)
print(len(stones))

# this seems like the most instructive part two so far. Need to return to this