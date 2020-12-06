# To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the
# corrupted database) and the corporate policy when that password was set.
# How many passwords are valid according to their policies?

correct_passwords = 0

def check_password(policy, password):
    (permitted_occurrence, letter) = policy.split()
    (occurrence_min, occurrence_max) = permitted_occurrence.split("-")
    occurrence_min = int(occurrence_min)
    occurrence_max = int(occurrence_max)
    occurrence = password.count(letter)
    if occurrence_min <= occurrence <= occurrence_max:
        return True
    else:
        return False


with open("adventofcode_day2.txt") as day2_file:
    for line in day2_file:
        (key, val) = line.strip().rsplit(" ", 1)
        key = key.strip(":")
        if check_password(key, val):
            correct_passwords += 1
        else:
            pass

print("There are " + str(correct_passwords) + " correct passwords!")