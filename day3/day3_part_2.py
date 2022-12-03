def calculate_priority(letter):
    ascii_value = ord(letter)
    if ascii_value >= ord('a') and ascii_value <= ord('z'):
        return ascii_value - 96
    elif ascii_value >= ord('A') and ascii_value <= ord('Z'):
        return ascii_value - 38
    else:
        return -1 


with open("./input.txt") as f:
    total = 0
    
    lines = f.readlines()
    groups = [[] for i in range(0, len(lines), 3)]
    group_counter = 0
    for i in range(len(lines)):
        line = lines[i].strip()
        groups[i // 3].append(line)
    current_priority = 0
    for group in groups:
        sets = [set(elf) for elf in group]
        group_badge = list(sets[0].intersection(sets[1], sets[2]))[0]
        total += calculate_priority(group_badge)

                
        
    print(total)