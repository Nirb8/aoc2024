with open('input.txt', 'r') as file: 
    number_safe = 0
    for line in file:
        report = list(map(int, line.split()))
        print(report)
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
        if safe:
            number_safe += 1
    print(number_safe)