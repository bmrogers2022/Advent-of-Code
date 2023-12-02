# Day Two Notes

Nothing new today, for any logistics questions refer to day one.  
What is notable is the emphasis on parsing input thusfar and how that functions as the hardest part of the problems. I don't enjoy this type of problem very much.

# Part One
###### Personal difficulty rating = 3

### Solution logic
The first step for me in this type of problem is always to separate the relevant data from the stuff we don't care about. To do that in this case we will be using only the data after the first colon. After that we create counters to make sure the amount of cubes is possible and reset counter on semi-colons. We add the IDs (index of line + 1) that have an impossible number of cubes together and print them at the end.

### Exceptions to logic
On the end of the line there is not semi-colon, so we must check counters on end line markers also.

# Part Two
###### Personal difficulty rating = 3

### Solution logic
Given we already answered part 1, this is super easy. We can use Python's built in max function in order to track the most of a color shown on each line and use that to find our answer. I also decided to erase unnecessary bits of code left over from the previous solution. Difficulty rating is only 3 because it includes completing both parts.

### Exceptions to logic
Nothing exceptional to report.