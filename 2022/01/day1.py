with open('input.txt') as f:
  calories = sorted([sum([int(y) for y in x.split()]) for x in f.read().split('\n\n')], reverse=True)
  print(f'Part 1: {calories[0]}\nPart 2: {sum(calories[0:3])}')
