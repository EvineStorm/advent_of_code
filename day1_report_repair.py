# Find the two entries that sum to 2020; what do you get if you multiply them together?

with open("adventofcode_day1.txt") as day1_file:
    expense_report = day1_file.read().splitlines()
    expense_report = [int(i) for i in expense_report]

for index, entry in enumerate(expense_report):
    for compare_entry in expense_report[(index+1):]:
        # prevents the numbers already added together on previous iterations being checked again
        if entry + compare_entry == 2020:
            print("The answer is: " + str(entry) + " * " + str(compare_entry) + " = "
                  + str(entry * compare_entry) + " !")
        else:
            pass


# In your expense report, what is the product of the three entries that sum to 2020?

for index, first_entry in enumerate(expense_report):
    for second_entry in expense_report[(index+1):]:
        for third_entry in expense_report[(index + 2):]:
            # prevents the numbers already added together on previous iterations being checked again
            if first_entry + second_entry + third_entry == 2020:
                print("The answer is: " + str(first_entry) + " * " + str(second_entry) + " * " +
                      str(third_entry) + " = " + str(first_entry * second_entry * third_entry) + " !")
            else:
                pass
