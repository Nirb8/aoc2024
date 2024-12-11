import time
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def print_disk(disk):
    for b in disk:
        if(b == -1):
            print(".", end="")
            continue
        print(str(b), end = "")
    print("")
def find_blank(disk, blank_size, fileOriginalIndex):
    # print("search blank")
    # print(str(blank_size))
    blank_index = -1
    current_blank_size = 0
    for i in range(0,  fileOriginalIndex + blank_size):

        if (disk[i] < 0):
            current_blank_size += 1
        if (disk[i] >= 0):
            current_blank_size = 0
        if (current_blank_size >= blank_size):
            blank_index = i - blank_size + 1
            break

    # print("found at")
    # print(str(blank_index))
    return blank_index
            
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
    files = []
    for line in file:
        input = list(map(int, list(line.rstrip())))
    print(input)
    for i in range(len(input)):
        if(i % 2 == 0):
            # even is file
            fileId = int(i / 2)
            fileSize = input[i]
            files.append((fileId, fileSize, len(disk)))
            for j in range(fileSize):
                disk.append(fileId)
        else:
            spaceSize = input[i]
            for j in range(spaceSize):
                disk.append(-1)
    fileCount = 0
    for file in reversed(files):

        if(fileCount % 100 == 0):
            cls()
            print("checked file " + str(fileCount) +" / " + str(len(files)))
        fileCount += 1
        # print_disk(disk)
        fileId = file[0]
        fileSize = file[1]
        fileOriginalIndex = file[2]
        blank_index = find_blank(disk, fileSize, fileOriginalIndex)
        if(blank_index == -1):
            continue
        for i in range(0, fileSize):
            disk[blank_index + i] = fileId
            disk[fileOriginalIndex + i] = -1
        

    checksum = 0
    for i in range(len(disk)):
        if(disk[i] != -1):
            checksum += disk[i] * i


    # 6421724836639 incorrect

    while(disk.pop() == -1):
        pass
    print(disk)

    print(checksum)