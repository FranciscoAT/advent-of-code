import sys

overlap_inches = set()
used_inches = set()
patterns = []
intact = []

with open(sys.argv[1], 'r') as pattern_file:
    for pattern in pattern_file:
        new_pattern = pattern.rstrip().split(' ')
        intact.append(True)
        point = new_pattern[2].replace(':', '').split(',')
        dim = new_pattern[3].split('x')
        new_pattern = [int(x) for x in (point + dim)]
        patterns.append(new_pattern)

for pattern in patterns:
    init_x = pattern[0]
    init_y = pattern[1]
    width = pattern[2]
    height = pattern[3]
    for x in range(init_x, init_x + width):
        for y in range(init_y, init_y + height):
            new_pos = (x, y)
            if new_pos in used_inches:
                used_inches.remove(new_pos)
                overlap_inches.add(new_pos)
            elif new_pos not in used_inches and new_pos not in overlap_inches:
                used_inches.add(new_pos)

for index, pattern in enumerate(patterns):
    init_x = pattern[0]
    init_y = pattern[1]
    width = pattern[2]
    height = pattern[3]
    for x in range(init_x, init_x + width):
        for y in range(init_y, init_y + height):
            new_pos = (x, y)
            if new_pos in overlap_inches:
                intact[index] = False

print(intact.index(True) + 1)