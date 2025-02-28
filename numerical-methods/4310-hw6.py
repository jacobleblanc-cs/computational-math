import math
import numpy

# Not working properly right now, need to fix
# Only going to 1 level
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
    if(abs(two_simpson - one_simpson) < 15*eps):
      print("Current level = ", level, "Current value = ", two_simpson, "Current interval = ", h)
      result = two_simpson + ((two_simpson-one_simpson)/15)
    else:
      left_simpson = Simpson(f, a, c, eps/2, level, level_max)
      right_simpson = Simpson(f, c, b, eps/2, level, level_max)
      result = left_simpson + right_simpson
  return result

def x_cubed(x):
  return x**3

print(Simpson(x_cubed, 0, 1, 10**(-8), 0, 10))

def x_fifth(x):
  return x**5

print(Simpson(x_fifth, 0, 1, 10**(-6), 0, 10))

#def gauss4_a_b(f, a, b):
  