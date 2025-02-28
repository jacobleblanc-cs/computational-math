import math
import random

# Using my randab function from lab10 for some problems
def randab(a, b):
  x = random.random()
  return (((b - a) * x) + a)

# Part 1

# Problem 8, pg 490
print("Exercise #8, page 490")
#If x1, x2,... is a random sequence of numbers uniformly distributed 
#in the interval (0, 1), what proportion would you expect to	
# satisfy the inequality 40x^2 + 7 > 43x ? 
# Write a program to test this on 1000 random numbers.


# First step: For what values of x is this inequality satisfied?
# 40x^2 - 43x +7 > 0
# Using quadratic formula:
#       (43± √(-43)^2 - (4)(40)(7)) / 2(40)
#      =(43± √1849 - 1120) / 80
#      =(43± √729) / 80
#      =(43 ± 27) / 80
#      Solutions at 70/80 and 16/80
#      Or 7/8 and 1/5
#      The intervals where this is > 0 are
#      when x is in [0, 1/5)U(7/8, 1]
#      which we can see by plugging in 1/5 and 7/8 into our original formula
#      then testing nearby values and seeing that it is only > 0 within that range
#      Thus, the probability of being > 0 is
#      1/8 + 1/5 == 5/40 + 8/40 == 13/40
#      Exact answer is 0.325 or 32.5%

# This function returns the original formula, solved to set the inequality as > 0
def prob8Fn(x):
    return (40*(x**2))-(43*x)+7

# This function plugs a random number on the interval (0,1) into the balanced
# inequality, and if it satisfies the inequality it is added to a sum
# It then returns the percentage of points which satisfied the inequality
def intervalDistrib(f):
    sum = 0
    for i in range (0, 1001):
        if(f(randab(0, 1)) > 0):
            sum += 1
    return sum/1000

# This loop calls our two functions above to run 5 trials and print output regarding the
# statistical likelihood of a point satisfying the inequality
trialSum = 0
for i in range (1, 6):
    trialI = intervalDistrib(prob8Fn)
    trialSum += trialI
    print("On trial",i,", the probability that a random point on the interval satisfies the inequality is", trialI*100, "%")

# This statement gives a more summarized look at things, showing the average percentage of
# points satisying the inequality across all 5 trials
print("The average probability of a random point satisfying the inequality for these trials was", (trialSum*100)/5)

# From the trials I ran, I saw average probabilities across 5 trials that were very close to my calculated expected value.
# With an expected value of 32.5%, I saw results of 31.66%, 33.12%, and 31.68% across three sets of these experimental runs of 5 trials.




# Problem 11a, pg 497

print("\n\nExercise #11a, page 497")
# Use the Monte Carlo method to approximate the following integral:
# Triple integral with all three bounds of integration from -1 to 1
# Function being integrated is (x^2 - y^2 - z^2)dxdydz
# I solved this problem on paper so I will attach a scan of that scratch work
# In short, the exact solution to this integral is -8/3 or -2.666....

def prob11aFn(x, y, z):
    return x**2 - y**2 - z**2

def monteCarlo11a(f):
    sum = 0
    for i in range (0, 10000):
        xpt = randab(-1, 1)
        ypt = randab(-1, 1)
        zpt = randab(-1, 1)
        sum += f(xpt, ypt, zpt)
    retVal = (6*sum)/10000
    return retVal

sum11a = 0
for i in range (1, 6):
    trial11a = monteCarlo11a(prob11aFn)
    sum11a += trial11a
    print("The approximate value of this definite integral on trial", i, "is", trial11a)
print("The average estimate from these trials was", sum11a/5)
print("The exact value was -8/3 or -2.666...")

# From my time running this code, the average value reported across the trials was about -2
# I ran the code multiple times and the averaged value between all the runs was -2.01, -1.99, and -1.99 again


# Problem 18, pg 505

print("\n\nExercise #18, page 505")

# Consider the lattice points (pts w/ int coords) in the square 0 <= x <= 6,
# 0 <= y <= 6. A particle starts at (4,4) and moves in the following way:
# At each step, it moves with equal probability to one of the four adjacent
# lattice pts. What is the probability that when the particle first crosses the
# boundary of the square, that it crosses the bottom boundary? Use Monte Carlo simulation

# For this problem, I am going to generate a random direction for both axes by using
# my randab function to generate a number between 1 and 5 (Due to the fact its not inclusive here),
# then I will cast that result to an integer to truncate it
# This should produce a result of either 1, 2, 3, or 4 with equal probability,
# which I will treat as a direction. 
# For x: 1 = right, 2 = left
# For y: 3 = up, 4 = down

def prob18soln():
    sum = 0
    for i in range (0, 10000):
        x = 4
        y = 4
        hitBound = False
        while (hitBound == False):
            move = int(randab(1,5))
            if move == 1:
                x += 1
            elif move == 2:
                x -= 1
            elif move == 3:
                y += 1
            elif move == 4:
                y -= 1

            if (x == 0 or x == 6 or y == 6):
                hitBound = True
            elif y == 0:
                sum += 1
                hitBound = True
    probability = sum / 10000
    return probability

