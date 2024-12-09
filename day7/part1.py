def generate_binary_strings(n):
  if n == 0:
    return [""]
  else:
    prev_strings = generate_binary_strings(n - 1)
    return ["0" + s for s in prev_strings] + ["1" + s for s in prev_strings]

with open('input.txt', 'r') as file: 
    total = 0
    for line in file:
        args = line.rstrip().split(":")
        target = int(args[0])
        # numbers = list(map(int, args[1].split(" ")))
        numbers = list(map(int, args[1].strip().split(" ")))
        binary_strings = generate_binary_strings(len(numbers) - 1)
        # print(target)
        # print(numbers)
        is_solution = False
        for binary in binary_strings:
            current = numbers[0]
            index = 1
            binlist = list(map(int, list(binary)))
            for b in binlist:
                if (b == 0) :
                    # do add
                    current += numbers[index]
                if (b == 1) :
                    current *= numbers[index]
                index += 1
                if current > target :
                    break
            if current == target:
                is_solution = True
                break
        if (is_solution):
            total += target
    print(total)
