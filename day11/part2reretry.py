from functools import cmp_to_key
import time

stone_dict = {}

def tuple_sort(a, b):
    if not isinstance(a, tuple) and not isinstance(b, tuple):
        return 0
    if isinstance(a, tuple) and not isinstance(b, tuple):
        return 1
    if not isinstance(a, tuple) and isinstance(b, tuple):
        return -1
    if a[1] < b[1]:
        return -1
    if a[1] > b[1]:
        return 1
    if int(a[0]) < int(b[0]):
        return -1
    if int(a[0]) > int(b[0]):
        return 1
    return 0

def generate_closures(seed, blinks_left):

    new_seeds = expand_one_stone(seed)
    if (blinks_left == 0):
        return [1]
    if len(new_seeds) == 1:
        return generate_closures(new_seeds[0], blinks_left - 1)
    if len(new_seeds) == 2:
        closure_list = []
        first = generate_closures(new_seeds[0], blinks_left - 1)
        second = (new_seeds[1], blinks_left - 1)
        closure_list.extend(first)
        closure_list.append(second)
        return closure_list
    
def eval_closure(seed_tuple):
    if not isinstance(seed_tuple, tuple):
        return 1
    seed = seed_tuple[0]
    blinks_left = seed_tuple[1]
    if (blinks_left == 0): 
        return 1
    if (blinks_left == 1):
        seed_list = expand_one_stone(seed)
        return len(seed_list)
    
    if (seed_tuple in stone_dict):
        return stone_dict[seed_tuple]
    
    seed_length = 0
    new_seeds = expand_one_stone(seed)

    if len(new_seeds) == 1:
        seed_length = eval_closure((new_seeds[0], blinks_left - 1))
    else:
        seed_length = eval_closure((new_seeds[0], blinks_left - 1)) + eval_closure((new_seeds[1], blinks_left - 1))
    stone_dict[seed_tuple] = seed_length
    return seed_length

tuple_sort_key = cmp_to_key(tuple_sort)

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
    
    blink_amount = 75
    total = 0
    tuple_list = []
    before = time.time()
    for stone in stones:
        tuple_list.extend(generate_closures(stone, blink_amount))
    tuple_list = sorted(tuple_list, key=tuple_sort_key)
    for stone_tuple in tuple_list:
        total += eval_closure(stone_tuple)
    end = time.time()-before
    print(total)
    print("done in " + str(end) + " seconds")