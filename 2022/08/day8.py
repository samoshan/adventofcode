from math import prod; grid = [[*map(int, row)] for row in open('input.txt').read().splitlines()]
perimeter, cells = ((w := len(grid[0])) + (h := len(grid))) * 2 - 4, [(x,y) for x in range(1,w-1) for y in range(1,h-1)]
views = [(grid[y][x],[grid[y][x-1::-1],[d[x] for d in grid[y-1::-1]],grid[y][x+1:],[d[x] for d in grid[y+1:]]]) for x,y in cells]
print(perimeter + sum(any(all(oh<h for oh in line) for line in lines) for h,lines in views))
print(max([prod([next((i+1 for i,oh in enumerate(line) if oh>=h), len(line)) for line in lines]) for h,lines in views]))
