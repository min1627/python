# Test = (1,2,3,4,5)
# print Test[0]
# print Test[1]

# x = 100
# divisors = ()
# for i in range (1,x):
#   if x%i == 0:
#     divisors = divisors+(i,) #put divisors in tuple
# print divisors

# Techs = ['MIT', 'Cal Tech']
# Ivys = ['Harvard', 'Yale', 'Brown']
# Univs = []
# Univs.append(Techs)
# print Univs

# Univs.append(Ivys)
# print Univs
# for e in Univs:
#   print e

# flat = Techs + Ivys
# print flat

# artSchools = ['RISD', 'Harvard']
# for u2 in artSchools:
#   if u2 in flat:
#     flat.remove(u2)
# print flat

# flat.sort()
# print flat

# flat[1] = 'UMass'
# print flat

EtoF = {'bread':'du pain', 'wine':'du vin', \
'eats':'mange', 'drinks':'bois',\
'likes':'aime', 1:'un', '6.00':'6.00'}

# print EtoF
# print EtoF.keys
# print EtoF.keys()

# del EtoF[1]
# print EtoF

# D = {1: 'one', 'deux': 'two', 'pi': 3.14159}
# D1 = D
# print D1
# D[1] = 'uno'

# for k in D1.keys():
#   print k, '=', D1[k]
# print D1

# def translateWord(word, dictionary):
#   if word in dictionary:
#     return dictionary[word]
#   else:
#     return word

# def translate(sentence):
#   translation = ''
#   word = ''
#   count = 0
#   for c in sentence:
#     if c != ' ':
#       word = word + c
#     else:
#       translation = translation+' '+translateWord(word, EtoF)
#       count += 1

#       print translation, ' ', count
#       word = ''
#   return translation[1:] + ' ' + translateWord(word, EtoF)

# print translate('John eats bread')
# print translate('Steve drinks wine')
# print translate('John likes 6.00')

def keySearch(L, K):
  for elem in L:
    if elem[0] == k:
      return elem[1]
  return None

