import time

def check_rules(rules_dict, update):
    seen = []
    compliant = True
    for number in update:
        # print(seen)
        if(number in rules_dict):
            rules = rules_dict.get(number)
            for rule in rules:
                if (rule not in seen and rule in update):
                    compliant = False
        seen.append(number)

    # print(compliant)
    # print(update)
    # time.sleep(2)
    return compliant

rules_dict = {}
total = 0
with open('rules/input.txt', 'r') as file: 
    numbers = []
    for line in file:
        pair = line.replace('\n','').split("|")
        pair = list(map(int, pair))
        numbers.append(pair)
    for pair in numbers:
        if (pair[1] in rules_dict):
            rules = rules_dict.get(pair[1])
            rules.append(pair[0])
            rules_dict.update({pair[1]: rules})
        else:
            rules = []
            rules.append(pair[0])
            rules_dict.update({pair[1]: rules})
    # print(rules_dict)
with open('updates/input.txt', 'r') as file:
    lists = []
    noncompliant_updates = []
    for line in file:
        update = line.split(",")
        update = list(map(int, update))
        lists.append(update)
    for update in lists:
        seen = []
        compliant = True
        for number in update:
            # print(seen)
            if(number in rules_dict):
                rules = rules_dict.get(number)
                for rule in rules:
                    if (rule not in seen and rule in update):
                        compliant = False
                        # print("rule " + str(rule) + " before " + str(number) + " violated")
            seen.append(number)
        if (not compliant):
            noncompliant_updates.append(update)
    for update in noncompliant_updates:

        is_fixed = False
        while(not is_fixed) :
            seen = []
            for number in update :
                should_break = False
                if(number in rules_dict):
                    rules = rules_dict.get(number)
                    for rule in rules:
                        if(rule not in seen and rule in update):
                            update.pop(update.index(number))
                            update.append(number)
                            should_break = True
                            break
                
                seen.append(number)
            if (check_rules(rules_dict, update)): 
                is_fixed = True
        mid_index = int(len(update)/2)
        # print(update)
        total += update[mid_index]
    print(total)