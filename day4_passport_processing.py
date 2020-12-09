# Count the number of valid passports - those that have all required fields.
# Treat cid as optional. In your batch file, how many passports are valid?

import re


def valid_passport(passport):
    expected_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    field_names = passport.keys()
    if all(fields in field_names for fields in expected_fields):
        return True
    else:
        return False


valid_passports = 0

with open("adventofcode_day4.txt") as day4_file:
    present_passport_fields = {}
    for line in day4_file:
        if line != "\n":
            passport_line = line.strip().split()
            for item in passport_line:
                (key, value) = item.split(":")
                present_passport_fields[key] = value
        else:
            if valid_passport(present_passport_fields):
                valid_passports += 1
            present_passport_fields = {}
    if valid_passport(present_passport_fields):  # For last passport of file there is no new line, so I check it here
        valid_passports += 1

print(valid_passports)

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

# Count the number of valid passports - those that have all required fields and valid values.
# Continue to treat cid as optional. In your batch file, how many passports are valid?


def valid_passport_with_validation(passport):
    expected_fields_with_rules = ["byr", "iyr", "eyr", "hgt", ["hcl", '^#[a-f0-9]{7}'], "ecl", "pid"]
    for fields in passport:

        return True
    else:
        return False


input = "Enter an input string:"
m = re.match('\d{5}\Z',input)

if m:
    print("True")
else:
    print("False")