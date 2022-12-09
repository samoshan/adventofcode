knots, visited, dirs = [0]*10, [{0}, {0}], {'L': -1, 'U': -1j, 'R': 1, 'D': 1j}
for d, n in [((l := line.split(' '))[0], int(l[1])) for line in open('input.txt').read().splitlines()]:
  for _ in range(n):
    knots[0] = knots[0] + dirs[d]
    for i,knot in enumerate(knots[1:],1):
      if abs(knot-knots[i-1]) >= 2:
        knots[i] = knot + complex(((c := knots[i-1]-knot).real>0)-(c.real<0),(c.imag>0)-(c.imag<0))
    list(map(lambda v, k: v.add(knots[k]), visited, [1,-1]))
print(*map(len, visited))
