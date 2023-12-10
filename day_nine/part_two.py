# variables to make changing between testing and running easy
problem_file = "data.txt"
tester_file = "test_two.txt"

# put file lines into data
with open(tester_file) as file:
    data = file.readlines()
    data = [[int(y) for y in x.split()][::-1] for x in data]

answer =  0

# find values of each group
for group in data:
    history_value = 0
    curr_group = group
    not_equal = True
    while not_equal:
        not_equal = False
        diff_value = curr_group[0] - curr_group[1]
        new_group = [diff_value]
        for i in range(2, len(curr_group)):
            temp = diff_value
            diff_value = curr_group[i]-curr_group[i-1]
            if temp != diff_value:
                not_equal = True
            new_group.append(diff_value)
        history_value += curr_group[-1]
        curr_group = new_group
    print(history_value)
    answer += history_value

print(answer)

"""
Tester correctly outputs 5
Problem correctly outputs 1140
"""