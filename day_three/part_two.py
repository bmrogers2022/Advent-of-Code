# variables to make changing between testing and running easy
problem_file = "data.txt"
tester_file = "test_two.txt"

# put file lines into data
with open(problem_file) as file:
    data = file.readlines()

# same method of counter from previous problems
counter = 0

# set up for the problems
number_indexes = {}
# no repeat indexes
symbol_indexes = set()
adjacencies = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
max_x = len(data[0])-1 #-1 for new line char
max_y = len(data)

# function to add to indexes
def symbol_add(y, x):
    for i in adjacencies:
        adjacency = (y+i[0], x+i[1])
        # if within bounds of graph
        legit_y = adjacency[0] >= 0 and adjacency[0] < max_y
        legit_x = adjacency[1] >= 0 and adjacency[1] < max_x
        # append adjacencies
        if legit_y and legit_x:
            symbol_indexes.add(adjacency)

# loop through and fill indexes dictionaries
for i in range(len(data)):
    running_chars = ""
    for j in range(len(data[i])):
        curr_char = data[i][j]
        if curr_char.isdigit():
            running_chars += curr_char
        elif curr_char == ".": # if non digit, non symbol
            if running_chars: # if running_chars not empty
                """
                big bug fix:
                making multiple lists so we can double count numbers.
                Put all indexes into list, then append list to dictionary's list
                """
                word_indexes = []
                for k in range(len(running_chars)):
                    word_indexes.append((i, j-(k+1)))
                if number_indexes.get(running_chars, False):
                    number_indexes[running_chars].append(word_indexes)
                else:
                    number_indexes[running_chars] = [word_indexes]
                running_chars = ""
        elif curr_char != "\n":
            if running_chars: # if running_chars not empty
                word_indexes = []
                for k in range(len(running_chars)):
                    word_indexes.append((i, j-(k+1)))
                if number_indexes.get(running_chars, False):
                    number_indexes[running_chars].append(word_indexes)
                else:
                    number_indexes[running_chars] = [word_indexes]
                running_chars = ""
            symbol_add(i, j)
        else:
            # bug fix for me here: makes sure to check for running chars at end of line
            if running_chars: # if running_chars not empty
                word_indexes = []
                for k in range(len(running_chars)):
                    word_indexes.append((i, j-(k+1)))
                if number_indexes.get(running_chars, False):
                    number_indexes[running_chars].append(word_indexes)
                else:
                    number_indexes[running_chars] = [word_indexes]

# reuse symbol_code() function to make * checking easier
def asterisk_add(y, x):
    adjacency_mult = []
    for i in adjacencies:
        adjacency = (y+i[0], x+i[1])
        # if within bounds of graph
        legit_y = adjacency[0] >= 0 and adjacency[0] < max_y
        legit_x = adjacency[1] >= 0 and adjacency[1] < max_x
        # check amount of adjacencies and add to list
        if legit_y and legit_x:
            for i in number_indexes.keys():
                curr_arr = number_indexes.get(i)
                for j in range(len(curr_arr)):
                    for k in range(len(curr_arr[j])):
                        if curr_arr[j][k] == adjacency:
                            adjacency_mult.append(int(i))
                            number_indexes[i][j] = [] # no double counting
                            break
    if len(adjacency_mult) == 2:
        return adjacency_mult[0]*adjacency_mult[1]
    return 0


# We already have a ton of graph data from the last problem, so let's use it.
for i in range(len(data)):
    for j in range(len(data[i])):
        curr_char = data[i][j]
        if curr_char == "*":
            counter += asterisk_add(i, j)

print(counter)

"""
Tester correctly outputted 467835
Problem correctly outputted 85010461
"""
