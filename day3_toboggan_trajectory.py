# Starting at the top-left corner of your map and following a slope of right 3 and down 1,
# how many trees would you encounter?

with open("adventofcode_day3.txt") as day3_file:
    slope_map = [line.strip() for line in day3_file]

# Start going down the slope at coordinate 0,0.
side = 0
down = 0
trees = 0
pattern_width = len(slope_map[0])
slope_hight = len(slope_map) - 1    # - 1 to convert to index and making sure the last iteration does not fail.

for level in range(slope_hight):
    side += 3    # 3 to the right
    down += 1    # 1 down
    side = side if side < pattern_width else side - pattern_width   # Continue in pattern after initial block.
    if slope_map[down][side] == "#":
        trees += 1
    else:
        pass

print(trees)
