from math import lcm

# variables to make changing between testing and running easy
problem_file = "data.txt"
tester_file = "tester_two.txt"

# put file lines into data
with open(problem_file) as file:
    data = file.readlines()

r_l = data[0][:-1]

# left is first element, right is second
directions = {"L": 0, "R": 1}
network = {}

# add each line of instructions
for i in range(len(data)):
    if "=" in data[i]:
        # dealt with the data in an ugly manner, this just makes keys in format "AAA": ("BBB", "CCC")
        network[data[i][0:3]] = (data[i][7:10], data[i][12:15])

# start at "AAA"
points = [x[0:3] for x in data[2:] if x[2] == "A"]
first_z = []
loop_z = []
steps = 0
done = False

for point in points:
    count = 0
    while point[-1] != "Z":
        point = network[point][directions[r_l[count % len(r_l)]]]
        count += 1
    first_z.append((point, count))

# error in previous solution: logic works, but only for this example
for point in first_z:
    count = point[1] # must keep same point as last time, not reset
    temp = count
    loc = point[0]
    # first step necessary to initiate for loop
    loc = network[loc][directions[r_l[count % len(r_l)]]]
    count += 1
    while loc != point[0]:
        loc = network[loc][directions[r_l[count % len(r_l)]]]
        count += 1
    loop_z.append((loc, count-temp))

# printing both results
print(first_z)
print(loop_z)

for i in range(len(first_z)):
    print(f"{first_z[i][1]} + ({loop_z[i][1]} times some number)" + (" =" if i != len(first_z)-1 else ""))

# Because the first loop and the second loop are equal, we actually can just run lcm on this
answer = 1
for i in range(len(loop_z)):
    answer = lcm(answer, loop_z[i][1])

print(f"answer = {answer}")

"""
Tester correctly outputs 6
Problem correctly outputs 9858474970153
"""
