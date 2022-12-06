
def find_marker_char(string, length):
    marker_char = -1
    i = 0
    marker_found = False
    while not marker_found and i < len(string):
        potential_marker = string[i:i+length]
        marker_set = set(potential_marker)
        if len(potential_marker) == len(marker_set):
            marker_char = i+length
            marker_found = True   
        i += 1
    return marker_char


with open("./input.txt") as f:
    line = f.read().strip()
    print(f"PART 1 - {find_marker_char(line, 4)}")
    print(f"PART 2 - {find_marker_char(line, 14)}")