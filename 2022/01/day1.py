calories = sorted([sum(map(int, x.split())) for x in open('input.txt').read().split('\n\n')])
print(f'Part 1: {calories[-1]}\nPart 2: {sum(calories[-3:])}')
