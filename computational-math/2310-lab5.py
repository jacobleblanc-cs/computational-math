import math

# Problem 1
for i in range(0, 6):
  print(i)

for i in range(1, 10):
  print(i)

for i in range(11, 36, 5):
  print(i)

# Problem 2
x1 = 0
if x1 > 2:
  print(3 * x1)
elif x1 <= 2:
  print(4 * x1)

x2 = 0
if x2 <= 0:
  print(abs(2 * x2))
elif x2 >= 1:
  print((x2**3) - 1)
else:
  print(math.sin(x2))

# Problem 3
x3 = -10
while x3 < 0:
  print("While loop 1 is working! Setting x to 0 to break loop...")
  x3 = 0

x4 = 5
while x4 > 1:
  print("While loop 2 is working! Setting x to 1 to break loop...")
  x4 = 1

xnew = 1000
xprev = 900
TOL = 150
i = 50
while (((abs(xnew - xprev)) < TOL) and (i <= 1000)):
  print("While loop 3 is working! Setting i to 1001 to break loop...")
  i = 1001

# Problem 4

for i in range(1000, 2000):
  print(i, 2.0**-i)

ind = 0
retVal = 1.1
while retVal > 1.0:
  retVal = 1.0 + 2**-ind
  ind += 1
  print(ind, retVal)


def triangle(a, b, c):
  if ((a < b + c) or (b < a + c) or (c < a + b)):
    print("The numbers", a, ",", b, ",", c,
          "are the sides of a valid triangle.")
  else:
    print("The numbers", a, ",", b, ",", c,
          "are not the sides of a valid triangle.")


print(triangle(2, 4, 5))


def addintegers(N):
  sum7 = 0
  i = 1
  while (sum7 < N):
    sum7 += i
    i += 1
  print("You need to add ", i, "integers so that the sum is greater than ", N)

addintegers(10)