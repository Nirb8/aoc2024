import re

with open('input.txt', 'r') as file:
    pattern = "mul\\(\\d+,\\d+\\)"
    matches = []

    total = 0
    for line in file:
        commands = re.findall(pattern, line)
        matches.extend(commands)
    print(matches)
    number_pattern = "mul\\((\\d+),(\\d+)\\)"
    for candidate in matches:
        match = re.match(number_pattern, candidate)
        if match:
            first = int(match.group(1))
            second = int(match.group(2))
            total += first * second
    print(total)
