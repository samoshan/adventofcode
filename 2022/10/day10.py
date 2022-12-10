X, t, crt, sigs, ln, lines = 1, 0, [], [], -1, open('input.txt').read().splitlines()
for c in range(240):
  if t == 0 and lines[(ln := ln+1)][:4] == 'addx': qv, t = int(lines[ln][5:]), 2
  sigs, crt = sigs + [(c+1)*X], crt + ['#' if abs(c%40 - X) <= 1 else '.']
  if ((t := t-1 if t > 0 else 0) == 0) and qv != None: X, qv = X + qv, None
print(sum([sigs[i-1] for i in range(20,221,40)]), *[''.join(row) for row in [crt[i:i+40] for i in range(0,240,40)]], sep='\n')
