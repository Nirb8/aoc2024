
def string_reverse(str):
    return str[::-1]

with open('input.txt', 'r') as file: 
    total_xmas = 0
    lines = []
    for line in file:
        lines.append(line)
    for i in range(1, len(lines)-1):
        to_check = []
        search_index = 0
        while True:
            index = lines[i].find("A", search_index)
            # print("found")
            # print(index)
            if index == -1:
                break
            to_check.append(index)
            search_index = index + 1
        for index in to_check:
            if (index >= len(lines[i]) - 1) :
                continue
            top_left = lines[i - 1][index - 1]
            top_right = lines[i - 1][index + 1]
            bottom_left = lines[i + 1][index - 1]
            bottom_right = lines[i + 1][index + 1]

            lr_mas =  (top_left == "S" and bottom_right == "M") or (top_left == "M" and bottom_right == "S")
            rl_mas = (top_right == "S" and bottom_left == "M") or (top_right == "M" and bottom_left == "S")
            if (lr_mas and rl_mas): 
                total_xmas += 1
    print("total")
    print(total_xmas)