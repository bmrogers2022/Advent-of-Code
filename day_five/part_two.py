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
    for j in range(len(map_2)):
        source = int(instructions[0])
        source_two = int(map_2[j][0])
        lower_bound = int(map_2[j][1])
        range_len = int(map_2[j][2])
        upper_bound = lower_bound + range_len

        # find corresponding bounds
        if lower_bound <= source <= upper_bound:
            added_rule = []
            added_rule.append(source + source_two - lower_bound) # new source
            added_rule.append(int(instructions[1])) # keep map_1's lower bound
            added_rule.append(max(upper_bound-source, int(instructions[2]))) # same or lower upper bound
            if (int(instructions[2]) > upper_bound - source): # range not covered
                # TODO: fix this mess
                # should run same thing with source,  + (int(map_1[i][2]) - (upper_bound - source))
                new_instructions = []
                new_instructions.append(source+int(instructions[2])-upper_bound+source) # new source
                new_instructions.append(int(instructions[1])+int(instructions[2])-upper_bound+source) # new lower
                new_instructions.append(int(instructions[2])-upper_bound+source) # new upper
                return [added_rule, combine_rules(new_instructions, map_2)]
            else:
                return [added_rule]
        # TODO: add upper bounds check (source + int(instructions[2]))
    return [instructions] # if nothing changes, keep same rule

def add_rules(instructions, map_1, outputter):
    add = True
    for j in range(len(map_1)):
        lower_bound = int(map_1[j][1])
        range_len = int(map_1[j][2])
        upper_bound = lower_bound + range_len
        our_lower = int(instructions[1])
        our_upper = our_lower + int(instructions[2])
        # find corresponding bounds
        if lower_bound <= our_lower <= upper_bound:
            add = False
            if lower_bound <= our_upper <= upper_bound:
                break
            for i in add_rules([instructions[0], upper_bound, our_upper-upper_bound], map_1, outputter):
                outputter.append(i)
        elif lower_bound <= our_upper <= upper_bound:
            add = False
            for i in add_rules([instructions[0], our_lower, lower_bound], map_1, outputter):
                outputter.append(i)
        elif lower_bound > our_lower and upper_bound < our_upper:
            add = False
            for i in add_rules([instructions[0], upper_bound, our_upper-upper_bound], map_1, outputter):
                outputter.append(i)
            for i in add_rules([instructions[0], our_lower, lower_bound], map_1, outputter):
                outputter.append(i)
    if add:
        outputter.append(instructions)
    return outputter

"""
Our entire current objective is to create a function that combines two 
separate maps. This seems to be the hardest part of the implementation.
"""
def combine_maps(map_1, map_2):
    combined_instructions = []
    # go through each source category in map_1, change to corresponding map_2 value
    for i in range(len(map_1)):
        for rule in combine_rules(map_1[i], map_2):
            combined_instructions.append(rule)
    
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
print(conversions)
print(combine_maps(conversions[0], conversions[1]))
print(minimum)
