# For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?
with open("adventofcode_day6.txt") as day6_file:
    total_group_answers = []
    sum_group_answers = 0
    for line in day6_file:
        if line != "\n":
            person_answer = line.strip()
            for answer in person_answer:
                if answer not in total_group_answers:
                    total_group_answers += [answer]
        else:
            sum_group_answers += int(len(total_group_answers))
            total_group_answers = []

sum_group_answers += int(len(total_group_answers))
print(sum_group_answers)

# For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?


def split(word):
    return [char for char in word]


with open("adventofcode_day6.txt") as day6_file:
    common_group_answers = [1]
    sum_group_answers = 0
    for line in day6_file:
        if line != "\n":
            person_answer = split(line.strip())
            if common_group_answers == [1]:  # The 1 is a placeholder to differentiate between empty and 'new group' arrays
                common_group_answers = person_answer
            else:
                common_group_answers = list(set(common_group_answers).intersection(person_answer))
        else:
            sum_group_answers += int(len(common_group_answers))
            common_group_answers = [1]


sum_group_answers += int(len(common_group_answers))
print(sum_group_answers)
