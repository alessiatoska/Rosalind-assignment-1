#FIB rosalind

def fib(n,k):
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
    return fib(n-1,k)+k*fib(n-2,k)
  
print(fib(5,3))
