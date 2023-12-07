# variables to make changing between testing and running easy
problem_file = "data.txt"
tester_file = "test.txt"

# put file lines into data
with open(problem_file) as file:
    data = file.readlines()
    data = [[int(y) for y in x.split()[1:]] for x in data]

print(data)

time, distance = data[0], data[1]

output = 1

# for each race
for i in range(len(data[0])):
    ways_to_win = 0
    # brute force every possible strategy
    for j in range(time[i]+1):
        if ((time[i]-j)*j > distance[i]):
            ways_to_win += 1
    output *= ways_to_win

print(output)

"""
tester correctly outputs 288
problem correctly outputs 74698
"""
