def print_node(node):
    node_value = str(node["value"])
    print(node_value + " ->", end="")
    for connectedNode in node["list"]:
        connectedNodeValue = str(connectedNode["value"])
        print(connectedNodeValue + " ,", end="")
    print("")

def score_trail(node):
    next_nodes = []
    search_for = 1
    next_nodes = find_next_nodes(node, search_for)
    while(search_for < 9):
        search_for += 1
        new_nodes = []
        if(len(next_nodes) > 0):
            for pathNode in next_nodes:
                # print_node(pathNode)
                new_nodes.extend(find_next_nodes(pathNode, search_for))
        next_nodes = new_nodes
    foundPositions = []
    for finalPathNode in next_nodes:
        pos = finalPathNode["position"]
        if(pos not in foundPositions) :
            foundPositions.append(pos)
        
    return len(foundPositions)


def find_next_nodes(node, value):
    next_nodes = []
    for list_node in node["list"]:
        if(list_node["value"] == value):
            next_nodes.append(list_node)
    return next_nodes

with open('input.txt', 'r') as file: 
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
    # print(mapped_area)
    for i in range(0, len(mapped_area)):
        for j in range(0, len(mapped_area[0])):
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

    # for node_list in mapped_area:
    #     for node in node_list:
    #         node_value = str(node["value"])
    #         print(node_value + " ->", end="")
    #         for connectedNode in node["list"]:
    #             connectedNodeValue = str(connectedNode["value"])
    #             print(connectedNodeValue + " ,", end="")
    #         print("")
    trailheads = []
    for node_list in mapped_area:
        for node in node_list:
            if(node["value"] == 0):
                trailheads.append(node)
    total = 0
    for head in trailheads:
        # print("scoring trail")
        print_node(head)
        total += score_trail(head)
        
    print(total)
