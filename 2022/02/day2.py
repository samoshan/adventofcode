cols = [[ord(x) % 65 % 23 for x in round.split()] for round in open('input.txt').readlines()]
p1 = [shape+1 + (3 if opp == shape else 6 if [1, 2, 0][opp] == shape else 0) for opp, shape in cols]
p2 = [(opp if out==1 else [1, 2, 0][opp] if out==2 else [2, 0, 1][opp])+1 + [0, 3, 6][out] for opp, out in cols]
print(f'Part 1: {sum(p1)}\nPart 2: {sum(p2)}')
