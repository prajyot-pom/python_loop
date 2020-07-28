# -----------------------------------  for loop -----------------------------------------

# for loop iterates over a collection such as list or dict

for i in [0,1,2,3,4]:
    print (i)

# range is a function that returns a series of numbers under an iterable form
print ("Using range function")

for i in range(5):
    print (i)

# If you want to loop through both the elements of a list and have an index for the elements as well,
# you can use Python's enumerate function
print ("Using enumerate function")
for index, item in enumerate(['one', 'two', 'three', 'four']):
    print (index, "::", item)

"""
Iterate over a list with value manipulation using map and lambda,
i.e. apply lambda function on each element in the list.

NB: in Python 3.x map returns an iterator instead of a list
so you in case you need a list you have to cast the result print(list(x))
"""
print ("Using map and lambda function")
x = map(lambda e:  e.upper(), ['one', 'two', 'three', 'four'])
print(x)


# ---------------- Loops with else clause ------------------------------------

"""
The else clause only executes after a for loop terminates by iterating to completion,
or after a while loop terminates by its conditional expression becoming false.
"""

print ("For loop with else clause:: ")
for i in range(3):
    print (i)
else:
    print ('done')

print ('While loop with else clause')
i = 0
while i < 3:
    print (i)
    i += 1
else:
    print ('done')

"""
The else clause does not execute if the loop terminates some other way
(through a break statement or by raising an exception):
"""
print ('for with break: ')

for i in range(2):
    print(i)
    if i == 1:
        break
else:
    print('done')

# --------------------- pass statement -----------------------------------------------
"""
pass is a null statement for when a statement is required by Python syntax
(such as within the body of a for or while loop), but no action is required or desired by the programmer.
This can be useful as a placeholder for code that is yet to be written
"""
# x = y = 1
# while x == y:
#     pass

# ----------------------Iterating over dictionaries -----------------------------------
print ("Iterating over dictionaries:: ")
d = {"a": 1, "b": 2, "c": 3}
for key in d:
    print(key)
print ('-----------------------')

for key in d.keys():
    print(key)
print ('-----------------------')
for key, value in d.items():
    print(key, "::", value)

"""
Note that in Python 2, .keys(), .values() and .items() return a list object. 
If you simply need to iterate through the result, you can use the equivalent .iterkeys(), 
.itervalues() and .iteritems().

iter* methods are generators. 
Thus, the elements within the dictionary are yielded one by one as they are evaluated. 
When a list object is returned, all of the elements are packed into a list and 
then returned for further evaluation.
"""