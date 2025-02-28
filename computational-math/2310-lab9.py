import math

# Exact answers and scratchwork included in photos uploaded separately


# Problem 3
def euler(f, a, b, alpha, h):
  n = (b - a) / h
  t = a
  x = alpha
  for i in range(0, int(n)):
    x = x + (f(x, t) * h)
    t = t + h
  return (x, t)


# Problem 4
def tay2de(f, fp, a, b, alpha, h):
  n = (b - a) / h
  t = a
  x = alpha
  for i in range(0, int(n)):
    x = x + (f(x, t) * h) + (fp(x, t) * (h**2) / 2)
    t = t + h

  return (x, t)


# Problem 5a
print("\n\nProblem 5, part A.")


# Defines f(x,t) = x
def probAf(x, t):
  return x


# Defines fp(x,t) = 1 (Derivative of f(x,t))
def derAf(x, t):
  return 1


eulerdata = euler(probAf, 0, 1, 1, 1)
print("\nFor Euler's method, the approximate value of the solution at x =",
      eulerdata[1], "is", eulerdata[0])
print("The absolute error for Euler's method with h = 1 is",
      abs(eulerdata[0] - math.exp(1)))

tay2data = tay2de(probAf, derAf, 0, 1, 1, 1)
print(
    "\nFor the Taylor series method of order 2, the approximate value of the solution at x =",
    tay2data[1], "is", tay2data[0])
print(
    "The absolute error for the 2nd order Taylor series method with h = 1 is",
    abs(tay2data[0] - math.exp(1)))

eulerdata1 = euler(probAf, 0, 1, 1, 0.5)
print("\nFor Euler's method, the approximate value of the solution at x =",
      eulerdata1[1], "is", eulerdata1[0])
print("The absolute error for Euler's method with h = 0.5 is",
      abs(eulerdata1[0] - math.exp(1)))

tay2data1 = tay2de(probAf, derAf, 0, 1, 1, 0.5)
print(
    "\nFor the Taylor series method of order 2, the approximate value of the solution at x =",
    tay2data1[1], "is", tay2data1[0])
print(
    "The absolute error for the 2nd order Taylor series method with h = 0.5 is",
    abs(tay2data1[0] - math.exp(1)))

# Problem 5b
print("\n\nProblem 5, part B.")


def prob2f(x, t):
  return -0.06258176 * (x - 22)


def prob2fp(x, t):
  return -0.06258176


# Initialize variables for the loop
exactVal = 32.3042830726994
h = 0.1

for i in range(0, 4):
  eulerEst = euler(prob2f, 0, 6, 37, h)
  eulerErr = abs(exactVal - eulerEst[0])
  print("\nFor Euler's method, the approximate value of the solution at x =",
        eulerEst[1], "is", eulerEst[0])
  print("The absolute error for Euler's method with h =", h, " is", eulerErr)

  tay2Est = tay2de(prob2f, prob2fp, 0, 6, 37, h)
  tay2Err = abs(exactVal - tay2Est[0])
  print(
      "\nFor the Taylor series method of order 2, the approximate value of the solution at x =",
      tay2Est[1], "is", tay2Est[0])
  print("The absolute error for the 2nd order Taylor series method with h =",
        h, " is", tay2Err)

  h = h / 10

# For Euler's method, the error for each iteration is 1/10 of the last, which is the same amount we reduce the step size by
# We can call this relationship linear

# For the 2nd Order Taylor series method, the error for each iteration is also 1/10 of the last, which is the same amount we reduce the step size by
# We can call this relationship linear as well

# Problem 5c
print("\n\nProblem 5 part C.")


# Defines f(x,t) = -30x
def partCf(x, t):
  return -30 * x


# Defines fp(x,t) = -30 (derivative of f(x,t))
def partCfp(x, t):
  return -30


partCexact = math.exp(-30)

print("The exact answer to this DE at x = 1 is", partCexact)
cEulerTenth = euler(partCf, 0, 1, 1, 0.1)
print(
    "\nFor Euler's method with h = 0.1, the approximate value of the solution at x =",
    cEulerTenth[1], "is", cEulerTenth[0])
print("The absolute error is", abs(cEulerTenth[0] - partCexact))

cEulerHundredth = euler(partCf, 0, 1, 1, 0.01)
print(
    "\nFor Euler's method with h = 0.01, the approximate value of the solution at x =",
    cEulerHundredth[1], "is", cEulerHundredth[0])
print("The absolute error is", abs(cEulerHundredth[0] - partCexact))

cTayTenth = tay2de(partCf, partCfp, 0, 1, 1, 0.1)
print(
    "\nFor the Taylor series method of order 2 with h = 0.1, the approximate value of the solution at x =",
    cTayTenth[1], "is", cTayTenth[0])
print(
    "The absolute error for the 2nd order Taylor series method with h = 0.5 is",
    abs(cTayTenth[0] - partCexact))

cTayHundredth = tay2de(partCf, partCfp, 0, 1, 1, 0.01)
print(
    "\nFor the Taylor series method of order 2 with h = 0.01, the approximate value of the solution at x =",
    cTayHundredth[1], "is", cTayHundredth[0])
print(
    "The absolute error for the 2nd order Taylor series method with h = 0.5 is",
    abs(cTayHundredth[0] - partCexact))

print(
    "\n The above results are expected for a stiff DE, as lower step sizes are associated with greater numerical stability. With larger step sizes, we see wild oscillations which result in very poor estimations. As we reduce h, the estimates start to fall in line for what we expect from these algorithms."
)
