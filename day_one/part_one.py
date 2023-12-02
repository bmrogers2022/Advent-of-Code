# variables to make changing between testing and running easy
problem_file = "data.txt"
tester_file = "test.txt"

# This is my favorite way to take input for Advent
with open(problem_file) as file:
    data = file.readlines()

"""
data should contain a list of lines now, in format ["str1", "str2", "str3"]
"""

counter = 0

# add calibration values for each line
for line in data:
    nums = []

    # iterate through each character
    for c in line:
        if c.isdigit():
            nums.append(int(c))

    # adds the first int to the 10s place and the last to the 1s place
    calibration_value = nums[0]*10 + nums[-1]

    counter += calibration_value

print(counter)

"""
Tester correctly outputted 142
Problem correctly outputted 53334
"""
