def expand_stone(stone):
    new_stones = []
    if (stone == "0"):
        new_stones.append("1")
        return new_stones
    if (len(stone) % 2 == 0):
        # print("last char of " + stone)
        # is even, should split
        middle = int(len(stone) / 2)
        new_stones.append(stone[0:middle])
        second_stone = stone[middle:].lstrip("0")
        if second_stone == "":
            second_stone = "0"
        new_stones.append(second_stone)
    else:
        new_stones.append(str(int(stone) * 2024))
    return new_stones

with open('input.txt', 'r') as file: 
    stones = []
    for line in file:
        for number in line.split(" "):
            stones.append(number)
    # print(stones)
    blinks = 75
    
    while blinks > 0:
        new_stones = []
        for stone in stones:
            new_stones.extend(expand_stone(stone))
        stones = [str for str in new_stones if str != ""]
        blinks -= 1
        # print(stones)
    print(len(stones))