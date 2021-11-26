# Find the sum of the digits.
def multiplication(n):
  og = n
  while n > 1:
    mult = og * (n-1)
    og = mult
    n -= 1
  return addition(mult)

def addition(i):
  add = sum([int(a) for a in str(i)])
  return add

print(multiplication(100))