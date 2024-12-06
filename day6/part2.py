from enum import IntEnum
import time
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class Direction(IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

guardDirection = 0

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
    guard_pos = find_guard(mapped_area)
    # print_map(mapped_area)
    guardDirection = Direction.NORTH
    while (guard_pos[0] != -1 and guard_pos[1] != -1) :
        old_pos = (guard_pos[0], guard_pos[1])
        guard_pos = walk(mapped_area, guard_pos, guardDirection)
        if(old_pos == guard_pos) :
            guardDirection =  (guardDirection + 1) % 4
            print(guardDirection)
    x_count = 0
    for line in mapped_area:
        x_count += line.count("X")
    print(x_count)