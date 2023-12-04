# variables to make changing between testing and running easy
problem_file = "data.txt"
tester_file = "test_two.txt"

# put file lines into data
with open(problem_file) as file:
    """
    Worth mentioning this is a different way to collect the data than usual.
    The goal here is to make our work easier later by making each line a list
    of strings, starting after "Card x:". Data is now a list of lists.
    """
    data = [f.split()[2:] for f in file.readlines()]

"""
queue = [i for i in range(len(data))] was too inefficient to work
"""
hashmap = {i: 1 for i in range(len(data))}

counter = 0

# run for each number in hashmap, in sorted order so card nums aren't run twice
for i in range(len(data)):
    # using sets because it is faster and I don't think repeat nums are allowed
    lucky_nums = set()
    winning_nums = set()
    is_second_half = False

    for num in data[i]:
        if num.isdigit():
            if is_second_half:
                winning_nums.add(num)
            else:
                lucky_nums.add(num)
        else:
            is_second_half = True

    # add a card for each matching num * number of cards we have
    for j in range(hashmap[i]):
        for k in range(1, len(lucky_nums.intersection(winning_nums))+1):
            hashmap[i+k] += 1
        counter += 1

print(counter)

"""
Tester correctly outputs 30
Problem correctly outputs 5037841
"""
