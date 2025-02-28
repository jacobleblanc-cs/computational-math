import math
import numpy

def Simpson(f, a, b, eps, level, level_max):
  level = level+1
  h = b-a
  c = (a+b)/2
  one_simpson = (h*(f(a) + 4*f(c) + f(b)))/6
  d = (a+c)/2
  e = (c+b)/2
  two_simpson = (h*(f(a) + 4*f(d) + 2*f(c) + 4*f(e) + f(b)))/12
  if (level >= level_max):
    result = two_simpson
    return result
  else:
    if(abs(two_simpson-one_simpson) < 15*eps):
      result = two_simpson + (two_simpson-one_simpson)/15
      return result
    else:
      left_simpson = Simpson(f, a, c, eps/2, level, level_max)
      right_simpson = Simpson(f, c, b, eps/2, level, level_max)
      result = left_simpson + right_simpson
  return result

def xcubed(x):
  return math.sin(x**3)

print(Simpson(xcubed, 0, 1, 10**-8, 0, 4))


def Romberg(f, a, b, n):
  R = numpy.zeros((n + 1, n + 1))
  h = b - a
  R[0, 0] = (h / 2) * (f(a) + f(b))
  for i in range(1, n + 1):
    h = h / 2
    sum = 0
    for k in range(1, 2**i, 2):
      sum = sum + f(a + (k * h))
    R[i, 0] = (0.5 * R[i - 1, 0]) + (sum * h)
    for j in range(1, i + 1):
      R[i, j] = R[i, j - 1] + (R[i, j - 1] - R[i - 1, j - 1]) / (4**j - 1)
  print("The final estimate by Romberg integration is:", R[n, n])
  return R


print(Romberg(math.sin, 0, math.pi, 4))

print(Romberg(xcubed, 0, math.pi, 4))