# x = 3
# x = x*x
# print x

# y = raw_input('Enter a number: ')
# print type(y)
# print y

# y = float(raw_input('Enter a number: '))
# print type(y)
# print y
# print y*y

# x = int(raw_input('Enter an integer: '))
# if x%2 == 0:
#   print 'Even'
# else:
#   print 'Odd'
#   if x%3 != 0:
#     print 'And not divisible by 3'
#   else:
#     print 'divisible by 3'

# x = int(raw_input('Enter x:'))
# y = int(raw_input('Enter y:'))
# z = int(raw_input('Enter z:'))

# # if x < y:
# #   if x < z:
# #     print 'x is least'
# #   else:
# #     print 'z is least'
# # else:
# #   print 'y is least'

# # if x < y:
# #   if x < z:
# #     print 'x is least'
# #   else:
# #     print 'z is least'
# # elif y < z:
# #   print 'y is least'
# # else:
# #   print 'z is least'

# if x < y and x < z:
#   print 'x is least'
# elif y < z:
#   print 'y is least'
# else:
#   print 'z is least'


# x = int(raw_input('Enter an integer:'))
# ans = 0
# while ans*ans*ans < abs(x):
#   ans = ans + 1
#   print ans
# if ans*ans*ans != abs(x):
#   print 'x is not cube'
# else:
#   if x < 0:
#     ans = -ans
#   print 'cube root of ' + str(x) + ' is ' + str(ans)

####### Problem 1


# balance = float(raw_input('Enter the outstanding balance on your credit card: '))
# interest = float(raw_input('Enter the annual credit card interest rate as a decimal: '))
# mmpr = float(raw_input('Enter the minimum monthly payment rate as a decimal: '))

# month = 0
# total_amount_paid = 0

# while month < 12:
#   month += 1
#   mmp = mmpr*balance
#   interest_paid = (interest/12)*balance
#   principal_paid = mmp - interest_paid
#   balance = balance - principal_paid

#   if mmp > interest_paid:
#     total_amount_paid = total_amount_paid + mmp
#   else:
#     total_amount_paid = total_amount_paid + interest_paid

#   print 'Month: '+str(month)
#   print 'minimum monthly paid: '+str(round(mmp, 2))
#   print 'Principal Paid: '+str(round(principal_paid, 2))
#   print 'Remaning balance: '+str(round(balance, 2))

# print 'RESULT'
# print 'Total amount paid: '+str(round(total_amount_paid, 2))
# print 'Remaning balance: '+str(round(balance, 2))

####### Problem 2
