import re; import math; data, regex = open('input.txt').read(), r'(\d+(?:, \d+)*)\n.+= (.+)\n.+?(\d+)\n.+(\d)\n.+(\d)'
def day11(rounds, div):
  monkeys = [([*map(int, m[0].split(','))], m[1], *map(int,m[2:])) for m in re.findall(regex, data)]
  counts, lcm = [0]*(len(data.split('\n'))//7), math.lcm(*[monkey[2] for monkey in monkeys])
  for i, (items, op, test, t, f) in rounds * [*enumerate(monkeys)]:
    while items: counts[i]+=1; monkeys[t if (lvl:=eval(op.replace('old',str(items.pop(0))))%lcm//div)%test==0 else f][0].append(lvl)
  return counts
print(*[math.prod(sorted(day11(rounds, div))[-2:]) for rounds, div in [(20,3), (10000,1)]])
