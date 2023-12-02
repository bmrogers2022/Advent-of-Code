# variables to make changing between testing and running easy
problem_file = "data.txt"
tester_file = "test.txt"

# put file lines into data
with open(tester_file) as file:
    data = file.readlines()

# initialize counters
id_counter = 0
red_counter = 0
blue_counter = 0
green_counter = 0

# rules
max_red = 12
max_green = 13
max_blue = 14

# checks if too many cubes of any one color
def valid_count(r, g, b):
    return True if r <= max_red and g <= max_green and b <= max_blue else False

# check validity of each line
for i in range(len(data)):
    # reset counters each new line
    red_counter = 0
    blue_counter = 0
    green_counter = 0

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
            elif "green" in game_pulls[j]:
                green_counter += cube_counter
            elif "blue" in game_pulls[j]:
                blue_counter += cube_counter

            # check if new item is connected or separate
            if ";" or "\n" in game_pulls[j]:
                if not valid_count(red_counter, green_counter, blue_counter):
                    game_possible = False

                # reset counters  
                red_counter = 0
                green_counter = 0
                blue_counter = 0
    
    if game_possible:
        id_counter += (i+1)

print(id_counter)      

"""
Tester correctly outputted 8
Problem correctly outputted 2207
"""
