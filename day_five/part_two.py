# variables to make changing between testing and running easy
problem_file = "data.txt"
tester_file = "test.txt"

# put file lines into data
with open(tester_file) as file:
    data = file.readlines()

# store min
minimum = float("inf") # max possible int

# firstly, lets pull all the seeds by splitting at spaces and removing "seeds:"
seeds = data[0].split()[1:]

# secondly, lets separate all the different conversions
conversions = []
i = 0
while i < len(data):
    if data[i] == "\n":
        new_conversion = []
        while i+2 < len(data) and data[i+2] != "\n":
            new_conversion.append(data[i+2][:-1].split()) # don't include "\n"
            i += 1
        conversions.append(new_conversion)
        i -= 1 # sets data[i] to be "\n" for next iteration
    i += 1

# hopefully successfully combines all rules from maps 1 and 2
def combine_rules(instructions, map_2):
    for i in range(len(map_2)):
        # set variables
        m1d = int(instructions[0])
        m1s = int(instructions[1])
        m1i = int(instructions[2])
        if m1i == 0:
            return []
        m1m = m1d + m1i - 1
        m2d = int(map_2[i][0])
        m2s = int(map_2[i][1])
        m2i = int(map_2[i][2])
        m2m = m2s + m2i - 1
        # | = m1, \ = m2
        # case 1: ||\\
        if m1m < m2s:
            # check next command
            continue
        # case 2: \\||
        elif m1d > m2m:
            # check next command
            continue
        # case 3: |\|\
        elif m1d <= m2s and m2s <= m1m <= m2m:
            # we want to return new instructions for \| and run again on |\
            new_instructions = []
            new_instructions.append(m2d) # same starting destination as m2
            new_instructions.append(m1s+(m2s-m1d)) # same source plus \ - |
            new_instructions.append(m1m-m2s+1) # range of | - \
            new_command = []
            new_command.append(m1d) # same starting destination as m1
            new_command.append(m1s) # same starting source as m1
            new_command.append(m2s-m1d) # range of \ - |
            return new_instructions + combine_rules(new_command, map_2)
        # case 4: \|\|
        elif m2s <= m1d and m1d <= m2m <= m1m:
            # we want to return new instructions for |\ and run again on \|
            new_instructions = []
            new_instructions.append(m2d+(m1d-m2s)) # starting destination of m2 + diff between \ and |
            new_instructions.append(m1s) # same source as m1
            new_instructions.append(m2m-m1d+1) # range of \ - |
            new_command = []
            new_command.append(m1d+(m2m-m1d)+1) # same destination + diff of \ and |
            new_command.append(m1s+(m2m-m1d)+1) # same source + diff of \ and |
            new_command.append(m1m-m2m) # range of | - \
            return new_instructions + combine_rules(new_command, map_2)
        # case 5: \||\
        elif m2s <= m1d and m2m >= m1m:
            # we want to return new instructions for ||
            new_instructions = []
            new_instructions.append(m2d+(m1d-m2s)) # destination of m2 + diff between | and \
            new_instructions.append(m1s) # same source as m1
            new_instructions.append(m1i) # same increment as m1
            return new_instructions
        # case 6: |\\|
        elif m1d <= m2s and m1m >= m2m:
            # we want to return new instructions for \\ and run again on |\ and \|
            new_instructions = []
            new_instructions.append(m2d) # same destination as m2
            new_instructions.append(m1s+(m2s-m1d)) # old starting + diff between \ and |
            new_instructions.append(m2i) # same range as m2
            first_command = []
            first_command.append(m1d) # same destination as m1
            first_command.append(m1s) # same start as m1
            first_command.append(m2s-m1d) # range of | to \
            second_command = []
            second_command.append(m1d+(m2m-m1d)+1) # destination of m1 + \ - |
            second_command.append(m1s+(m2m-m1d)+1) # start of m1 + \ - |
            second_command.append(m1m-m2m) # range of \ through |
            return new_instructions + combine_rules(first_command, map_2) + combine_rules(second_command, map_2)
    # if instructions remain unchanged through all new rules, return same instructions
    return [m1d, m1s, m1i]

