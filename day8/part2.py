with open('input.txt', 'r') as file: 
    first = []
    second = []
    for line in file:
        ids = line.split()
        first.append(int(ids[0]))
        second.append(int(ids[1]))
    sum = 0
    for i in range(0, len(first)):
        search_value = first[i]
        found_number = 0
        for j in range(0, len(first)):
            if (search_value == second[j]):
                found_number += 1
        # print("found " + str(found_number) + " of " + str(search_value))
        sum += found_number * search_value
    print(sum)