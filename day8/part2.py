def print_map(mapped_area):
    for line in mapped_area:
        for char in line:
            print(char, end='')
        print("")
def get_unique_pairs(pairs_list):
    pair_pairs = []
    for pair in pairs_list :
        for pair_two in pairs_list :
            current_pair = (pair, pair_two)
            if (current_pair not in pair_pairs and (current_pair[0], current_pair[1]) not in pair_pairs):
                pair_pairs.append(current_pair)
    return pair_pairs

with open('input.txt', 'r') as file: 
    city_map = []
    signal_beacons = {}
    antinodes = {}
    for line in file:
        city_map.append(list(line.rstrip()))
    for i in range(0, len(city_map)):
        for j in range(0, len(city_map[0])):
            tile = city_map[i][j]
            if(tile != '.'):
                if(tile in signal_beacons):
                    signal_beacons[tile].append((i, j))
                else:
                    locations = []
                    locations.append((i, j))
                    signal_beacons[tile] = locations
    for key in signal_beacons.keys():
        values = signal_beacons[key]
        pair_pairs = get_unique_pairs(values)
        for pair_pair in pair_pairs:
            first_pos = pair_pair[0]
            second_pos = pair_pair[1]
            if (first_pos == second_pos) :
                continue
            first_dist = first_pos[0] - second_pos[0]
            second_dist = first_pos[1] - second_pos[1]
            for i in range(- len(city_map), len(city_map)):
                possible_antinode = (first_pos[0] + (first_dist * i), first_pos[1] + (second_dist * i))
                if (possible_antinode in antinodes) :
                    antinodes[possible_antinode] += 1
                else :
                    antinodes[possible_antinode] = 1

    toDel = []
    for antinode in antinodes:
        if (antinode[0] < 0 or antinode[1] < 0 or antinode[0] >= len(city_map) or antinode[1] >= len(city_map[0])):
            toDel.append(antinode)
    for antinode in toDel:
        del antinodes[antinode]
    for antinode in antinodes:
        print(antinode)
        city_map[antinode[0]][antinode[1]] = "#"
    print(signal_beacons)
    print_map(city_map)
    print(len(antinodes))