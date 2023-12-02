# Day One Notes
The way Advent of code generally works is you are given data and you want to write code corresponding to the prompt to pull your answer out of the data. Make sure to save your file after pasting the data into it.

The way I find most convenient to do this is to create a new file ```data.txt``` and paste the input I was given by the Advent of Code website.  

I also like to make a test file ```test.txt``` with the example input they give to test my code.

# Part One
###### Personal difficulty rating = 1

### Solution logic
Day one's problem is straightforward so there is not much to say. My method is to create a counter, put all integers into a list, and add together ```list[0]*10 + list[-1]``` to find the final int to add to counter for each line, before printing counter's final number at the end of the file to get the answer.

### Exceptions to logic
Because each line is said to have a unique calibration number, we know that our list will always have a first and last element so our logic will never break.

# Part Two
###### Personal difficulty rating = 2

### Solution logic
Part two simply asks us to make our implementation work even in the case that the numbers are written out in English rather than as numbers. We will use the same logic as before but with a dictionary in order to convert the strings into the correct integers.

### Exceptions to logic
Because each line is said to have a unique calibration number, we know that our list will always have a first and last element so our logic will never break.
