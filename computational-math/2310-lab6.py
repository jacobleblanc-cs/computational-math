import math

# Problem 1

# Setting initial conditions for S_2 and P_1
S = 1
P = 2
# This loop should be calculating the equations given by the book. However I'm getting insane results...
for i in range(2, 21):
  S = S / (2 + (2 * (math.sqrt(1 - S))))
  P = 2**(i) * (math.sqrt(S))
  print("P =", P, ". Error is", abs(math.pi - P))


# Problem 3
def deriv(f, x):
  h = 0.5
  est = 0
  oldEst = 1  # Need to track last estimate for our condition on the while loop
  while (abs(oldEst - est) > 0.000001):
    # When two answers are within 10^-6 of each other, break the loop
    oldEst = est
    est = (f(x + h) - f(x - h)) / (2 * h)
    h = h / 2
  print("The derivative at " + str(x) + " is " + str(est))


# Here i've defined three functions to test my derivative estimator on
def testFn(x):
  return math.sqrt(x)


def testFn1(x):
  return x**3


def testFn2(x):
  return math.sin(x)**2 / math.log(math.sqrt(x))


deriv(testFn, 9)  # Should print 1/6
deriv(testFn1, 3)  # Should print 27
deriv(testFn2, 2)  # This is a wacky integral but I trust the results
