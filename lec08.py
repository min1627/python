# def f(n):
#   assert n >= 0
#   answer = 1

#   while n > 1:
#     answer *= n
#     n -= 1
#     print answer
#   return answer

# f(10)

# def g(n):
#   x = 0
#   for i in range(n):
#     for j in range(n):
#       x += 1
#       print x
#   return x

# g(5)
# g(3)
# g(10)

def bSearch(L, e, low, high):
  global numCalls
  numCalls += 1
  if high - low < 2:
    return L[low] == e or L[high] == e
  mid = low + int((high-low)/2)
  if L[mid] == e:
    return True
  if L[mid] > e:
    return bSearch(L, e, low, mid-1)
  else:
    return bSearch(L, e, mid+1, high)

def search(L, e):
  return bSearch(L, e, 0, len(L)-1)

L = range(1000)
numCalls = 0
print search(L, 3)
print numCalls
