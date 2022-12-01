import numpy as np

def update_top_3(total, top_3):
    for i in range(len(top_3)):
        if total > top_3[i]:
            return top_3[:i] + [total] + top_3[i+1:]
    return top_3

with open("./input.txt") as f:
    max_calories = 0
    calories = []
    top_3 = [0,0,0]
    top_3 = [0 for i in range(3)]
    new_calories = []
    for line in f:
        line = line.strip()
        try:
            item = int(line)
            new_calories.append(item)

        except:
            total = sum(new_calories)
            calories.append(total)
            new_calories = []
                
    sorted_calories = sorted(calories)[::-1]
    print(sorted_calories)
    print(sum(sorted_calories[:3]))
    #print(max_calories)






