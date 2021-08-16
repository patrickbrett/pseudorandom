def middle_square(seed):
  sq = str(seed ** 2)
  sq = (8 - len(sq)) * '0' + sq[:8]

  middle_four = sq[2:6]
  return int(middle_four)

print(middle_square(4567))

def run_ms(start_seed, n):
  seed = start_seed
  for i in range(n):
    seed = middle_square(seed)
    yield seed

print(list(run_ms(1234, 6)))

