with open('input.txt', 'r') as file: 
    first = []
    second = []
    for line in file:
        ids = line.split()
        first.append(int(ids[0]))
        second.append(int(ids[1]))
    sum = 0
    for i in range(0, len(first)):
        sum = sum + abs(first[0]-second[0])
    print(sum)