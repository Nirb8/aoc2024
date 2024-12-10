def check_compact(disk):
    is_compact = True
    fileZone = True
    for f in disk:
        if( f < 0): 
            fileZone = False
        if( f >= 0 and fileZone is False):
            is_compact = False
    return is_compact
def do_compact_step(disk):
    fileIndex = 0
    fileId = 0
    spaceIndex = 0
    for i in range(len(disk)-1, 0, -1):
        if(disk[i] >= 0):
            fileIndex = i
            fileId = disk[i]
            break
    for i in range(0, len(disk)):
        if(disk[i] < 0):
            spaceIndex = i
            break

    disk[spaceIndex] = fileId
    disk[fileIndex] = -1


with open('input.txt', 'r') as file: 
    input = []
    disk = []
    spaces = []
    for line in file:
        input = list(map(int, list(line.rstrip())))
    print(input)
    for i in range(len(input)):
        if(i % 2 == 0):
            # even is file
            fileId = int(i / 2)
            fileSize = input[i]
            for j in range(fileSize):
                disk.append(fileId)
        else:
            spaceSize = input[i]
            for j in range(spaceSize):
                disk.append(-1)
    print(disk)
    while(check_compact(disk) == False):
        do_compact_step(disk)
    print(disk)

    checksum = 0
    for i in range(len(disk)):
        if(disk[i] != -1):
            checksum += disk[i] * i
    print(checksum)