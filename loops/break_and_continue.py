# break and continue statements in loops

print ('-------------------- break statement-----------------------')
# when 'break' statement executes inside a loop, control flow 'breaks' out of the loop immediately

i = 0

print ('break in while loop')
while i < 7:
    print (i)
    if i == 4:
        print ('Breaking from loop')
        break
    i += 1

"""
1. The loop conditionals will not be executed after the break statement is executed.
2. Note that break statements are allowed only inside the loops syntactically
3. A break stat. inside a function can't be used to terminate the loop that called that function
4. Just like while, break statement can be used in for loops.
5. If a loop has an else clause, it does not execute when the loop is terminated through break statement.
"""
print ('break in for loop')
for i in (0, 1, 2, 3, 4, 5):
    print (i)
    if i == 2:
        break

print ('-------------------- continue statement-----------------------')

"""
continue stat. will skip to the next iteration of the loop bypassing the rest of the current block
but continuing the loop
"""

for i in (0, 1, 2, 3, 4, 5):
    if i == 2 or i == 4:
        continue
    print (i)

"""
In above snippet, 2 and 4 will not be printed, This is because continue goes to next iteration skipping all other 
statements after the continue.
"""

"""
Things to remember:
break and continue only operate on a single level of loop. Python doesn't have the ability to break out of 
multiple loops at once. If this behaviour is desired, refactoring one or more loops into a function and replacing
break with return statement may be the way to go.
The return statement exits from a function, without executing the code that comes after it.
 
"""
