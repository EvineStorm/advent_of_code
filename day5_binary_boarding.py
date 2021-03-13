# As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?

def row(front_back):
    plane_rows = list(range(0, 128))
    for letter in front_back:
        if letter == 'F':  # Keep lower half
            plane_rows = plane_rows[0:(len(plane_rows) // 2)]
        elif letter == 'B':
            plane_rows = plane_rows[(len(plane_rows) // 2):]
    return plane_rows


def column(left_right):
    plane_columns = list(range(0, 8))
    for letter in left_right:
        if letter == 'L':  # keep lower half
            plane_columns = plane_columns[0:(len(plane_columns) // 2)]  # double slash for int
        elif letter == 'R':  # Keep upper half
            plane_columns = plane_columns[(len(plane_columns) // 2):]
    return plane_columns


with open("adventofcode_day5.txt") as day5_file:
    for line in day5_file:
        boarding_pass = line.strip()
        my_row = row(boarding_pass[0:7])
        my_column = column(boarding_pass[-3:])
        seat = my_row, my_column
        print(seat)

