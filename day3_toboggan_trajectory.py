# Starting at the top-left corner of your map and following a slope of right 3 and down 1,
# how many trees would you encounter?

def is_tree(char):
    if char == "#":
        True
    else:
        False


with open("adventofcode_day3.txt") as day3_file:
    for line in day3_file:
        line = line.strip()

