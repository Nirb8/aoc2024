with open('test.txt', 'r') as file: 
    mapped_area = []
    i = 0
    for line in file:
        row = []
        j = 0
        for number in list(map(int, list(line.rstrip()))):
            node = {}
            node["value"] = number
            node["position"] = (i, j)
            node["list"] = []
            row.append(node)
            j += 1
        i += 1
        mapped_area.append(row)

    for i in range(len(mapped_area)):
        for j in range(len(mapped_area[0])):
            # construct adjacency list for each node
            current_node = mapped_area[i][j]
            # Assuming mapped_area is a 2D array (list of lists)
            rows = len(mapped_area)
            cols = len(mapped_area[0])

            if i + 1 < rows:
                current_node["list"].append(mapped_area[i + 1][j])
            if i - 1 >= 0:
                current_node["list"].append(mapped_area[i - 1][j])
            if j + 1 < cols:
                current_node["list"].append(mapped_area[i][j + 1])
            if j - 1 >= 0:
                current_node["list"].append(mapped_area[i][j - 1])

    print(mapped_area)


