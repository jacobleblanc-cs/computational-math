import math

##################
#   PROBLEM 1    #
##################


def deriv4(f, x0):
  h = 1 / 16
  x = x0
  tol = 10**-6
  est = 0
  new_est = 0
  diff = 1
  while (diff > tol):
    new_est = (1 / (h**4)) * (f(x + (2 * h)) - (4 * f(x + h)) + (6 * f(x)) -
                              (4 * f(x - h)) + f(x - (2 * h)))
    print("h =", h, ", approx =", new_est)
    diff = abs(est - new_est)
    h = h / 2
    est = new_est
  return est

def test(x):
  return math.exp(x)

print("Test function, should return e:", deriv4(test, 1))

##################
#     End #1     #
##################

#
#
#

##################
#   PROBLEM 2    #
##################

# Part a
print("\n\n")
print("#2 Part A")

def twoA(x):
  return ((x**6) - (x**2) + 1)


# Value of twoA's fourth derivative is 360x^2

twoAapprox = deriv4(twoA, 0)
print("\n")
twoAapprox1 = deriv4(twoA, 1)
print("The approximate value of the fourth derivative at x = 0 is", twoAapprox)
print("The approximate value of the fourth derivative at x = 1 is",
      twoAapprox1)

# Part b
print("\n\n")
print("#2 Part B")

# Approximated values from print outputs:
# h = 1/16 : approx = 0.46875
# h = 1/32 , approx = 0.1171875
# h = 1/64 , approx = 0.029296875
# h = 1/128 , approx = 0.00732421875
# h = 1/256 , approx = 0.0018310546875
abs16 = (0 - 0.46875)
abs32 = (0 - 0.1171875)
abs64 = (0 - 0.029296875)
abs128 = (0 - 0.00732421875)
abs256 = (0 - 0.0018310546875)

ratio1 = abs16/abs32
ratio2 = abs32/abs64
ratio3 = abs64/abs128
ratio4 = abs128/abs256

print("The first four ratios of successive estimates are: ", ratio1, ", ", ratio2, ", ", ratio3, ", ", ratio4)
print("Our error terms are given by h^n. These ratios show us that h^n/((h/2)^n) == 4. In other words, the next term's error is 1/4 the current term's error. So as our h input is divided by 2, the resulting error is divided by 4. Therefore we can conclude that the value of n is 2. Further work is shown in the comments below this print statement.")

# h^n/4 = (h/2)^n
# h^n/4 = h^n/2^n
# 1/4 = 1/2^n
# 2^n = 4
# logbase2(4) = n = 2

# Part c
print("\n\n")
print("#2 Part C")
def sinx(x):
  return math.sin(x)


sinApprox = deriv4(sinx, 0)
print("\n")
sinApproxp2 = deriv4(sinx, math.pi / 2)

print("The approximate value of the fourth derivative of sin(x) at x = 0 is",
      sinApprox)

print(
    "The approximate value of the fourth derivative of sin(x) at x = pi/2 is",
    sinApproxp2)

# The approximation for pi/2 is not accurate due to the fact that our tolerance is too high,
# and thus the loop continues to the point that our h value becomes very small.
# This tiny h value compounds error in the formula, as it is taken to high exponents several times,
# but causes the real error when it is being subtracted from other small numbers,
# which our formula must do to build its approximation.
# This approximation was good here for an accuracy of 10^-5, but we used a tolerance of 10^-6, hence
# the trouble we see here.
