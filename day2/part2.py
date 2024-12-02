def sublists_minus_one(lst):
    result = []
    for i in range(len(lst)):
        result.append(lst[:i] + lst[i+1:])
    return result

def check_safe(report):
    safe = True
    is_positive = True

    if (report[1] - report[0] < 0):
        is_positive = False
    for i in range(0, len(report)-1):
        difference = report[i+1]-report[i]
        if (abs(difference) == 0 or abs(difference) > 3): 
            safe = False
        if (is_positive and difference < 0):
            safe = False
        if (not is_positive and difference > 0):
            safe = False
    return safe

with open('input.txt', 'r') as file: 
    number_safe = 0
    for line in file:
        report = list(map(int, line.split()))
        print(report)
        safe = False
        all_possible = sublists_minus_one(report)
        all_possible.append(report)
        for sub_report in all_possible:
            if(check_safe(sub_report)):
                safe = True
        if safe:
            number_safe += 1
    print(number_safe)