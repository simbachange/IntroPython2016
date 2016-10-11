def fib(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1
    else:
        return fib (n-2) + fib (n-1)
"""this function creates a recursion or fibonacci series that outputs the next 
number as the sum of the previous two numbers"""


def lucas(n):
    if n == 0:
        return 0
    elif == 1:
        retrun 1
    else:
        return lucas (n-1) + lucas (n-2)

"""this function creates a recursion or lucas numbers liner recursion which is the sum of its 
first two immediate terms"""
 

for n in range (0,15):
    print (fib(n))
    print (lucas(n))