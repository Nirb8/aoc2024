def generate_ternary_strings(n):

  if n == 0:
    return [""]

  result = []
  for string in generate_ternary_strings(n - 1):
    for digit in "012":
      result.append(string + digit)

  return result

with open('input.txt', 'r') as file: 
    total = 0
    for line in file:
        args = line.rstrip().split(":")
        target = int(args[0])
        # numbers = list(map(int, args[1].split(" ")))
        numbers = list(map(int, args[1].strip().split(" ")))
        ternary_strings = generate_ternary_strings(len(numbers) - 1)
        # print(target)
        # print(numbers)
        is_solution = False
        for ternary in ternary_strings:
            current = numbers[0]
            index = 1
            terlist = list(map(int, list(ternary)))
            for b in terlist:
                if (b == 0) :
                    # do add
                    current += numbers[index]
                if (b == 1) :
                    current *= numbers[index]
                if (b == 2) :
                    current = int(str(current) + str(numbers[index]))
                index += 1
                if current > target :
                    break
            if current == target:
                is_solution = True
                break
        if (is_solution):
            total += target
    print(total)
