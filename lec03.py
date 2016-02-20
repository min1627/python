# #Find the cube root of perfect cube

# x = int(raw_input('Enter an integer: '))
# ans = 0

# while ans*ans*ans < abs(x):
#   ans = ans + 1
#   print 'current guess = ', ans
# if ans*ans*ans != abs(x):
#   print x, 'is not a perfect cube'
# else:
#   if x < 0:
#     ans = -ans
#     print 'cube root of ' + str(x) + ' is ' + str(ans)


#Find the cube root of perfect cube
# x = int(raw_input('Enter an integer: '))
# for ans in range(0, abs(x)+1):
#   if ans**3 == abs(x):
#     break

# if ans**3 != abs(x):
#   print x, 'is not a perfect cube'
# else:
#   if x < 0:
#     ans = -ans
#   print ans


# x = float(raw_input('Enter an integer: '))
# epsilon = 0.01
# numGuesses = 0
# ans = 0.0

# while abs(ans**2 - x) >= epsilon and ans*ans <= x:
#   ans += 0.0001
#   numGuesses += 1
#   print 'numGuesses =', numGuesses
#   if abs(ans**2 -x) >= epsilon:
#     print 'Failed on square root of', x
#   else:
#     print ans, 'is close to square root of', x



x = float(raw_input('Float : '))

epsilon = 0.0001
numGuesses = 0
low = 0.0 # set lower
high = max(x, 1.0) #set upper
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
  print 'ans = ', ans, 'low = ', low, 'high = ', high
  numGuesses += 1
  if ans**2 < x:
    low = ans # if smaller, set low as ans
  else:
    high = ans
  ans = (high + low)/2.0

print 'num = ', numGuesses
print 'ans = ', ans






