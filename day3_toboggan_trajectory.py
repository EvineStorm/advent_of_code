# Starting at the top-left corner of your map and following a slope of right 3 and down 1,
# how many trees would you encounter?

with open("adventofcode_day3.txt") as day3_file:
    slope_map = [line.strip() for line in day3_file]

# Start going down the slope at coordinate 0,0.
side = 0
down = 0
trees = 0
pattern_width = len(slope_map[0])
slope_hight = len(slope_map)

while down < len(slope_map) - 1:
    side += 3    # 3 to the right
    down += 1    # 1 down
    side = side if side < pattern_width else side - pattern_width   # Continue in pattern after initial block.
    if slope_map[down][side] == "#":
        trees += 1
    else:
        pass

print(trees)

# What do you get if you multiply together the number of trees encountered on each of the listed slopes?
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
trees_on_slope = []

for slope in slopes:
    side = 0
    down = 0
    trees = 0
    while down < len(slope_map) - 1:
        side += slope[0]
        down += slope[1]
        side = side if side < pattern_width else side - pattern_width   # Continue in pattern after initial block.
        encounter = slope_map[down][side]
        if encounter == "#":
            trees += 1
        else:
            pass
    trees_on_slope += [trees]


def multiply_list(my_list):
    result = 1
    for x in my_list:
        result = result * x
    return result


print(trees_on_slope)
print(multiply_list(trees_on_slope))
