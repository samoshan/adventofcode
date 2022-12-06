print(*[n+next(x for x in range(len(data)) if len(set(data[x:x+n]))==n) for n in [4,14] if (data:=open('input.txt').read())])
