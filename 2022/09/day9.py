from operator import add,sub; knots, visited, dirs = [(0,0),]*10, [{(0,0)},{(0,0)}], {'L':(-1,0),'U':(0,-1),'R':(1,0),'D':(0,1)}
for d, n in [((l := line.split(' '))[0], int(l[1])) for line in open('input.txt').read().splitlines()]:
  for _ in range(n):
    knots[0] = tuple(map(add, knots[0], dirs[d]))
    for i,knot in enumerate(knots[1:],1):
      if abs(knot[0]-knots[i-1][0]) > 1 or abs(knot[1]-knots[i-1][1]) > 1:
        knots[i] = tuple(map(add, knot, map(lambda x: 0 if x==0 else x/abs(x), map(sub, knots[i-1], knot))))
    list(map(lambda v, k: v.add(knots[k]), visited, [1,-1]))
print(*map(len, visited))
