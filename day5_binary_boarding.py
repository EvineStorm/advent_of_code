# As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?

def row(front_back):
    plane_rows = list(range(0, 128))
    for letter in front_back:
        if letter == 'F':  # Keep lower half
            plane_rows = plane_rows[0:(len(plane_rows) // 2)]
        elif letter == 'B':
            plane_rows = plane_rows[(len(plane_rows) // 2):]
    return plane_rows[0]


def column(left_right):
    plane_columns = list(range(0, 8))
    for letter in left_right:
        if letter == 'L':  # keep lower half
            plane_columns = plane_columns[0:(len(plane_columns) // 2)]
        elif letter == 'R':  # Keep upper half
            plane_columns = plane_columns[(len(plane_columns) // 2):]
    return plane_columns[0]


with open("adventofcode_day5.txt") as day5_file:
    all_seat_ids = []
    for line in day5_file:
        boarding_pass = line.strip()
        my_row = row(boarding_pass[0:7])
        my_column = column(boarding_pass[-3:])
        seat_id = int(my_row) * 8 + int(my_column)
        all_seat_ids += [seat_id]
        all_seat_ids.sort()

print(all_seat_ids[-1])

# Your seat should be the only missing boarding pass in your list. What is the ID of your seat?
# Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

for index, seat in enumerate(all_seat_ids):
    if index == 0:  # Skip the first
        pass
    else:
        if seat - all_seat_ids[index-1] == 2:
            print('My seatnumber is: ' + str(seat-1))
            break
        else:
            pass
