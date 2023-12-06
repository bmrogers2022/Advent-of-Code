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

# to reverse engineer the mappings, reverse the list of conversions

reversed_mappings = conversions[::-1]

print(reversed_mappings)

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

# print(minimum)
