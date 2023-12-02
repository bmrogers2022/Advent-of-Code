# variables to make changing between testing and running easy
problem_file = "data.txt"
tester_file = "test_two.txt"

# put file lines into data
with open(problem_file) as file:
    data = file.readlines()

# initialize counters
power_counter = 0
red_counter = 0
blue_counter = 0
green_counter = 0

# check validity of each line
for i in range(len(data)):
    # reset counters each new line
    red_counter = 0
    blue_counter = 0
    green_counter = 0

    # max counters
    max_red = 0
    max_green = 0
    max_blue = 0

    # variable that keeps track of last cube num
    cube_counter = 0

    """
    split each line, separating each word separated
    by spaces as different strings in an array
    """
    game_pulls = data[i].split()
    game_pulls = game_pulls[2:len(game_pulls)] # remove "Game x:"
    game_possible = True

    # iterate through lines to check pulls
    for j in range(len(game_pulls)):
        # check if number or color
        if game_pulls[j].isdigit():
            cube_counter = int(game_pulls[j])
        else:
            # check color of cube and add to counters
            if "red" in game_pulls[j]:
                red_counter += cube_counter
                max_red = max(red_counter, max_red)
            elif "green" in game_pulls[j]:
                green_counter += cube_counter
                max_green = max(green_counter, max_green)
            elif "blue" in game_pulls[j]:
                blue_counter += cube_counter
                max_blue = max(blue_counter, max_blue)

            # check if new item is connected or separate
            if ";" in game_pulls[j]:
                # reset counters  
                red_counter = 0
                green_counter = 0
                blue_counter = 0
            
            # check end of line
            if j == len(game_pulls)-1:
                power_counter += max_red * max_green * max_blue
    
print(power_counter)

"""
Tester correctly outputted 2286
Problem correctly outputted 62241
"""
