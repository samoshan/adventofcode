beats, score_p1, score_p2, guide = [1, 2, 0], 0, 0, open('input.txt').read().splitlines()
for round in guide:
  opponent, col2 = [ord(x) - (65 if x < 'X' else 88) for x in round.split(' ')]
  score_p1 += col2 + 1 + (3 if opponent == col2 else 6 if beats[opponent] == col2 else 0)
  my_shape = opponent if col2 == 1 else beats[opponent] if col2 == 2 else beats[beats[opponent]]
  score_p2 += my_shape + 1 + [0, 3, 6][col2]
print(f'Part 1: {score_p1}\nPart 2: {score_p2}')
