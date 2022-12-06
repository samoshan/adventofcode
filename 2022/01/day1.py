print(*[(calories:=sorted([sum(map(int, x.split())) for x in open('input.txt').read().split('\n\n')]))[-1], sum(calories[-3:])])
