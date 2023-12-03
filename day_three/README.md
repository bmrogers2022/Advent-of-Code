# Day 3 Notes

First 2D array graphing problem today. Should be a fun problem but also a significant jump in difficulty.  

Bug one find: extra counting from new line chars, resolved  

Bug two find: can never double count same num, even in different spots  

At this point the solutions are not possible to be considered "beginner friendly" but I am doing my best to make the solutions still intuitive and readable

# Part One
###### Personal difficulty rating = 8

### Solution logic
My first thought is to get each number and store the indexes in a dictionary, then cross reference the indexes with all symbols to add to counter.

### Exceptions to logic
Main issues to deal with here are indexing errors, we should be able to handle this by checking to make sure we don't check indexes out of the bounds of the graph.

# Part Two
###### Personal difficulty rating = 8

### Solution logic
Similar to the last problem, but we will now check every surrounding * symbol for different numbers. Part 2 does not contribute much to the difficulty of this problem, so much like the last problem it recieves the same difficulty rating. My solution was very rushed and readability was somewhat compromised whil also being inefficient, but it is good enough for a star today.

### Exceptions to logic
An annoying case for this problem is if the symbol is mirrored by the same number on either side, making it so a simple set trick won't do