# variables to make changing between testing and running easy
problem_file = "data.txt"
tester_file = "test.txt"

# put file lines into data
with open(problem_file) as file:
    """
    Worth mentioning this is a different way to collect the data than usual.
    The goal here is to make our work easier later by making each line a list
    of strings, starting after "Card x:". Data is now a list of lists.
    """
    data = [f.split()[2:] for f in file.readlines()]

counter = 0

# conduct logic on each line
for line in data:
    # using sets because it is faster and I don't think repeat nums are allowed
    lucky_nums = set()
    winning_nums = set()
    is_second_half = False

    for num in line:
        if num.isdigit():
            if is_second_half:
                winning_nums.add(num)
            else:
                lucky_nums.add(num)
        else:
            is_second_half = True

    # Reference README for logic
    counter += int(2**(len(lucky_nums.intersection(winning_nums))-1))

print(counter)

"""
Tester correctly outputs 13
Problem correctly outputs 32001
"""