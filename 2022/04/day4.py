pairs = [[{*range(a,b+1)} for a,b in map(lambda l: map(int, l.split('-')), p.split(','))] for p in open('input.txt').readlines()]
print(f'Part 1: {sum(a <= b or b <= a for a,b in pairs)}\nPart 2: {sum(len(a & b) > 0 for a,b in pairs)}')
