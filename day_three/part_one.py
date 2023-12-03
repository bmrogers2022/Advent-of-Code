# variables to make changing between testing and running easy
problem_file = "data.txt"
tester_file = "test.txt"

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

# cross reference symbol indexes with number indexes
for i in number_indexes.keys():
    for j in number_indexes.get(i):
        for k in j:
            if k in symbol_indexes:
                counter += int(i)
                break

print(counter)

"""
Tester correctly outputted 4361
335979 is too low, debug
Problem correctly outputted 550064
"""