# --------------------------------------- half loop do-while ---------------------------------------

"""
Python doesnt have a do-until or do-while loop construct.
But we can achieve it by combining a while True with a break statement to achieve same purpose
"""

a = 10
while True:
    a = a - 1
    print (a)

    if a < 7:
        break
print ('done')

# --------------------------------------- Looping and unpacking ---------------------------------------

"""
There is a way through which we can loop over a list of touples
"""

collection = [('a', 'b', 'c'), ('p', 'q', 'r'), ('x', 'y', 'z')]

print ('first way')
for item in collection:
    i1 = item[0]
    i2 = item[1]
    i3 = item[2]

    print (i1)
    print (i2)
    print (i3)
print ('-----------------------')
print ('second way')
for item in collection:
    i1, i2, i3 = item
    print (i1)
    print (i2)
    print (i3)
print ('-----------------------')
print ('Third way')
for i1, i2, i3 in collection:
    print (i1)
    print (i2)
    print (i3)
print ('-----------------------')
# --------------------------------------- Iterating over diff. portion of list --------------------------------

"""
We may find different scenarios for iterating over a list.
"""
lst = ['alpha', 'bravo', 'charlie', 'delta', 'echo']

print ('1. Iterating over whole list :: ')
for s in lst:
    print s[:1]  # print only first letter

print ('-----------------------')

print ('2. printing element and its respective index :: ')
for idx, s in enumerate(lst):
    print ('%s has an index of %d' % (s, idx))

print ('-----------------------')

print ('3. Iterate over a sublist :: ')
for i in range(2, 4):
    print ('lst at %d contains %s' % (i, lst[i]))

print ('-----------------------')

print ('3. With slice notations ::')
for s in lst[1::2]:
    print(s)
print ('-----------------------')

# --------------------------------------- While Loop -----------------------------------------------

"""
A while loop will cause the loop statements to be executed until the loop condition is false
"""

i = 0

while i < 4:
    print (i)
    i = i + 1