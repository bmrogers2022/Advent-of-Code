# Day 4 Notes
The simplicity of these problems is a breath of fresh air after Day 3. This is the best problem of the four so far, especially part 2.

# Part One
###### Personal difficulty rating = 1

### Solution logic
For each line make array of lucky numbers and array of winning numbers, then add ```2^(length of their intersection - 1)``` to counter.

### Exceptions to logic
This method counts the card as being worth .5 points if there are no common numbers, so add a conditional statement to check for that.  
###### note: I opted to use the int function to round down .5 to 0 instead of using a conditional, since the solution looks cleaner

# Part Two
###### Personal difficulty rating = 3

### Solution logic
Initial thought here is to use a queue data structure that starts which each cards index. From there we add cards to the queue based on the amount of matches as instructed, increment counter by one, and pop the top queue element. The only problem I could end up seeing with this logic is the amount of time it could take to run, since it is a brute force technique.  

### Update:  
As anticipated, this technique took too long. To speed it up I will use a dictionary that stores the cards added for each other card.  

### Update two:  
Alright well I was hoping to use a queue but I'll settle on another hash map approach since the input is too large for a queue implementation to work. Logic remains roughly the same, except we go through our hashmap one index at a time using our known knowledge of the elements in there and just do the adding step ```x``` times where x is the value pair of the key

### Exceptions to logic
Exceptions only occur when cards make you copy a card past the table, which is given to be impossible in this problem.
