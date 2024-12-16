import time

stone_dict = {}


def expand_stone(stone):
    new_stones = []

    if (stone in stone_dict):
        return stone_dict[stone]
    

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
    stone_dict[stone] = new_stones
    
    return new_stones
def do_blinks(stones, blinks, should_print):
    original_blinks = blinks
    before = time.time()

    while blinks > 0:
        if should_print:
            print("blink " + str(int(abs(blinks - original_blinks))) + " / " + str(original_blinks))
            print("in " + str(time.time() - before))
            before = time.time()
        new_stones = []
        for stone in stones:
            new_stones.extend(expand_stone(stone))
        stones = [str for str in new_stones if str != ""]
        blinks -= 1
        # print(stones)
    return stones

with open('input.txt', 'r') as file: 
    stones = []
    for line in file:
        for number in line.split(" "):
            stones.append(number)
    # print(stones)
    stones = do_blinks(stones, 25, True)
    more_stones = []
    print("sub stones level 1")
    for stone in stones:
        more_stones.append(do_blinks([stone], 25, False))
    print("sub stones level 2")
    total = 0
    for stoneList in more_stones: 
        for s in stoneList:
            total += len(do_blinks([stone], 25, False))



    # total = 0
    # total_stones = len(stones)
    # stone_index = 0
    # for stone in stones:
    #     if(stone_index % 1000 == 0):
    #         print(str(stone_index) + " / " + str(total_stones) +" substones processed")
    #     stone_index += 1
    #     total += len(do_blinks([stone], 33, False))

    print(total)

    #  use a TREEEEEEE