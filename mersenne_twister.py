# Heavily inspired by https://github.com/yinengy/Mersenne-Twister-in-Python/
# with slight modifications.

w, n, m, r = 32, 624, 397, 31
a = 0x9908B0DF
u, d = 11, 0xFFFFFFFF
s, b = 7, 0x9D2C5680
t, c = 15, 0xEFC60000
l = 18
f = 1812433253

MT = [0 for i in range(n)]
index = n+1
lower_mask = 0x7FFFFFFF
upper_mask = 0x80000000

def mt_seed(seed):
  MT[0] = seed
  for i in range(1, n):
    temp = f * (MT[i-1] ^ (MT[i-1] >> (w-2))) + i
    MT[i] = temp & 0xffffffff

def extract_number():
  global index
  if index >= n:
    twist()
    index = 0

  y = MT[index]
  y = y ^ ((y >> u) & d)
  y = y ^ ((y << s) & b)
  y = y ^ ((y << t) & c)
  y = y ^ (y >> l)

  index += 1
  return y & 0xffffffff

def twist():
  for i in range(n):
    x = (MT[i] & upper_mask) + (MT[(i+1) % n] & lower_mask)
    xA = x >> 1
    if (x % 2) != 0:
      xA ^= a
    MT[i] = MT[(i + m) % n] ^ xA

if __name__ == '__main__':
  mt_seed(0)
  print(list(extract_number() for _ in range(20)))
