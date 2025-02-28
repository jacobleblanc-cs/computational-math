def gs(A, b, x, n, tol):
  iterate = 0
  for k in range(1, 100):
    iterate += 1
    error = 0
    xold = list(x)
    for i in range(n):
      summ = 0.0
      for j in range(1,i):
        summ += A[i][j]*x[j]
      for j in range(i+1,n):
        summ += A[i][j]*x[j]
      x[i] = (b[i]-summ)/A[i][i]
      error += abs(x[i]-xold[i])
    if error < tol:
      print("Converges")
      return x
  print("Didn't converge in 100 iterations")
  return

import numpy as np

def gauss_seidel(A, b, x, n, tol):
    max_iter = 1000
    iter_count = 0
    while iter_count < max_iter:
        x_new = np.copy(x)
        for i in range(n):
            sum_ = np.dot(A[i, :i], x_new[:i]) + np.dot(A[i, i+1:], x[i+1:])
            x_new[i] = (b[i] - sum_) / A[i, i]
        error = np.linalg.norm(np.dot(A, x_new) - b, ord=1)
        if error < tol:
            print("Solution:", x_new)
            print("Number of iterations:", iter_count)
            return x_new
        x = x_new
        iter_count += 1
    print("Maximum iterations reached without convergence.")
    return x