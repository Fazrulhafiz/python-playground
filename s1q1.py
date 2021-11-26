# Using NO BUILT IN LIBRARIES, write a program that satisfies the following problem:
# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800, and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!
def multiplication(n): # n =10
  og = n
  while n > 1:
    mult = og * (n-1) # 90 = 10 x 9
    og = mult
    n -= 1
  return addition(mult)

def addition(i):
  add = sum([int(a) for a in str(i)])
  return add

print(multiplication(10))