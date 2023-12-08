# variables to make changing between testing and running easy
problem_file = "data.txt"
tester_file = "test.txt"

# put file lines into data
with open(problem_file) as file:
    data = file.readlines()

r_l = data[0][:-1] # don't inlcude newline

# left is first element, right is second
directions = {"L": 0, "R": 1}
network = {}

# add each line of instructions
for i in range(len(data[2:])):
    # dealt with the data in an ugly manner, this just makes keys in format "AAA": ("BBB", "CCC")
    network[data[i][0:3]] = (data[i][7:10], data[i][12:15])

# start at "AAA"
point = "AAA"
steps = 0
while point != "ZZZ":
    direction = directions[r_l[steps % len(r_l)]]
    point = network[point][direction]
    steps += 1

print(steps)

"""
Tester correctly outputs 2
Problem correctly outputs 11567
"""
