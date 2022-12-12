width,height = len((data:=open('input.txt').read().splitlines())[0]), len(data)
(start,end),grid = map(lambda c: ((i:=''.join(data).find(c))%width,i//width),'SE'), [l.replace('S','a').replace('E','z') for l in data]
def bfs(start, target, f):
  queue, visited = [[start]], {start}
  while queue:
    if (p := (path := queue.pop(0))[-1]) == target or grid[(cy := p[1])][(cx := p[0])] == target: return len(path)-1
    for x, y in [(cx-1,cy), (cx,cy-1), (cx+1,cy), (cx,cy+1)]:
      if (x,y) not in visited and 0<=x<width and 0<=y<height and ((ord(grid[y][x]) - ord(grid[cy][cx]))*f <= 1):
        queue, visited = queue + [path + [(x, y)]], visited | {(x, y)}
print(bfs(start, end, 1), bfs(end, 'a', -1))
