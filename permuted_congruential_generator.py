state = 0x4d595df4d0f33173
multiplier = 6364136223846793005
increment = 1442695040888963407

def rotr32(x, r):
  return x >> r or x << (-r & 31)

def pcg32():
  global state, multiplier, increment

  x = state
  count = x >> 59

  state = x * multiplier + increment
  x ^= x >> 18
  return rotr32(x >> 27, count)

def pcg32_init(seed):
  global state
  state = seed + increment
  pcg32()


if __name__ == '__main__':
  pcg32_init(5129803)
  print(list(pcg32() for _ in range(20)))
