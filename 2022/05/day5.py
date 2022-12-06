with open('input.txt') as f: data = f.read().splitlines()
stacks1 = [[*filter(str.isalpha, [data[y][1+4*x] for y in range([l=='' for l in data].index(1)-1)])] for x in range(9)]
instructions, stacks2 = [map(int, line.split(' ')[1::2]) for line in data if 'move' in line], stacks1.copy()
for n, frm, to in instructions:
  stacks1[to-1], stacks1[frm-1] = stacks1[frm-1][n-1::-1] + stacks1[to-1], stacks1[frm-1][n:]
  stacks2[to-1], stacks2[frm-1] = stacks2[frm-1][:n] + stacks2[to-1], stacks2[frm-1][n:]
print(f'Part 1: {"".join([stack[0] for stack in stacks1])}\nPart 2: {"".join([stack[0] for stack in stacks2])}')
