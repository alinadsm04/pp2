'''
1. Create a generator that generates the squares of numbers up to some number N.
2. Write a program using generator to print the even numbers between 0 and n in comma
separated form where n is input from console.
3. Define a function with a generator which can iterate the numbers, which are divisible
by 3 and 4, between a given range 0 and n.
4. Implement a generator called squares to yield the square of all numbers from (a) to (b).
Test it with a "for" loop and print each of the yielded values.
5. Implement a generator that returns all numbers from (n) down to 0.
'''
# 1)
def sqrt_num(n):
    num = 1
    while num <= n:
        yield num ** 2
        num += 1

n = int(input())
for i in sqrt_num(n):
    print(i)


# 2)
def evenn(n):
   for i in range(n):
     if i % 2 == 0: 
       yield i

n = int(input())
even = evenn(n)
print(", ".join(str(x) for x in even))


# 3)
def divs(n):
  for i in range (n):
    if i % 3 == 0 and i % 4 == 0:
      yield i

n = int(input())
div = divs(n)
print(" ".join(str(x) for x in div))

# 4)
def squares(a, b):
    for i in range(a, b+1):
        yield i**2

a, b = int(input()), int(input())

for square in squares(a, b):
    print(square)


# 5)
def reverse_num(n):
  s = (i for i in range (n))
  for i in range (n, 0, -1):
    yield i

n = int(input())
revers = reverse_num(n)
print(", ".join(str(i) for i in revers))