# variables to make changing between testing and running easy
problem_file = "data.txt"
tester_file = "test_two.txt"

# This is my favorite way to take input for Advent
with open(problem_file) as file:
    data = file.readlines()

"""
data should contain a list of lines now, in format ["str1", "str2", "str3"]
"""

counter = 0

# hard coding dict because it is more readable
possible_words = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
                  "six": 6, "seven": 7, "eight": 8, "nine": 9}

# add calibration values for each line
for line in data:
    nums = []

    # now we need to keep track of input as we go along to check for words
    word_num = ""

    # iterate through each character
    for c in line:
        if c.isdigit():
            nums.append(int(c))
            word_num = "" # reset word num after adding a num
        else:
            """
            This approach is a little strange, but the idea is
            to keep adding letters to word_num until some word
            is a substring of word_num, effectively finding numbers
            when they occur
            """
            word_num += c
            for word in possible_words.keys():
                if word in word_num:
                    nums.append(possible_words.get(word))
                    word_num = ""
                    break

    # adds the first int to the 10s place and the last to the 1s place
    calibration_value = nums[0]*10 + nums[-1]

    counter += calibration_value

print(counter)

"""
Tester correctly outputted 281
Problem correctly outputted 52834
"""