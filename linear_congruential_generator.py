"""
m = modulus
a = multiplier
c = increment
seed = starting value
"""
def lcg(m, a, c, seed):
  return (seed * a + c) % m


def lcg_gen(m, a, c, seed, n):
  for _ in range(n):
    seed = lcg(m, a, c, seed)
    yield seed


print(list(lcg_gen(7829, 378, 2310, 4321, 10)))
