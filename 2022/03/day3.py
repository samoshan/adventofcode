from string import ascii_letters
with open('input.txt', 'r') as f:
  sacks = [line.strip() for line in f.readlines()]
  part1 = [ascii_letters.index((set(sack[:len(sack)//2]) & set(sack[len(sack)//2:])).pop())+1 for sack in sacks]
  groups = [sacks[x*3:x*3+3] for x in range(len(sacks)//3)]
  part2 = [ascii_letters.index(set.intersection(*map(set, group)).pop())+1 for group in groups]
  print(f'Part 1: {sum(part1)}\nPart 2: {sum(part2)}')
