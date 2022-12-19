from itertools import groupby
elves = []
calories_per_elf =[]

with open("input.txt", 'r') as f:
    lines = f.readlines()
    removed_newlines_list = []
    for line in lines:
        removed_newlines_list.append(line.replace('\n',''))
    for k, g in groupby(removed_newlines_list, key=bool):
        if k:
            elves.append(list(g))

for elf in elves:
    rolling_sum = 0
    for calories in elf:
        rolling_sum += int(calories)
    calories_per_elf.append(rolling_sum)

print(max(calories_per_elf)) #part one answer
print()

###
ordered_elves = calories_per_elf
ordered_elves.sort(reverse = True)
sum_ordered_elves = ordered_elves[0] + ordered_elves[1] + ordered_elves[2]

print(sum_ordered_elves) #part two answer
