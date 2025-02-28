import numpy as np

def gauss(A, b, n):
  L = np.arange(n)
  scale = [0]*n
  x = [0]*n
  for i in range(n):
    maxvalue = 0.0
    for j in range(n):
      if abs(A[i][j]) > maxvalue:
        maxvalue = abs(A[i][j])
    scale[i] = maxvalue
  for j in range(n-1):
    ratiomax = 0
    maxrow = 0
    for i in range(j, n):
      if abs(float(A[L[i]][j]/scale[L[i]])) > ratiomax:
        ratiomax = abs(float(A[L[i]][j]/scale[L[i]]))
        maxrow = i
    temp = L[j]
    L[j] = L[maxrow]
    L[maxrow] = temp
    for i in range(j+1, n):
      multiplier = -A[L[i]][j]/A[L[j]][j]
      for k in range(j, n):
        A[L[i]][k] = A[L[i]][k] + multiplier*A[L[j]][k]
      b[L[i]]=b[L[i]] + multiplier*b[L[j]]
  x[n-1]=b[L[n-1]]/A[L[n-1]][n-1]
  for i in range(n-2, -1, -1):
    summ = 0.0
    for j in range(i+1, n):
      summ = summ + A[L[i]][j] * x[j]
    x[i] = (b[L[i]] - summ)/A[L[i]][i]
  return x

A = np.array([[3, -13, 9, 3], [-6, 4, 1, -18], [6, -2, 2, 4], [12, -8, 6, 10]])

b = np.array([-19, -34, 16, 26])

print(gauss(A, b, 4))

num8 = np.array([[2, 4, -2],[1, 3, 4],[5, 2, 0]])

num8b = np.array([6, -1, 2])

print(gauss(num8, num8b, 3))

num19A1 = np.array([[1, 1/2, 1/3, 1/4, 1/5], [1/2, 1/3, 1/4, 1/5, 1/6], [1/3, 1/4, 1/5, 1/6, 1/7], [1/4, 1/5, 1/6, 1/7, 1/8], [1/5, 1/6, 1/7, 1/8, 1/9]])

num19A2 = np.array([[1, 0.5, 0.333333, 0.25, 0.2], [0.5, 0.333333, 0.25, 0.2, 0.166667], [0.333333, 0.25, 0.2, 0.166667, 0.142857], [0.25, 0.2, 0.166667, 0.142857, 0.125], [0.2, 0.166667, 0.142857, 0.125, 0.111111]])

num19b = np.array([1, 0, 0, 0, 0])

print(gauss(num19A1, num19b, 5))
print(gauss(num19A2, num19b, 5))

num19x1 = np.array([25, -300, 1050, -1400, 630])
num19x2 = np.array([26.9314, -336.018, 1205.11, -1634.03, 744.411])
