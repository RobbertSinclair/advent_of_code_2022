
with open("./input.txt") as f:
    lines = f.readlines()
    i = 0
    part1Stacks = {num: [] for num in range(1, (len(lines[0]) // 4) + 1)}
    while lines[i] != "\n":
        for j in range(0, len(lines[i]), 4):
            part1Container = lines[i][j:j+3]
            if '[' in part1Container.strip():
                part1Stacks[(j // 4) + 1].insert(0, part1Container)
        i += 1
    part2Stacks = {key: part1Stacks[key].copy() for key in part1Stacks}
    i += 1
    for i in range(i, len(lines)):
        line = [int(char) for char in lines[i].strip().split(" ") if char.isdigit()]
        moved = 0
        print(line)
        part2Stack = []
        while moved < line[0]:
            part1Container = part1Stacks[line[1]].pop()
            part2Container = part2Stacks[line[1]].pop()
            part2Stack.insert(0, part2Container)
            part1Stacks[line[2]].append(part1Container)
            moved += 1
        part2Stacks[line[2]] = part2Stacks[line[2]] + part2Stack
    print(f"PART 1 - {[part1Stacks[key][-1] for key in part1Stacks]}")
    print(f"PART 2 - {[part2Stacks[key][-1] for key in part2Stacks]}")
    
