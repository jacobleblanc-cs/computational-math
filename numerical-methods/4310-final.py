import math
import matplotlib.pyplot as plt

# Problem 2
# Write a Python program to implement the Runge-Kutta Method of Order 4 to approximate the value of the solution of the DE
# x'(t)=f(t,x) x(a)=xa at t=b using n steps

print("Problem 2 in source file")


def rk4(f, t, x, h, n):
  t_a = t
  for i in range(1, n + 1):
    k1 = h * f(t, x)
    k2 = h * f(t + h / 2, x + k1 / 2)
    k3 = h * f(t + h / 2, x + k2 / 2)
    k4 = h * f(t + h, x + k3)
    x = x + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    t = t_a + (i * h)
  return t, x, n


# Problem 3
# Test the rk4 procedure on the example from page 315
# Result is printed to the console
print("\nProblem 3:\n")


def test_rk4(t, x):
  return 2 + (x - t - 1)**2


testrk4t, testrk4x, testrk4n = rk4(test_rk4, 1, 2, (0.5625 / 72), 72)
print("The approximate value of the solution at x =", testrk4t, "is", testrk4x)

# Problem 4
# Consider the DE x'=(2-t)x with x(2)=1
# Use the rk4 procedure to approximate the value of the solution at t=3 with step size n=2^k for k=0,1,...,6
print("\n\nProblem 4:\n")


def prob4fn(t, x):
  return (2 - t) * x


def prob4exact(t):
  return math.e**((-(t - 2)**2) / 2)


exact_answer = prob4exact(3)

for k in range(7):
  n = 2**k
  tempt, tempx, tempn = rk4(prob4fn, 2, 1, (1 / n), n)
  abs_error = abs(exact_answer - tempx)
  print("The approximate value of the solution at x =", tempt, "with", tempn,
        "steps is", tempx, "with an absolute error of", abs_error)
  print("The relative error is", abs_error / exact_answer, "\n")

print(
    "We can tell that this method is order 4 because the step size, which is equivalent to 1/n, is decreasing by half with each iteration. However the error is "
)

# Problem 5
print("\n\nProblem 5:\n")


def tri(diag, subdiag, supdiag, b, n):
  for i in range(1, n):
    mult = subdiag[i - 1] / diag[i - 1]
    diag[i] -= mult * supdiag[i - 1]
    b[i] -= mult * b[i - 1]
  x = [0] * n
  x[n - 1] = b[n - 1] / diag[n - 1]
  for i in range(n - 2, -1, -1):
    x[i] = (b[i] - supdiag[i] * x[i + 1]) / diag[i]
  return x


diag = [1, 1, 1, 1]
subdiag = [2, 2, 2]
supdiag = [2, 2, 2]
b = [3, 5, 5, 3]
n = 4

solution = tri(diag, subdiag, supdiag, b, n)
print("Solution x =", solution)

# Problem 6
print("\n\nProblem 6:\n")


def question6e():
  n = 50
  h = (math.pi / 2) / n  # Corrected h value
  diag = [h**2 - 2] * (n - 1)
  subdiag = [1] * (n - 2)
  supdiag = subdiag.copy()
  b = [0] * (n - 1)
  b[n - 2] = -1

  x = tri(diag, subdiag, supdiag, b, n - 1)

  # Construct t vector
  t = [0.0] * (n - 1)
  for i in range(1, n - 1):
    t[i] = 0 + h * (i - 1)

  plt.plot(t, x)
  plt.show()

  return x


solution6e = question6e()
