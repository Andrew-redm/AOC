with open('9input.txt') as f:
    inputString = f.readlines()

inputString = inputString[0]
len(inputString)

testString = '2333133121414131402'
testString2 = '12345'

file = True
index = 0


# uncompress
uncompressed = []
for i in inputString:
    if not file:
        for j in range(int(i)):
            uncompressed.append('.')
    if file:
        for j in range(int(i)):
            uncompressed.append(index)
        index += 1
    file = not file

while True:
    try:
        left_dot_index = uncompressed.index('.')
        right_num_index = len(uncompressed) - 1 - uncompressed[::-1].index(next(filter(lambda x: isinstance(x, int), uncompressed[::-1])))
        if left_dot_index < right_num_index:
            uncompressed[left_dot_index], uncompressed[right_num_index] = uncompressed[right_num_index], uncompressed[left_dot_index]
        else:
            break
    except ValueError:
        break

checkSum = []

for i in range(len(uncompressed)):
    if isinstance(uncompressed[i], int):
        checkSum.append(uncompressed[i]*i)

print(sum(checkSum))
