monkeys={m:int(x) if x.isdigit() else tuple(x.split(' ')) for m,x in [l.split(': ') for l in open('input.txt').read().splitlines()]}
parent_of = {monke: next((p for p,x in monkeys.items() if type(x)==tuple and monke in x), None) for monke in monkeys.keys()}
def calc(monke): return int(x if type(x:=monkeys[monke])==int else eval(str(calc(x[0])) + x[1] + str(calc(x[2]))))
def part2(monke):
  (left,op,right) = monkeys[(parent_name := parent_of[monke])]; peer = calc(left if right==monke else right)
  if parent_name == 'root': return peer
  parent = part2(parent_name); order=(parent,peer) if op in '+*' else (peer,parent)
  return eval(str(order[0]) + ({'+':'-', '-':'+', '*':'/', '/':'*'}[op] if op in '+*' or left==monke else op) + str(order[1]))
print(calc('root'), int(part2('humn')))
