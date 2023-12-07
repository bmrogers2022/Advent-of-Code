# variables to make changing between testing and running easy
problem_file = "data.txt"
tester_file = "test.txt"

# put file lines into data
with open(problem_file) as file:
    data = file.readlines()
    data = ["".join(x.split()[1:]) for x in data]

print(data)

time, distance = int(data[0]), int(data[1])

ways_to_win = 0
# brute force every possible strategy
for j in range(time+1):
    if ((time-j)*j > distance):
        ways_to_win += 1

print(ways_to_win)

"""
Tester correctly outputs 71503
Problem correctly outputs 
"""
