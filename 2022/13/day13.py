import json, itertools as it, math, functools as ft; data = [json.loads(l) for l in open('input.txt').read().splitlines() if l!='']
def compare(left, right):
  if type(left) == int and type(right) == int: return left - right
  for l,r in it.zip_longest(left if type(left)==list else [left], right if type(right)==list else [right]):
    if None in (l,r): return -1 if l == None else 1
    if (v := compare(l, r)) != 0: return v
  return 0
print(sum([i+1 for i in range(len(data)//2) if compare(*data[i*2:i*2+2]) < 0]))
print(math.prod([i+1 for i,p in enumerate(sorted([[[2]],[[6]]]+data, key=ft.cmp_to_key(compare))) if p in [[[2]],[[6]]]]))
