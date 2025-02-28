import math

#### PROBLEM 1 ####
def cuberoot2(x0):
    xold = x0
    tol = 10^(-7)
    i = 1
    xnew = 1/3 * (2 * xold + 2 / (xold ** 2))
    while (abs(xnew-xold) > tol):
        xold = xnew
        xnew = 1/3 * (2 * xold + 2 / (xold ** 2))
        i += 1
    print("The sequence starting at", x0, "converges to", xnew, "in", i+1, "iteration(s).")

#### PROBLEM 2 ####
def nesty(x):
    f = (x-1)**5
    g = (x**5) - 5*(x**4) + 10*(x**3) - 10*(x**2) + 5*x - 1
    h = (((((x-5)*x+10)*x-10)*x+5)*x-1)

    print("x =", x, ", f(x) =", f, ", g(x) =", g, ", h(x) =", h)

x = 1.0
j = 0.1
for i in range (0, 7):
    x = 1.0 + j
    j = j/10
    nesty(x)

# Exact answers are in one of the PDFs I submitted
# f(x) appears to be the most accurate of the algorithms.
# This is likely because of the fact that multiplication does not contribute much to error propagation,
# but addition and multiplication can. There is likely cancelation error occurring in g and h.
