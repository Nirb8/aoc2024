
def check_string_for_xmas(line):
    return line.count("XMAS") + line.count("SAMX")

def extract_lr_diagonals(lines):
    lr_diagonals = [""] * (len(lines[0]) - 1)
    for line in lines:
        line.replace('\n','')
        lr_diagonals.insert(0, "")
        for i in range(0, len(line)):
            lr_diagonals[i] += line[i]
    return lr_diagonals

def extract_rl_diagonals(lines):
    lr_diagonals = [""] * (len(lines[0]) - 1)
    for line in lines:
        line.replace('\n','')
        lr_diagonals.append("")
        for i in range(0, len(line)):
            lr_diagonals[len(lr_diagonals)-i-1] += line[len(line)-i-1]
    return lr_diagonals

def string_reverse(str):
    return str[::-1]

with open('input.txt', 'r') as file: 
    total_xmas = 0
    lines = []
    for line in file:
        lines.append(line)
    
    # check horizontal
    total_horizontal = 0
    for line in lines:
        total_horizontal += check_string_for_xmas(line)
    print(total_horizontal)
    total_xmas += total_horizontal
        
    # check vertical
    verticals = [""] * len(lines[0])
    for i in range(len(lines)):
        for line in lines:
            verticals[i] += line[i]
    for line in verticals:
        total_xmas += check_string_for_xmas(line)

     # check diagonal (left->right)
    lr_diagonals = extract_lr_diagonals(lines)
    for diagonal in lr_diagonals:
        total_xmas += check_string_for_xmas(diagonal)
    
    # check diagonal (right->left)
    rl_diagonals = extract_rl_diagonals(verticals)
    for diagonal in rl_diagonals:
        total_xmas += check_string_for_xmas(diagonal)

    print(total_xmas)
     
