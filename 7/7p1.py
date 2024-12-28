from itertools import product

with open('7input.txt') as f:
    lines =  f.readlines()

lines = [line.strip() for line in lines]
lines = [line.split(' ') for line in lines]
target_values = [line[0] for line in lines]
target_values = [int(target[:-1]) for target in target_values]
target_values

numbers = [[int(num) for num in line[1:]] for line in lines]

def evaluate_expression(nums, ops):
    result = nums[0]
    for num, op in zip(nums[1:], ops):
        if op == '+':
            result += num
        elif op == '*':
            result *= num
    return result
def check_combinations(target, nums):
    for ops in product(['*', '+'], repeat=len(nums)-1):
        if evaluate_expression(nums, ops) == target:
            return target

combination_results = []
for target, nums in zip(target_values, numbers):
    combination_results.append(check_combinations(target, nums))



print(combination_results.count(True)/len(combination_results))
combination_results = [result for result in combination_results if result is not None]
sum(combination_results)