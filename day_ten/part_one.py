# variables to make changing between testing and running easy
problem_file = "data.txt"
tester_file = "test_two.txt"

# put file lines into data
with open(problem_file) as file:
    data = [x.strip() for x in file.readlines()] # removes \n

# imagine 2d array as a grid, these are the directions
d = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}
pipes = {"|": (d["N"], d["S"]), "-": (d["E"], d["W"]), "L": (d["N"], d["E"]),
         "J": (d["N"], d["W"]), "7": (d["S"], d["W"]), "F": (d["S"], d["E"]),
         ".": (), "S": ()}
max_x = len(data[0]) - 1
max_y = len(data) - 1
visited = set() # don't double count
max_distance = -1
queue = []

# check for index error
def is_legal(pt):
    return 0 <= pt[0] <= max_x and 0 <= pt[1] <= max_y

# find start point
def find_s(map):
    for i in range(len(map)):
        for j in range(len(map)):
            if map[i][j] == "S":
                return [i, j]

# input 2 lists of coords, return next direction or False     
def in_pipe(x, y):
    pipe = data[y[0]][y[1]]
    for i in pipes[pipe]:
        if [y[0] + i[0], y[1] + i[1]] == x:
            for j in pipes[pipe]:
                if j != i:
                    return j # the other direction
    return False

# Start traversing array
l = find_s(data) # location
symbol = data[l[0]][l[1]]

# hard part is starting, after that it just follows a simple direction
for i in d.values():
    new_pipe = [l[0]+i[0], l[1]+i[1]]
    adjacent = in_pipe(l, new_pipe)
    if adjacent:
        queue.append([new_pipe, adjacent, 1])

while queue:
    # get all data from front of queue
    current = queue[0]
    loc = current[0]
    dir = current[1]
    moves = current[2]
    new_pipe = [loc[0]+dir[0], loc[1]+dir[1]]
    pipe_str = str(new_pipe[0]) + str(new_pipe[1])
    next_dir = in_pipe(loc, new_pipe)
    if next_dir:
        queue.append([new_pipe, next_dir, moves+1])
    queue.pop(0)

print(int((moves+1)/2))

"""
Test 1 correctly outputs 4
Test 2 correctly outputs 8
Problem correctly outputs 6754
"""
