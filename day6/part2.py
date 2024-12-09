from enum import IntEnum
import time
import os
import copy

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class Direction(IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

guardDirection = 0

walked_nodes = []
clean_map = []

def find_guard(mapped_area):
    for i in range(len(mapped_area)):
        for j in range(len(mapped_area[0])):
            if(mapped_area[i][j] == '^'):
                return (i, j)
    return (-1, -1)
def print_map(mapped_area):
    for line in mapped_area:
        for char in line:
            print(char, end='')
        print("")
def walk(mapped_area, guard_pos, guardDirection) :
    # mark current position
    mapped_area[guard_pos[0]][guard_pos[1]] = "X"
    new_pos = calculate_delta(guardDirection, guard_pos)
    if (new_pos[0] == -1 or new_pos[1] == -1):
        return new_pos
    if (new_pos[0] == len(mapped_area) or new_pos[1] == len(mapped_area[0])):
        return (-1, -1)
    if (mapped_area[new_pos[0]][new_pos[1]] == "#"):
        return guard_pos
    return new_pos
def walk_special(mapped_area, guard_pos, guardDirection) :
    # print_map(mapped_area)
    new_pos = calculate_delta(guardDirection, guard_pos)
    # print(guard_pos)
    # print("to")
    # print(new_pos)
    if (new_pos[0] == -1 or new_pos[1] == -1):
        return new_pos
    if (new_pos[0] == len(mapped_area) or new_pos[1] == len(mapped_area[0])):
        return (-1, -1)
    if (mapped_area[new_pos[0]][new_pos[1]] == "#"):
        return guard_pos
    return new_pos

def calculate_delta(direction, current_position) :
    if(direction == Direction.NORTH) :
        return (current_position[0] - 1, current_position[1])
    
    if(direction == Direction.EAST) :
        return (current_position[0], current_position[1] + 1)
    
    if(direction == Direction.SOUTH) :
        return (current_position[0] + 1, current_position[1])
    
    if(direction == Direction.WEST) :
        return (current_position[0], current_position[1] - 1)
    
with open('input.txt', 'r') as file: 
    mapped_area = []
    for line in file:
        mapped_area.append(list(line.rstrip()))
    clean_map = copy.deepcopy(mapped_area)
    guard_pos = find_guard(mapped_area)
    blacklist_start_pos = guard_pos
    # print_map(mapped_area)
    guardDirection = Direction.NORTH
    while (guard_pos[0] != -1 and guard_pos[1] != -1) :
        old_pos = (guard_pos[0], guard_pos[1])
        guard_pos = walk(mapped_area, guard_pos, guardDirection)
        if(old_pos == guard_pos) :
            guardDirection =  (guardDirection + 1) % 4
            # print(guardDirection)
    
    for i in range(len(mapped_area)):
        for j in range(len(mapped_area[0])):
             if (mapped_area[i][j] == "X"):
                 if((i, j) != blacklist_start_pos):
                    walked_nodes.append((i, j))
    temp_reality = []
    total_loops = 0
    loopNumber = 0
    for node in walked_nodes: 
        cls()
        print(str(loopNumber) + " / " + str(len(walked_nodes)) + "   " + str(total_loops) + " / " + str(len(walked_nodes)))
        loopNumber += 1
        # reset guard
        guard_pos = find_guard(clean_map)
        # perform simulation
        temp_reality = copy.deepcopy(clean_map)
        temp_reality[node[0]][node[1]] = "#"
        # print_map(temp_reality)
        # print("")
        guardDirection = Direction.NORTH
        is_loop = False
        visited_map = {}
        while (guard_pos[0] != -1 and guard_pos[1] != -1) :
            old_pos = (guard_pos[0], guard_pos[1])
            guard_pos = walk_special(temp_reality, guard_pos, guardDirection)
            if(old_pos == guard_pos) :
                guardDirection = (guardDirection + 1) % 4
            else :
                if((old_pos in visited_map)):
                    visited_map[old_pos] += 1
                else:
                    visited_map[old_pos] = 1
            if (5 in visited_map.values()):
                is_loop = True
                break
            # time.sleep(1)
        if(is_loop) :
            total_loops += 1
    print(total_loops)