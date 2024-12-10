import time
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


with open('input.txt', 'r') as fileObject: 
    input = []
    disk = []
    files = []
    spaces = []
    files_and_spaces = []
    for line in fileObject:
        input = list(map(int, list(line.rstrip())))
    # print(input)
    total_space = 0
    for i in range(len(input)):
        total_space += input[i]
        if(i % 2 == 0):
            # even is file
            fileId = int(i / 2)
            fileSize = input[i]
            fileObject = {}
            fileObject["fileId"] = fileId
            fileObject["fileSize"] = fileSize
            files.append(fileObject)
            files_and_spaces.append(fileObject)
            # print("read file with id " + str(fileId) + " and size " + str(fileSize) )
        else:
            spaceSize = input[i]
            spaceObject = {}
            spaceObject["storedFiles"] = []
            spaceObject["remainingSpace"] = spaceSize
            spaces.append(spaceObject)
            files_and_spaces.append(spaceObject)
            # print("read empty space with size " + str(fileSize) )
    real_total = 0


    for fileObject in reversed(files) :
        
        fileSize = fileObject["fileSize"]
        # print("moving file")
        # print(fileObject["fileId"])
        # print("size: " + str(fileSize))
        

        for spaceObject in spaces:
            if (spaceObject["remainingSpace"] >= fileSize) :
                # perform movement of file
                spaceObject["remainingSpace"] -= fileSize
                spaceObject["storedFiles"].append((int(fileObject["fileId"]), fileSize))
                fileObject["fileId"] = -1
                break
            # print("skipping space with size: " + str(spaceObject["remainingSpace"]))
    
    for file_or_space in files_and_spaces: 
        
        if( "fileId" in file_or_space):
            real_total += file_or_space["fileSize"]
        else:
            fileUsage = 0
            for file in file_or_space["storedFiles"]:
                fileUsage += file[1]
            real_total += file_or_space["remainingSpace"] + fileUsage


    print(total_space)
    print(real_total)

    # for spaceObject in spaces:
    #     print(spaceObject["storedFiles"])
    for file_or_space in files_and_spaces: 
        
        if( "fileId" in file_or_space):
            for i in range(file_or_space["fileSize"]):
                disk.append(file_or_space["fileId"])
        else:
            for file in file_or_space["storedFiles"]:
                for i in range(0, file[1]):
                    disk.append(file[0])
            if (file_or_space["remainingSpace"] > 0):
                for i in range(0, file_or_space["remainingSpace"]):
                    disk.append(-1)

    checksum = 0
    for i in range(len(disk)):
        if(disk[i] != -1):
            checksum += disk[i] * i

    print(len(disk))

    # for b in disk:
    #     if(b == -1):
    #         print(".", end="")
    #         continue
    #     print(str(b), end = "")
    # print("")
    # print("")
    print(checksum)