prob18avg = 0
for i in range (0, 5):
    soln = prob18soln()
    prob18avg += soln
    print(soln)
print("Average probability over all trials was", prob18avg/5)

# Looking at the results, I would estimate that the probability of crossing the bottom border is 1/8 or 0.125
# This is a rough estimate but the probabilities I was able to calculate from my estimate were all hovering between .12 and .13 which makes me feel confident about this estimate
# In my test, my program produced values of 0.1248, 0.1203, 0.1217, 0.1309, and 0.1192
# This is a tight grouping and averages to .1234, so I stand confidently by this estimated percentage



# Problem 19, pg 67

print("\n\nPART TWO")
print("\nExercise #19, page 67")

# Write a routine to compute the tangent of x in radians using the following algorithm:
# 1) The argument x is reduced to abs(x) <= pi/2
# 2) If 0 <= abs(x) <= 1.7*10^-9, set tanx roughly = x
# 3) If abs(x) > pi/4, set u = pi/2 - x; otherwise, set u = x, then compute the approx
# 4) If abs(x) was > pi/4, then tanx roughly = 1/tanu; otherwise, tanx roughly= tanu

def findTan(x):

    # First step: Check that x is within the first period of tangent(x)
    absx = abs(x)
    while (absx > (math.pi/2)):
        if (x > 0):
            x = x-math.pi
            absx = abs(x)
        elif (x < 0):
            x = x+math.pi
            absx = abs(x)

    # Second step: If x is already close to 0, tan(x) will also be roughly 0, so ret x
    TOL = 1.7*(10**-9)
    if (x >= 0 and x <= TOL):
        return x
    
    # Third step: Compute value of U
    u = 0
    if (absx > (math.pi/4)):
        u = (math.pi/2) - x
    else:
        u = x
        
    # Fourth step: Compute the approximation of tan(u)
    tanu = u*(135135 - (17336.106*(u**2)) + (379.23564*(u**4)) - (1.0118625*(u**6)))/(135135 - (62381.106*(u**2)) + (3154.9377*(u**4)) - (28.17694*(u**6)))
    
    # Final step: Compute the approximation of tan(x)
    tanx = 0
    if (absx > (math.pi/4)):
        tanx = 1/tanu
    else:
        tanx = tanu
        
    return tanx

print("tan( pi/4 ) = ", findTan(math.pi/4), "and the error is", abs(findTan(math.pi/4)-math.tan(math.pi/4)))
print("tan( -pi/6 ) = ", findTan(-math.pi/6), "and the error is", abs(findTan(-math.pi/6)-math.tan(-math.pi/6)))
print("tan( pi/4 + 214pi ) = ", findTan((math.pi/4)+(214*math.pi)), "and the error is", abs(findTan((math.pi/4)+(214*math.pi))-math.tan((math.pi/4)+(214*math.pi))))
print("tan( -pi/6 - 1000pi ) = ", findTan((-math.pi/6) - (1000*math.pi)), "and the error is", abs(findTan((-math.pi/6) - (1000*math.pi))-math.tan((-math.pi/6) - (1000*math.pi))))
print("tan( 10^-12 ) = ", findTan(10**(-12)), "and the error is", abs(findTan(10**(-12))-math.tan(10**(-12))))



# Range Reduction Problems
print("\n\nRange Reduction Section")


def e_taylor(x):
    # Skipping first term by starting result at 1. Shouldn't cause problems as e^0==1
    result = 1.0 
    factorial = 1.0 # Initializing both vars as floats to prevent int floor div
    
    for i in range (1, 51):
        factorial *= i
        result += (x**i)/factorial
    return result

testvals = [-100, -50, -10, -1, 1, 10, 50, 100]

totErrOG = 0
for i in range(0, 8):
    est = e_taylor(testvals[i])
    err = abs(est - math.e**testvals[i])
    totErrOG += err
    #print("The original estimate of e to the",testvals[i], "is", est, "with error", err)

def e_rangered(x):
    m = int(x/math.log(2))
    u = x - (m*math.log(2))
    
    result = 1.0
    factorial = 1.0
    
    for i in range (1, 11):
        factorial *= i
        result += (u**i)/factorial
    return result*2**m

totErrNew = 0
for i in range(0, 8):
    est = e_rangered(testvals[i])
    err = abs(est - math.e**testvals[i])
    totErrNew += err
    #print("The reduced range estimate of e to the", testvals[i], "is", est, "with error", err)
    
print("The average error of our original estimate was", totErrOG/8, "\nThe average error of our reduced range estimate was", totErrNew/8)

# To view the actual estimates and their individual error, uncomment the two lines in the for loops that calculate the error

# To summarize our findings here: The reduced range estimate was able to successfully reduce our error and produced more accurate estimates with lower computational intensity
# This was accomplished by pulling off m powers of two and then adding it back on at the end