import math

### START PROBLEM 1 ###
print("\nPROBLEM #1 PART A\n")

# Exercise 19, part a
x = 0
y = 0
z = 0

for i in range(1, 21):
    x = 2 + (1.0 / (8 ** i))
    y = math.atan(x)-math.atan(2)
    z = y * (8 ** i)
    print("x =", x, "y =", y, "z =", z)
    
# This function computes the difference between the arctangent of x and arctangent of 2
# X starts as 2+1/8, but the fraction added to it gets smaller and smaller with each iteration.
# This creates a situation where there is subtraction of very small decimals.
# This causes a cancelation error which results in truncation and rounding down to 0 by the end of the loop

print("\nPROBLEM #1 PART B\n")
# Exercise 19, part b
epsi = 1
while 1 < 1 + epsi:
    epsi = epsi/2
    print(epsi)
    
# The above problem calculates the smallest possible number which can be represented in Python's numerical system.
# It loops until 1+epsi is equal to 1, i.e. to the point where epsi is so small that it gets rounded to zero.


print("\nPROBLEM #2\n")
### START PROBLEM 2 ###
def mult15(n):
    answer = 0
    if n%15==0:
        answer = n-15
    else:
        answer = n-n%15
    print("The largest multiple of 15 that is smaller than", n, "is", answer)
    
mult15(31)
mult15(247)
mult15(50)
mult15(99)
mult15(30)