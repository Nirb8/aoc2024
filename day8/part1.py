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
            if (current_pair not in pair_pairs):
                pair_pairs.append(current_pair)


with open('test.txt', 'r') as file: 
    city_map = []
    signal_beacons = {}
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
    for key in signal_beacons.keys:
        values = signal_beacons[key]
        pair_pairs = get_unique_pairs(values)
        for pair_pair in pair_pairs:
            first_pos = pair_pair[0]
            second_pos = pair_pair[1]

    print(signal_beacons)
    print_map(city_map)