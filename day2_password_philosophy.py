# To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the
# corrupted database) and the corporate policy when that password was set.
# How many passwords are valid according to their policies?

def check_password_policy1(policy, password):
    (permitted_occurrence, letter) = policy.split()
    (occurrence_min, occurrence_max) = permitted_occurrence.split("-")
    occurrence_min = int(occurrence_min)
    occurrence_max = int(occurrence_max)
    occurrence = password.count(letter)
    if occurrence_min <= occurrence <= occurrence_max:
        return True
    else:
        return False


correct_passwords = 0
with open("adventofcode_day2.txt") as day2_file:
    for line in day2_file:
        (key, val) = line.strip().rsplit(" ", 1)
        key = key.strip(":")
        if check_password_policy1(key, val):
            correct_passwords += 1
        else:
            pass

print("There are " + str(correct_passwords) + " correct passwords!")

# How many passwords are valid according to the new interpretation of the policies?


def check_password_policy2(policy, password):
    (permitted_indices, letter) = policy.split()
    (first_index, second_index) = permitted_indices.split("-")
    first_index = (int(first_index)) - 1    # Correct for array count starting at 0
    second_index = (int(second_index)) - 1
    if (password[first_index] == letter and password[second_index] != letter) or \
            (password[first_index] != letter and password[second_index] == letter):
        return True
    else:
        return False


correct_passwords = 0
with open("adventofcode_day2.txt") as day2_file:
    for line in day2_file:
        (key, val) = line.strip().rsplit(" ", 1)
        key = key.strip(":")
        if check_password_policy2(key, val):
            correct_passwords += 1
        else:
            pass

print("There are " + str(correct_passwords) + " correct passwords!")

