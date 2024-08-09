def max(a, b):
  if a > b:
    return a
  else:
    return b
def min(a, b):
  if a < b:
    return a
  else:
    return b
"""
Eulid's algorithm is a process to find greatest common divisor of two numbers.
First function we have used basics of programming to write it.
Second function we have used recursion to write it.
"""
def EuclidAlgo1(a, b):
  n1 = max(a,b)
  n2 = min(a,b)
  if n2 == 0:
    return n1
  else:
    r = n1 % n2
    while r != 0:
      n1 = n2
      n2 = r
      r = n1 % n2
    return n2
    
def EuclidAlgo2(a, b):
  n1 = max(a,b)
  n2 = min(a,b)
  if n1 % n2 != 0:
    EuclidAlgo2(n2, n1 % n2)
  else:
    return n2  

        