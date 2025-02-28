import math


def bisect(f, a, b, tol):
  midpt = (a + b) / 2
  iteration = 1
  while (abs(f(midpt)) > tol):
    if (f(a) * f(midpt) < 0):
      b = midpt
      midpt = (a + b) / 2
      iteration += 1
    elif (f(b) * f(midpt) < 0):
      a = midpt
      midpt = (a + b) / 2
      iteration += 1
    else:
      print("There is no root on this interval")

  print("The approximate solution from bisection is", midpt,
        "which was found in", iteration, "iterations.")


def testFn(x):
  return math.exp(x) - x - 2


def testFn1(x):
  return x**3 - x - 2


bisect(testFn, -1, 2, 0.0001)
bisect(testFn1, -5, 5, 0.001)


def regfal(f, a, b, tol):
  xnaught = ((a * f(b)) - (b * f(a))) / (f(b) - f(a))
  iteration = 1
  originalA = a
  originalB = b
  while (abs(f(xnaught)) > tol and a >= originalA and b <= originalB):
    if (f(xnaught) < 0):
      a = xnaught
      xnaught = ((a * f(b)) - (b * f(a))) / (f(b) - f(a))
      iteration += 1
    elif (f(xnaught) > 0):
      b = xnaught
      xnaught = ((a * f(b)) - (b * f(a))) / (f(b) - f(a))
      iteration += 1
    else:
      print("There is no root on this interval")

  print("The approximate solution from regula falsi is", xnaught,
        "which was found in", iteration, "iterations.")


regfal(testFn, -1, 2, 0.0001)
regfal(testFn1, -5, 5, 0.001)
regfal(
    testFn1, -20, -19, 0.01
)  # This shouldn't be working but it manages to figure it out anyway lol. Gotta fix the range


# This isn't quite functional yet
def Newton(f, fp, x0, x1, TOL, N):
  i = N
  while i > 0:
    if ((x1 - x0) < TOL):
      return x1
    elif (abs(x1) > 10**20):
      return x1
    elif (fp < 10**-7):
      return x1
    else:
      x1 = x0 - f(x0) / fp(x0)
    i = i - 1
  return x1


def prob4Fn(x):
  return math.cos(30 * x) + (x**3) - (3 * (x**2)) + 0.8


bisect(prob4Fn, 2, 4, 0.01)
regfal(prob4Fn, 2, 4, 0.01)
#Newton(prob4Fn,something,3,)


def centroid(r, theta):
  return (2 * r * math.sin(theta)) / 3 * theta


# Finding equation of polynomial with root=sqrt(4+cuberoot(3))
# x = sqrt(4+(3)^(1/3))
# x^2 = 4+3^(1/3)
# (x^2 - 4)^3 = 3
# x^6 - 12x^4 + 48x^2 - 64 = 3
# x^6 - 12x^4 + 48x^2 - 67 = 0
def rootEqn(x):
  return x**6 - 12 * x**4 + 48 * x**2 - 67


regfal(rootEqn, 2, 3, 0.001)
#Newton(rootEqn,)
