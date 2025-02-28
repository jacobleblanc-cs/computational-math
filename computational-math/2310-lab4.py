def f(x):
  return ((x - 1)**6)


def fexpanded(x):
  return (x**6 - 6 * x**5 + 15 * x**4 - 20 * x**3 + 15 * x**2 - 6 * x + 1)


def fnested(x):
  #return ((((((x - 6) * (x + 15)) * (x - 20)) * (x + 15)) * (x - 6)) * (x + 1))
  return ((x + 1) * ((x - 6) * ((x + 15) * ((x - 20) * ((x + 15) * (x - 6))))))


for i in range(1, 8):
  x = 1 + 10**(-i)
  print(x, f(x), fexpanded(x), fnested(x))

# This loop prints out all of our functions with an input of 1 + 10^-index.
# For the first loop, this means x = 1.1
# For the second, x = 1.01
# Etc until we reach x = 1.0000001 when i=7


## Problem 4 ##
def fexpandederror(x):
  return (x**6 - 6 * x**5 + 15 * x**4 - 19.9 * x**3 + 15 * x**2 - 6 * x + 1)


print(fexpanded(1.1), fexpandederror(1.1))

## Problem 5 ##
sum = 0.0
for i in range(1, 10001):
  sum = sum + 1.0 / i**2
print("sum forward", sum)

sumRev = 0.0
for i in reversed(range(1, 10001)):
  sumRev = sumRev + 1.0 / i**2
print("sum backward", sumRev)

sum20 = 1.6448340718480597698

absErrFor = abs(sum20 - sum)
absErrRev = abs(sum20 - sumRev)
print("The absolute error of the forward sum is", absErrFor)
print("The absolute error of the reversed sum is", absErrRev)


## Problem 6 ##
def g(x):
  return (4 * x * (1 - x))


p = 1.0 / 7.0
for i in range(1, 41):
  p = g(p)
print("first p is ", p)
p2 = 1.0 / 7.0 + 10**(-12)
for i in range(1, 41):
  p2 = g(p2)
print("second p is ", p2)

# These loops are taking the variables p and p2 respectively, and then running
# them through the function g(x) 40 times. This shows a difference in
# compounding error between two starting points which vary only by
# 10^(-12)
