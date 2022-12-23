data=open('input.txt').readlines(); elves={complex(x,y) for x in range(len(data[0])) for y in range(len(data)) if data[y][x]=='#'}
checks,dif,rnd,prop = [[-1j,1-1j,-1-1j],[1j,1+1j,-1+1j],[-1,-1-1j,-1+1j],[1,1-1j,1+1j]], lambda nums: int(max(nums)-min(nums))+1, 1, {}
while any(any(elf+dir in elves for dir in [-1j,1-1j,1,1+1j,1j,-1+1j,-1,-1-1j]) for elf in elves):
  for elf in [elf for elf in elves if any(elf+dir in elves for dir in [-1j,1-1j,1,1+1j,1j,-1+1j,-1,-1-1j])]:
    dir = next((check[0] for check in checks if all(elf+dir not in elves for dir in check)), 0)
    if dir!=0: prop={e:d for e,d in prop.items() if d!=dest} if (dest:=elf+dir) in prop.values() else prop | {elf: dest}
  elves, checks, rnd, prop = elves - set(prop.keys()) | set(prop.values()), checks[1:]+[checks[0]], rnd+1, {}
  if rnd-1 == 10: print(dif([c.real for c in elves]) * dif([c.imag for c in elves]) - len(elves))
print(rnd)