# we will feed this function rules after running combine_rules
def add_rules(instructions, map_1):
    for i in range(len(map_1)):
        # set variables
        m2d = int(instructions[0])
        m2s = int(instructions[1])
        m2i = int(instructions[2])
        m2m = m2s + m2i - 1
        if m2i == 0:
            return []
        m1d = int(map_1[i][0])
        m1s = int(map_1[i][1])
        m1i = int(map_1[i][2])
        m1m = m1s + m1i - 1
        # | = m1, \ = m2
        # case 1: ||\\
        if m2s > m1m:
            continue
        # case 2: \\||
        elif m2m < m1s:
            continue
        # case 3: |\|\
        elif m1s <= m2s and m2s <= m1m <= m2m:
            # we want to try again with a smaller range
            new_instructions = []
            new_instructions.append(m2d+(m1m-m2s)+1) # destination of m2 + | - \
            new_instructions.append(m1m+1) # start where m1m ends
            new_instructions.append(m2m-m1m) # range of \ - |
            return add_rules(new_instructions, map_1)
        # case 4: \|\|
        elif m2s <= m1s and m1s <= m2m <= m1m:
            # we want to try again with a smaller range
            new_instructions = []
            new_instructions.append(m2d) # same destination as m2
            new_instructions.append(m2s) # same start as m2
            new_instructions.append(m1s-m2s) # range of | - \
            return add_rules(new_instructions, map_1)
        # case 5: \||\
        elif m2s <= m1s and m2m >= m1m:
            # we want to try again with two smaller ranges
            new_instructions = []
            new_instructions.append(m2d) # same destination as m2
            new_instructions.append(m2s) # same start as m2
            new_instructions.append(m2i-(m1s-m2s)) # range of | - \
            second_instructions = []
            second_instructions.append(m2d+(m1m-m2s)+1) # same destination as m2 + | - \
            second_instructions.append(m1m+1) # start where m1 ends
            second_instructions.append(m2m-m1m) # range of \ - |
            return add_rules(new_instructions, map_1) + add_rules(second_instructions, map_1)
        # case 6: |\\|
        elif m1s <= m2s and m1m >= m2m:
            # if fully engulfed, fail and return []
            return []
    return [m2d, m2s, m2i]

"""
Our entire current objective is to create a function that combines two 
separate maps. This seems to be the hardest part of the implementation.
"""
def combine_maps(map_1, map_2):
    combined_instructions = []
    # go through each source category in map_1, change to corresponding map_2 value
    for i in range(len(map_1)):
        rule = []
        combined_rules = combine_rules(map_1[i], map_2)
        for j in range(len(combined_rules)):
            rule.append(combined_rules[j])
            if (j + 1) % 3 == 0:
                combined_instructions.append(rule)
                rule = []
    for i in range(len(map_2)):
        rule = []
        added_rules = add_rules(map_2[i], combined_instructions)
        for j in range(len(added_rules)):
            rule.append(added_rules[j])
            if (j + 1) % 3 == 0:
                combined_instructions.append(rule)
                rule = []
        
    
    # check bounds in map_2 that aren't in map_1
    # for j in range(len(map_2)):
    #     for rule in add_rules(map_2[j], map_1, []):
    #         combined_instructions.append(rule)

    return combined_instructions

# make a function that finds location number of seeds
def find_location(seed):

    for i in conversions:
        for j in i:
            if int(j[1]) <= seed <= (int(j[1])+int(j[2])): # inbounds(seed) if this is too inefficient
                seed = int(j[0]) + (seed-int(j[1]))
                break

    return seed

# for s in range(0, len(seeds), 2):
#     for s2 in range(int(seeds[s+1])):
#         minimum = min(find_location(int(seeds[s])+s2), minimum)
#     print(f"one done. min = {minimum}")
print(conversions[0], conversions[1])
print(combine_maps(conversions[0], conversions[1]))
print(minimum)
