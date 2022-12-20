data = [(i,int(line)) for i,line in enumerate(open('input.txt').readlines())]
def decrypt(times, data):
  for orig,n in data*times: data.pop(current := data.index((orig, n))); data.insert((current + n) % len(data), (orig, n))
  return sum(data[([n for _,n in data].index(0) + offset) % len(data)][1] for offset in [1000, 2000, 3000])
print(decrypt(1, data.copy()), decrypt(10, [(i,n*811589153) for i,n in data]))
