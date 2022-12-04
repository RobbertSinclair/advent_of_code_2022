
def check_assignments(ass1, ass2):
    return ass1[0] >= ass2[0] and ass1[1] <= ass2[1]

def check_assignments_overlap(ass1, ass2):
    return (ass1[0] >= ass2[0] and ass1[0] <= ass2[1]) or (ass1[1] >= ass2[0] and ass1[1] <= ass2[1])

def assignments_fully_contains(elves):
    assignment1, assignment2 = tuple([[int(e) for e in elf.split("-")] for elf in elves])
    return check_assignments(assignment1, assignment2) or check_assignments(assignment2, assignment1)

def assignments_overlap(elves):
    assignment1, assignment2 = tuple([[int(e) for e in elf.split("-")] for elf in elves])
    return check_assignments_overlap(assignment1, assignment2)


with open("./input.txt") as f:
    part1_total = 0
    part2_total = 0
    for line in f:
        line = line.strip()
        elves = line.split(",")
        if assignments_fully_contains(elves):
            part1_total += 1
            part2_total += 1
        elif assignments_overlap(elves):
            part2_total += 1
        
    print(f"PART 1: {part1_total}")
    print(f"PART 2: {part2_total}")