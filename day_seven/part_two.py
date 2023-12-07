# using defaultdict for easy occurrence counting
from collections import defaultdict

# variables to make changing between testing and running easy
problem_file = "data.txt"
tester_file = "test.txt"

# put file lines into data
with open(problem_file) as file:
    data = file.readlines()
    data = [x.split() for x in data]

five = []
four = []
full = []
three = []
two = []
one = []
high = []

# I apologize for this, I don't want to write each value out
cards = "J23456789TQKA"
card_comp = {card: value for value, card in enumerate(cards)}

"""
We will check these functions in order from greatest to least so we
don't need to check if a hand is also five of a kind if it is three of a kind
or anything similar to that, only that it fulfills the minimum condition
"""

def is_five_of_a_kind(hand):
    hand_dict = defaultdict(int)
    for card in hand:
        if card != "J":
            hand_dict[card] += 1
    return len(hand_dict.values()) <= 1

def is_four_of_a_kind(hand):
    hand_dict = defaultdict(int)
    hand = sorted(hand, key=lambda x: [card_comp[card] for card in x], reverse=True)
    for card in hand:
        if card == "J":
            highest_freq = ("", 0)
            for k in hand_dict.keys():
                if hand_dict[k] > highest_freq[1]:
                    highest_freq = (k, hand_dict[k])
            hand_dict[highest_freq[0]] += 1
        else:
            hand_dict[card] += 1
    return 4 in hand_dict.values()

def is_full_house(hand):
    hand_dict = defaultdict(int)
    hand = sorted(hand, key=lambda x: [card_comp[card] for card in x], reverse=True)
    print(hand)
    for card in hand:
        if card == "J":
            highest_freq = ("", 0)
            for k in hand_dict.keys():
                if hand_dict[k] > highest_freq[1]:
                    highest_freq = (k, hand_dict[k])
            hand_dict[highest_freq[0]] += 1
        else:
            hand_dict[card] += 1
    return len(hand_dict.values()) == 2

def is_three_of_a_kind(hand):
    hand_dict = defaultdict(int)
    hand = sorted(hand, key=lambda x: [card_comp[card] for card in x], reverse=True)
    for card in hand:
        if card == "J":
            highest_freq = ("", 0)
            for k in hand_dict.keys():
                if hand_dict[k] > highest_freq[1]:
                    highest_freq = (k, hand_dict[k])
            hand_dict[highest_freq[0]] += 1
        else:
            hand_dict[card] += 1
    return 3 in hand_dict.values()

def is_two_pair(hand):
    hand_dict = defaultdict(int)
    hand = sorted(hand, key=lambda x: [card_comp[card] for card in x], reverse=True)
    for card in hand:
        if card == "J":
            highest_freq = ("", 0)
            for k in hand_dict.keys():
                if hand_dict[k] > highest_freq[1]:
                    highest_freq = (k, hand_dict[k])
            hand_dict[highest_freq[0]] += 1
        else:
            hand_dict[card] += 1
    return len(set(hand)) == 3 and 2 in hand_dict.values()

def is_one_pair(hand):
    hand_dict = defaultdict(int)
    hand = sorted(hand, key=lambda x: [card_comp[card] for card in x], reverse=True)
    for card in hand:
        if card == "J":
            highest_freq = ("", 0)
            for k in hand_dict.keys():
                if hand_dict[k] > highest_freq[1]:
                    highest_freq = (k, hand_dict[k])
            hand_dict[highest_freq[0]] += 1
        else:
            hand_dict[card] += 1
    return len(hand_dict.values()) == 4

# else return high card

"""
The cleaner way to do this would be to map each function to corresponding list,
then do something like:
for i in range(len(functions)):
    if functions[i][0](hand[0]):
        functions[i][1].append(hand)
        break
The reason I chose not to do this is because it could create more complexities later
on and in general I want my code to be as simple visually as possible.
"""

def place_hand(hand):
    if is_five_of_a_kind(hand[0]):
        five.append(hand)
    elif is_four_of_a_kind(hand[0]):
        four.append(hand)
    elif is_full_house(hand[0]):
        full.append(hand)
    elif is_three_of_a_kind(hand[0]):
        three.append(hand)
    elif is_two_pair(hand[0]):
        two.append(hand)
    elif is_one_pair(hand[0]):
        one.append(hand)
    else:
        high.append(hand)

for i in range(len(data)):
    hand = data[i]
    place_hand(hand)

# sort according to high cards
five.sort(key=lambda x: [card_comp[card] for card in x[0]], reverse=True)
four.sort(key=lambda x: [card_comp[card] for card in x[0]], reverse=True)
full.sort(key=lambda x: [card_comp[card] for card in x[0]], reverse=True)
three.sort(key=lambda x: [card_comp[card] for card in x[0]], reverse=True)
two.sort(key=lambda x: [card_comp[card] for card in x[0]], reverse=True)
one.sort(key=lambda x: [card_comp[card] for card in x[0]], reverse=True)
high.sort(key=lambda x: [card_comp[card] for card in x[0]], reverse=True)

sorted_hands = five + four + full + three + two + one + high

winnings = 0
number_of_hands = len(sorted_hands)
for i in range(number_of_hands):
    winnings += (int(sorted_hands[i][1])*(number_of_hands-i))

print(winnings)

"""
Tester correctly outputs 5905
Problem correctly outputs 249631254
"""
