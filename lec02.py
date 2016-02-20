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

# balance_first = float(raw_input('Enter the outstanding balance on your credit card: '))
# interest = float(raw_input('Enter the annual credit card interest rate as a decimal: '))

# minimum_monthly_paid_upper = (balance_first*(1+(interest/12.0)**12.0)/12.0)
# minimum_monthly_paid_lower = balance_first/12.0

# minimum_monthly_paid = (minimum_monthly_paid_lower + minimum_monthly_paid_upper)/2
# monthly_interest = interest/12.0
# month = 0

# def calc_balance(b, mi, mmp):
#   m = 1

#   while m < 13:
#     b = b*(1+mi)-mmp
#     print m
#     print b

#     if b < 0:
#       print m
#       print mmp
#       print b
#       return
#     else:
#       m += 1

#   if b > 0:
#     if mmp >= minimum_monthly_paid:
#       mmp = (mmp + minimum_monthly_paid_lower)/2
#     else:
#       mmp = (mmp + minimum_monthly_paid_upper)/2

#     b = calc_balance (balance_first, monthly_interest, mmp)

# calc_balance (balance_first, monthly_interest, minimum_monthly_paid)

balance_first = float(raw_input('Enter the outstanding balance on your credit card: '))
interest = float(raw_input('Enter the annual credit card interest rate as a decimal: '))


monthly_interest = interest/12.0
month = 0
ipsilon = 0.1

minimum_monthly_paid_upper = (balance_first*(1+monthly_interest)**12.0)/12.0
minimum_monthly_paid_lower = balance_first/12.0

x = 1
balance = balance_first

while x < 100000:

  minimum_monthly_paid = (minimum_monthly_paid_lower+minimum_monthly_paid_upper)*0.5

  m = 1
  while m < 13:
    balance = balance*(1+monthly_interest)-minimum_monthly_paid
    print m
    print minimum_monthly_paid
    print balance
    m += 1

  print "ROOP END"

  if balance >= 0.1:
    minimum_monthly_paid_lower = minimum_monthly_paid
    balance = balance_first
  elif balance < -0.1: 
    minimum_monthly_paid_upper = minimum_monthly_paid
    balance = balance_first
  else:
    print balance
    print "aslfksdjflksdfjsdf"
    print "MMP" + str(minimum_monthly_paid)
    break
  x += 1

print minimum_monthly_paid_lower
print minimum_monthly_paid_upper

