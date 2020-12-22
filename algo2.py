def solution(A, B):
    L = max(A)
    max_b = max(B)
  
    fib = [0] * (L+2)
    fib[1] = 1
    for i in range(2, L + 2):
        fib[i] = (fib[i-1] + fib[i-2]) & ((1 << max_b) - 1)
  
    res = [0] * len(A)
  
    for j in range(len(A)):
        res[j] = fib[A[j]+1] & ((1 << B[j]) - 1)
  
    return res
