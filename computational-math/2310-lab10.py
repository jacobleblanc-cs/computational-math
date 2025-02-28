import random
import math

# Problem 3a
def linearCongruential(m):
  if (m > 2147483647 or m < 0):
    return -1
  seed = random.random()
  a = 16807
  seed = (seed * a) % m
  return (seed)


# Problem 3b
print(linearCongruential(1))

# Problem 3c
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(0, 1000001):
  genNum = linearCongruential(1)
  if 0 < genNum <= 0.1:
    arr[0] = arr[0] + 1
  elif 0.1 < genNum and genNum <= 0.2:
    arr[1] = arr[1] + 1
  elif 0.2 < genNum and genNum <= 0.3:
    arr[2] = arr[2] + 1
  elif 0.3 < genNum and genNum <= 0.4:
    arr[3] = arr[3] + 1
  elif 0.4 < genNum and genNum <= 0.5:
    arr[4] = arr[4] + 1
  elif 0.5 < genNum and genNum <= 0.6:
    arr[5] = arr[5] + 1
  elif 0.6 < genNum and genNum <= 0.7:
    arr[6] = arr[6] + 1
  elif 0.7 < genNum and genNum <= 0.8:
    arr[7] = arr[7] + 1
  elif 0.8 < genNum and genNum <= 0.9:
    arr[8] = arr[8] + 1
  elif 0.9 < genNum and genNum <= 1:
    arr[9] = arr[9] + 1

sum = sum(arr)
for i in range(0, 9):
  print((arr[i] / sum) * 100, "% of numbers generated were between", i / 10,
        "and", (i / 10) + 0.1)


# Problem 4
def randab(a, b):
  x = random.random()
  return (((b - a) * x) + a)


print(randab(1, 6))

print(randab(5, 9))

# Problem 5
x = []
y = []


def diamond(x, y):
  # Generate 1000 random pts uniformly distributed in the diamond
  # with vertices (0,1), (1,0), (-1,0), (0,-1)
  while len(x) < 1000 or len(y) < 1000:
    xin = randab(-1, 1)
    yin = randab(-1, 1)
    if (yin <= -abs(xin) + 1 and yin >= abs(xin) - 1):
      x.append(xin)
      y.append(yin)


diamond(x, y)
# Debug lines
#for i in range(0, 1000):
#  print(x[i], y[i], i)

# Problem 6
# Write a program to simulate 1000 simultaneous flips of three coins
# Print the number of times that two of the three coins come up heads


def flipCoins():
  count = 0
  # If generated value is > 0.5, treat it as heads
  for i in range(0, 1000):
    coin1 = (randab(0, 1))
    coin2 = (randab(0, 1))
    coin3 = (randab(0, 1))
    if (coin1 > 0.5 and coin2 > 0.5 and coin3 <= 0.5):
      count += 1
    elif (coin1 > 0.5 and coin2 <= 0.5 and coin3 > 0.5):
      count += 1
    elif (coin1 <= 0.5 and coin2 > 0.5 and coin3 > 0.5):
      count += 1
  return count


for i in range(0, 6):
  print(flipCoins())


# Problem 7
def verifyPi(f):
  n = 2500
  count = 0
  sum = 0
  while count < int(n):
    sum += f(randab(0, 2))
    count += 1
  sum = 2*sum / n
  return sum


def f(x):
  return (4 - x**2)**(1 / 2)

print(verifyPi(f))

piEstTotal = 0
for i in range (0, 10):
  newEst = verifyPi(f)
  piEstTotal += newEst
  print("Estimate", i, "is", newEst)
  
print("The average of our 10 estimates is:", piEstTotal / 10)