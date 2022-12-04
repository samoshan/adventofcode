sacks, letters = open('input.txt').read().splitlines(), ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
p1 = [letters.index((set(sack[:len(sack)//2]) & set(sack[len(sack)//2:])).pop()) for sack in sacks]
p2 = [letters.index(set.intersection(*map(set, sacks[x*3:x*3+3])).pop()) for x in range(len(sacks)//3)]
print(f'Part 1: {sum(p1)}\nPart 2: {sum(p2)}')
