# Count the number of valid passports - those that have all required fields.
# Treat cid as optional. In your batch file, how many passports are valid?

# Count the number of valid passports - those that have all required fields and valid values.
# Continue to treat cid as optional. In your batch file, how many passports are valid?

import re


def matches_rule(field, passport_value):
    if field == "byr":
        return True if 1920 <= int(passport_value) <= 2002 else False
    elif field == "iyr":
        return True if 2010 <= int(passport_value) <= 2020 else False
    elif field == "eyr":
        return True if 2020 <= int(passport_value) <= 2030 else False
    elif field == "hgt":
        if (passport_value[-2:] == "in") and (59 <= int(passport_value[:-2]) <= 76):
            return True
        elif (passport_value[-2:] == "cm") and (150 <= int(passport_value[:-2]) <= 193):
            return True
        else:
            return False
    elif field == "hcl":
        return True if re.match('^#[a-f0-9]{6}', passport_value) else False
    elif field == "ecl":
        return True if passport_value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] else False
    elif field == "pid":
        return True if re.match('^[0-9]{9}', passport_value) else False


def check_passport(passport):
    expected_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    if all(fields in passport.keys() for fields in expected_fields):
        return True
    else:
        return False


def validate_passport(passport):
    counter = 0
    expected_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for field in expected_fields:
        if field in passport:
            if matches_rule(field, passport.get(field)):
                counter += 1
    if counter == 7:
        return True
    else:
        return False


with open("adventofcode_day4.txt") as day4_file:
    valid_passports = 0
    passport = {}
    for line in day4_file:
        if line != "\n":
            passport_line = line.strip().split()
            for item in passport_line:
                (key, value) = item.split(":")
                passport[key] = value
        else:
            if validate_passport(passport):
                valid_passports += 1
            passport = {}
    if validate_passport(passport):  # For last passport of file there is no new line, so I check it here
        valid_passports += 1

print(valid_passports)


#   189 is te hoog -> 188 is goed? waarom heb ik dat laatste if statement voor check_passport nodig en voor validate_password niet?