# write a function that returns the largest element in a list
l = [1,2,3,4,5,6,7,8,9]
def m(l):
    return max(l)
m(l)
# write function that reverses a list, preferably in place
def rev(l):
    l.reverse()
    return l
rev(l)

# write a function that checks whether an element occurs in a list
def occ(l):
    i = int(input('Enter element'))
    if i in l:
        return print('element occurs in the list')
    else:
        return print('element doesn\'t occur in the list')
occ(l)

# write a function that returns the elements on odd positions in a list
l[0::2]

# write a function that computes the running total of a list
def runningtotal(l):
    l1 = [l[0]]
    for i in range(1, len(l)):
        l1.append(l1[i-1]+l[i])
    return print(l1)
runningtotal(l)

# write a function that test whether a string is a palindrome
a = str(input('enter string: ')).upper()
def palindrome(a):
    if a == a[::-1]:
        return print(f'{a} is a palindrome')
    else:
        return print(f'{a} isn\'t a palindrome')
palindrome(a)

# write three functions that compute the sum of the numbers in a list: using a for-loop, a while-loop and recursion
# (Subject to availability of these constructs in your language of choice)
def sumofnumber(l):
    s = 0
    for i in l:
        s += i
    return print(s)
sumofnumber(l)

i = 0
s = 0
while i < len(l):
    s += l[i]
    i +=1
print(s)

def s(l):
    if len(l) == 0:
        return 0
    else:
        return l[0] + s(l[1:])

print(s(l))

# Write a function on_all that applies a function to every element of a list. Use it to print the first twenty perfect squares. 
# The perfect squares can be found by multiplying each natural number with itself. THe first few perfect square are 1*1=1, 2*2=4, 3*3=9, 4*4=16. 
# Twelve for example is not a perfect square because there is no natural number m so that m*m=12. (This question is tricky if your programming
# language makes it difficult to pass functions as arguments)

# write a function that concatenates two lists [a,b,c], [1,2,3] -> [a,b,c,1,2,3]
def conc(a,b):
    return a + b
conc(a,b)

# write a function that combines two lists by alternatingly taking elements, e.g. [a,b],[1,2] -> [a,1,b,2]
def combine(l1,l2):
    nl = []
    if len(l1) >= len(l2):    
        for i in range(len(l1)):
            if i < len(l2):
                nl.append(l1[i])
                nl.append(l2[i])
            else:
                nl.append(l1[i])
    else:
        for i in range(len(l2)):
            if i < len(l1):
                nl.append(l1[i])
                nl.append(l2[i])
            else:
                nl.append(l2[i])
    return nl
combine([1,2,3,6],[4,5,5,7,8])

# write a function that merges two sorted lists into a new sorted list [1,4,6],[2,3,5].
# You can do this quicker than concatenation them followed by a sort
def sortedconcatenation(l1, l2):
    nl = l1 + l2
    nl.sort()
    return nl
sortedconcatenation([1,2,3,6],[4,5,5,7,8])

# write a function that rotates a list by k elements. For example [1,2,3,4,5,6] rotated by two becomes [3,4,5,6,1,2]. 
# Try solving this without creating a copy of the list. How many swap or move operations do you need?

def rotate(l,k):
    if k < len(l):
        return l[k:len(l)] + l[0:k]
    else:
        return print('list index out of range')
rotate([1,2,3,4,5],9)

# write a function that computes the list of the first 100 Fibonacci numbers.The first two Fibonacci numbers
# are 1 and 1. The n+1-st Fibonacci number can be computed by adding the n-th and the n-1-th Fibonaci number.
#The first few are therefore 1,1,1+1=2, 1+2=3,2+3=5,3+5=8

def fibonaccinumbers(l=[],n=100):
    l = l + [1,1]
    for k in range(2,n):
        l.append(l[k-1]+l[k-2])
    return l
fibonaccinumbers()

# write a function that takes a number and returns a list of its digit. So for 2342 it should return[2,3,4,2]
def numtolist(x):
    l = []
    for i in range(len(str(x))):
        l.append(int(str(x)[i]))
    return l
numtolist(1234556)

# write functions that add, subtract, and multiply two numbers in their digit-list representation
# (and return a new digit list). If you're ambitious you can implement Karatsuba multiplication.
# Try different bases. What is the best base if you care about speed? If you couldn't completely solve the prime
# number exercise above due to the lack of large numbers in your language, you can now use your own library for this task

