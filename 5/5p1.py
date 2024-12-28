from collections import defaultdict, deque

with open('rules.txt') as f:
    rules = f.readlines()

rules = [rule.split('|') for rule in rules]
rules = [[int(rule[0]), int(rule[1])] for rule in rules]

with open('manuals.txt') as f:
    manuals = [line.strip() for line in f]

len(rules)
manuals
manuals = [manual.split(',') for manual in manuals]
manuals = [[int(item) for item in manual] for manual in manuals]

valid_middle_numbers = []

for manual in manuals:
    valid = True
    for rule in rules:
        if rule[0] in manual and rule[1] in manual:
            if manual.index(rule[0]) > manual.index(rule[1]):
                valid = False
                break
    if valid:
        if manual:
            middle_index = len(manual) // 2
            valid_middle_numbers.append(manual[middle_index])

print(sum(valid_middle_numbers))

#part two work in progress
applicable_rules = []

for manual in manuals:
    valid = True
    for rule in rules:
        if rule[0] in manual and rule[1] in manual:
            if manual.index(rule[0]) > manual.index(rule[1]):
                valid = False
                break
    if valid:
        applicable_rules.append(manual)


