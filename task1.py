# Write a program that prints 'Hello World' to the screen
print('Hello World')

# Write a program that asks the user for their name and greets them with their name
print('what is your name?')
a = input('My name is ')
print(f'Hello {a}')

# Modify the previous program such that only the users Alice and Bob are greeted with their names
print('what is your name?')
a = input('My name is ')
if a == 'Alice' or a == 'Bob':
    print(f'Hello {a}')

# Write a program that asks the user for a number n and prints the sum of the numbers 1 to n
n = int(input('I like number: '))
s = 1
for i in range(2,n+1):
    s += i
print(f'sum of the numbers of 1 to n is {s}')

# Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3,5,6,9,10,12,15 for n = 17
n = int(input('I like number: '))
s = 0
for i in range(1,n+1):
    if i % 3 == 0 or i % 5 == 0:
        s += i
print(f'sum of multiples of three or five is {s}')

# Write a program that asks the user for a number n and gives them the possibility to choose between computing the sum and computing the product of 1,...,n
n = int(input('I like number: '))
c = str(input('enter x for product until n or + for sum until n'))

def multi(n):
    m = 1
    for i in range(2,n+1):
        m *= i
    return m

def sum(n):
    s = 1
    for i in range(2,n+1):
        s += i
    return s

if c == 'x':
    print(f'product until n: {multi(n)}')
elif c == '+':
    print(f'sum until n: {sum(n)}')

# Write a program that prints a multiplication table for numbers up to 12
n = 12
for i in range(1,n+1):
    print(list(range(1*i, (n+1)*i,i)))

# Write a program that prints all prime numbers. (Note: if your programming language does not support arbitrary size numbers
# , printing all primes up to the largest number you can easily represent is fine too)
n = int(input('Enter number: '))
for i in range(1,n):
    try:
        for x in range(2,i):
            if i % x == 0:
                break
        if x == i-1:
            print(i)
    except:
        print(i)

# Write a guessing game where the user has to guess a secret number. After every guess the program tells the user whether their number was too large or too small. 
# At the end the number of tries needed should be printed. It counts only as one try if they input the same number multiple times consecutively.
import random
x = random.randint(1,100)
n = 0
g = 'n'
t = 'start'
while g != x:
    g = int(input('I guess number '))
    if g != x:
        if g > x:
            print('number is too large')
        else:
            print('number is too small')
        if g != t:
            t = g
            n += 1
    else:
        n += 1
print(f'{n} times guess')

# Write a program that prints the next 20 leap years
y = int(input('This year is '))
def leap(y):
    for i in range(1,9):
        y += 1
        if y % 400 == 0:
            break
        elif y % 4 == 0 and y % 100 != 0:
            break
    return y
n = 0
while n < 20:
    print(leap(y))
    n +=1
    y = leap(y)

# Write a program that computes the sum of an alternating series where each element of the series is an expression of the 
# form ((-1)^{k+1})/(2* k-1) for each value of k from 1 to a million, multiplied by 4. Or, in more mathematical notation
#   4\cdot \sum_{k=1}^{10^6} \frac{(-1)^{k+1}}{2k-1} = 4\cdot(1-1/3+1/5-1/7+1/9-1/11\ldots).