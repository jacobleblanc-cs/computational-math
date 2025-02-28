import math

# Problem 1

# This is a rough draft from the psuedocode, clean this up later
def Newt(f, fp, x0, TOL, MAXITER):
    xold = x0
    xnew = 0

    for i in range (0, MAXITER):
        if math.abs(fp(xold)) < TOL:
            print("The derivative at an iterate with value", xold, "is zero.")
            return
        xnew = xold-f(xold)/fp(xold)
        if math.abs(xnew) > 10**20:
            print("The iterates tend to infinity.")
            return
        if math.abs(f(xnew)) < TOL or math.abs(xnew-xold) < TOL:
            print("Starting at", x0, ", the solution to the equation is", xnew, "in", i, "iterations.")
            return
        xprev = xnew
    print("The solution wasn't found in", MAXITER, "iterations.")
    return

# Problem 2

def twoA(x):
    (x**3) - (2*x) + 2

def twoAprime(x):
    (3*(x**2)) - 2

def twoB(x):
    (x**3) - (2*x) + 2 + (0.1*math.sin(1000*x))

def twoBprime(x):
    (3*(x**2)) - 2 + 100*cos(1000*x)

def twoC(x):
    (x-2)/(x-1)
def twoCprime(x):
    1/((x-1)**2)

Newt(twoA, twoAprime, 0, 10**-7, 20)
Newt(twoB, twoBprime, 0, 10**-7, 20)
Newt(twoC, twoCprime, 3.1, 10**-7, 20)
    
# Problem 3

# Equation I found through algebra was x^4-8x^2+13
def p3eq(x):
    return x**4 - 8*x**2 + 13

def p3prime(x):
    return 4*x**3 - 16*x

Newt(p3eq, p3prime, 1, 10**-7, 20)

# Problem 4
def Sec(f, a, b, TOL, MAXITER):
    
    fa = f(a)
    fb = f(b)
        
    for n in range (1, MAXITER):
        if (abs(fa) > abs(fb)):
            tempa = a
            a = b
            b = tempa
            tempfa = fa
            fa = fb
            fb = tempfa
        d = (b-a)/(fb-fa)
        b = a
        fb = fa
        d = d*fa
        if (math.abs(d) > 10**20):
            print("The iterates tend to infinity.")
            return
        if (abs(d) < TOL):
            print("The solution to the equation is", d, "in", n, "iterations.")
            return
    print("The solution wasn't found in", MAXITER, "iterations.")

def p(x):
    return x**5 + x**3 + 3

Sec(p, -1, 1, 10**-7, 20)

Sec(twoA, twoAprime, 0, 10**-7, 20)
Sec(twoB, twoBprime, 0, 10**-7, 20)
Sec(twoC, twoCprime, 3.1, 10**-7, 20)