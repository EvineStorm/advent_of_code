# To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the
# corrupted database) and the corporate policy when that password was set.
# How many passwords are valid according to their policies?

policies_and_passwords = {}
correct_passwords = 0

with open("adventofcode_day2.txt") as day2_file:
    for line in day2_file:
        (key, val) = line.strip().rsplit(" ", 1)
        key = key.strip(":")
        policies_and_passwords[key] = val


def check_password(policy, password):
    (permitted_occurrence, letter) = policy.split()
    (occurrence_min, occurrence_max) = permitted_occurrence.split("-")
    occurrence_min = int(occurrence_min)
    occurrence_max = int(occurrence_max)
    occurrence = password.count(letter)
    if occurrence_min <= occurrence <= occurrence_max:
        global correct_passwords
        correct_passwords += 1
        print(correct_passwords)
    else:
        pass


for key, val in policies_and_passwords.items():
    check_password(key, val)

print(correct_passwords)