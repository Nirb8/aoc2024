import time

stone_dict = {}

def find_seed_chart(seed, remainingBlinks):
    for i in range (remainingBlinks, 0, -1):
        seed_tuple = (seed, i)
        if (seed_tuple in stone_dict):
            return (i, stone_dict[seed_tuple])
    return -1


def do_blink(seed_tuple):
    # base case
    if(not isinstance(seed_tuple, tuple)):
        return [seed_tuple]
    seed = seed_tuple[0]
    blinks = seed_tuple[1]
    if(  blinks == 0): 
        return [seed_tuple]
    if(  blinks == 1):
        stone_dict[seed_tuple] = [expand_one_stone(seed)]
        return [expand_one_stone(seed)]
    if(  blinks == 2):
        seed_list = expand_one_stone(seed)
        returned_seeds = []
        for seed in seed_list:
            returned_seeds.extend(expand_one_stone(seed))
        stone_dict[seed_tuple] = returned_seeds
        return returned_seeds
    seed_chart_tuple = find_seed_chart(seed, blinks)

    if (seed_chart_tuple == -1):
        # do one step manually
        new_seeds = expand_one_stone(seed)
        if(len(new_seeds) == 2) :
            stone_dict[seed_tuple] = new_seeds
            returned_seeds = []
            seed_one = (new_seeds[0], blinks-1)
            seed_two = (new_seeds[1], blinks-1)
            returned_seeds.append(seed_one)
            returned_seeds.append(seed_two)
            return returned_seeds
        else:
            stone_dict[seed_tuple] = new_seeds
            return [(new_seeds[0], blinks-1)]


    # we found a seed chart
    used_blinks = seed_chart_tuple[0]
    seed_chart = seed_chart_tuple[1]
    next_seeds = []

    for seed in seed_chart :
        next_seeds.extend(expand_one_stone(seed))
    
    new_seed_tuple = (seed, used_blinks - 1)
    stone_dict[new_seed_tuple] = next_seeds

    final_seeds = []

    for next_seed in next_seeds :
        final_seed_result = (next_seed, blinks - used_blinks - 1)
        final_seeds.append(final_seed_result)
    return final_seeds

def expand_one_stone(stone):
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
    
    blink_amount = 5
    total = 0
    tuple_list = []

    for stone in stones:
        tuple_list.append((stone, blink_amount))
    
    while( True):
        # print(tuple_list)
        # time.sleep(2)
        if(not tuple_list):
            break
        tuple_delta = []
        for t in tuple_list:
            new_t = do_blink(t)
            tuple_delta.extend(new_t)
        clean_tuple_delta = []
        for t in tuple_delta:
            if (isinstance(t, tuple)):
                clean_tuple_delta.append(t)
            else:
                total += 1
        tuple_list = clean_tuple_delta
        
    print(total)
    # print(do_blink("20", 3))