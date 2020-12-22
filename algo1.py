def solution(N,A):
  res=[0]*len(A)
  for i in range (len(A)) :
    if(A[i]>=1) and (A[i]<=N) :
      res[A[i]-1]+=1
    elif (A[i]== N+1):
      
      ma=max(res)
      res=[ma]*N

  return(res)
