
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
    for line in f:
        line = line.strip()
        mid = len(line) // 2
        containers = [line[:mid], line[mid:]]
        first_container_set = set(containers[0])
        for item_type in first_container_set:
            if item_type in containers[1]:
                total += calculate_priority(item_type)
                break
    print(total)