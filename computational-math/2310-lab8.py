import math


# Problem 1
def trap(f, a, b, n):
  deltax = (b - a) / n
  sum = f(a) + f(b)
  if (a > b):
    print("a must be less than b.")
    return
  elif (n < 0):
    print("n must be a positive number.")
    return
  else:
    for i in range(1, n):
      sum += 2 * f(a + i * deltax)
    result = deltax * sum / 2
    print("The approximate value of the integral using Trapezoid method with",
          n, "subintervals is", result)


def sinpi(x):
  return math.sin(x)


# Problem 2
trap(sinpi, 0, math.pi, 10)
trap(sinpi, 0, math.pi, 100)
trap(sinpi, 0, math.pi, 1000)


# Problem 3
def tanpi(x):
  return 4 / (1 + (x**2))


trap(tanpi, 0, 1, 6814)


# Problem 4
def simpsons(f, a, b, n):
  deltax = (b - a) / n
  sum = f(a) + f(b)
  if (a > b):
    print("a must be less than b.")
    return
  elif (n < 0):
    print("n must be a positive number.")
    return
  elif (n & 2 == 1):
    print("n must be an even integer.")
    return
  else:
    for i in range(1, n):
      if i % 2 == 1:
        sum += 4 * f(a + i * deltax)
      else:
        sum += 2 * f(a + i * deltax)
    result = (deltax / 3) * sum
    print("The approximate integral using Simpson's rule using", n,
          "subintervals is", result)


# Problem 5
simpsons(sinpi, 0, math.pi, 10)
simpsons(sinpi, 0, math.pi, 100)

# Problem 6
# I get a weird smaller answer for 15 intervals
# 16 is the minimum needed using this algorithm
simpsons(tanpi, 0, 1, 16)
