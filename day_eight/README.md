# Day 8 Notes
Really the best intermediate type problem here so far. I wasn't a fan because it would have been much harder if lcm didn't work, which would have been totally feasible if the loop didn't loop back onto itself.

# Part One
###### Personal difficulty rating = 2

### Solution logic
Simply create a map of where to go, then go the direction we are instructed to go. Brute force method.

# Part Two
###### Personal difficulty rating = 4

### Solution logic
Brute forcing no longer works here (I tried). To account for this, I will find all starting points and save the length of the loops they must go through to get back to their Zs. Once I have this info, I can use math to find when they intersect. As it turns out, the time it takes to get to the Z the first time and the second time are both the same, which means the loop loops back on itself and we can just take the least common multiple of all of the loop numbers to get our answer.
