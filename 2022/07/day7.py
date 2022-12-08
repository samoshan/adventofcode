from collections import defaultdict; cd, sizes = [], defaultdict(lambda: 0)
for line in open('input.txt').read().splitlines():
  if line.startswith('$ cd'):
    cd = cd[:-1] if (dir := line[5:]) == '..' else cd + [dir]
  elif line[0].isnumeric():
    for x in range(len(cd)):
      sizes['/'.join(cd[:x+1])] += int(line.split(' ')[0])
print(sum(s for s in sizes.values() if s <= 100000), min(s for s in sizes.values() if s >= max(sizes.values())-40000000))
