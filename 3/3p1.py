import re

with open('3input.txt') as f:
    lines = f.readlines()

lines = ''.join(lines)

pattern = r'(mul\(\d+,\d+\)|do\(\)|don\'t\(\))'
matches = re.findall(pattern, lines)
matches

sumOfProds = 0
do = True
for match in matches:
    if match == 'do()':
        do = True
        continue
    elif match == "don't()":
        do = False
        continue

    nums = re.findall(r'\d+', match)
    mulprod = int(nums[0]) * int(nums[1])
    if do:
        sumOfProds += mulprod
    
sumOfProds