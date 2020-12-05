# Find the two entries that sum to 2020; what do you get if you multiply them together?

with open("adventofcode_day1.txt") as day1_file:
    expense_report = day1_file.read().splitlines()
    expense_report = [int(i) for i in expense_report]
    day1_file.close()

