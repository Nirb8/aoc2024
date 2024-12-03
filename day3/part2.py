import re

def clean_inputs(raw):
    cleaned_string = ""

    dont_strings = raw.split("don't()")
    # print(dont_strings)
    for dont in dont_strings:
        dont_list = dont.split("do()")
        # print(dont_list)
        dont_list = dont_list[1:] # trim first element
        cleaned_string += ''.join(dont_list)
    # print(cleaned_string)
    return cleaned_string

with open('input.txt', 'r') as file:
    pattern = "mul\\(\\d+,\\d+\\)"
    matches = []

    total = 0

    buffer = "do()"
    for line in file:
        buffer += line

    cleaned_input = clean_inputs(buffer)
    commands = re.findall(pattern, cleaned_input)
    matches.extend(commands)
    # print(matches)
    number_pattern = "mul\\((\\d+),(\\d+)\\)"
    for candidate in matches:
        match = re.match(number_pattern, candidate)
        if match:
            first = int(match.group(1))
            second = int(match.group(2))
            total += first * second
    print(total)
