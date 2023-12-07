# Day Seven Notes

Part one of this problem is actually just an easier version I have already programmed, so I am just going to modify some old code I have written. I lean pretty heavy on python builtins here, particularly in part 2. The problem would have been much worse without using builtins so I give it a relatively high difficulty ranking, seeing that my goal here is to make code beginners can easily understand.

# Part One
###### Personal difficulty rating = 3

### Solution logic
Check strength of hand, group into categories, sort using sorted() with a key that corresponds each card num to a value, concatenate all hands together and calculate total winnings. The hardest part of this is the sorting of the hand lists, but I have done this before so I just copied that over and it was no problem

# Part Two
###### Personal difficulty rating = 5

### Solution logic
We are going to use the same method as last time, except we will move J back in our sorting definition and change the algorithms for how we check each hand. To accomplish this we will sort our hand before we return the result, and just add 1 to the highest value numbers when we get a J.
