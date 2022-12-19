data,offsets = [(*map(int, l.split(',')),) for l in open('input.txt').readlines()], [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
print(sum(sum([(x+i,y+j,z+k) not in data for i,j,k in offsets]) for x,y,z in data)); faces,queue,visited = 0, [(-1,-1,-1)], {(-1,-1,-1)}
while queue:
  x,y,z = queue.pop(0)
  for new_coord in [(x+i,y+j,z+k) for i,j,k in offsets if all(-1<=p<21 for p in [x+i,y+j,z+k])]:
    if new_coord in data: faces += 1
    elif new_coord not in visited: queue, visited = queue + [new_coord], visited | {new_coord}
print(faces)
